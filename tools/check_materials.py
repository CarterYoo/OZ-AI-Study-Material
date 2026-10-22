"""Check the published file catalog, notebook splits, and teaching artifacts."""

import ast
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET

import nbformat
import numpy as np
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
catalog_path = ROOT / "materials.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
files = sorted(p for p in ROOT.rglob("*") if p.is_file() and not any(
    part.startswith(".") or part == "__pycache__" for part in p.relative_to(ROOT).parts
) and p != catalog_path)

if "--refresh-catalog" in sys.argv:
    records = {row["path"]: row for row in catalog["materials"]}
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        row = records.get(relative)
        if row is None:
            counterparts = [relative.replace(".en.", ".ko."), relative.replace(".en.", "."),
                            relative.replace(".ko.", "."), relative.replace(".ko.", ".en.")]
            original = next((records[p] for p in counterparts if p != relative and p in records), None)
            row = {"path": relative, "source": original["path"] if original else "OZ Lab",
                   "language": "en", "role": original["role"] if original else "repository support"}
        if ".ko." in path.name:
            row["language"] = "ko"
        elif ".en." in path.name:
            row["language"] = "en"
        row.update(bytes=path.stat().st_size, sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        records[relative] = row
    catalog["materials"] = [records[p.relative_to(ROOT).as_posix()] for p in files]
    catalog_path.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8", newline="\n")

for row in catalog["materials"]:
    path = ROOT / row["path"]
    assert path.is_file(), row["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"], row["path"]
assert {row["path"] for row in catalog["materials"]} == {p.relative_to(ROOT).as_posix() for p in files}

for path in files:
    if path.suffix == ".md":
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if re.match(r"(?:https?://|mailto:|#)", target):
                continue
            target = unquote(target.split("#")[0])
            if target:
                assert (path.parent / target).exists(), (path.relative_to(ROOT), target)

notebooks = {}
todo_counts = {}
for path in files:
    if path.suffix != ".ipynb":
        continue
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    assert "widgets" not in notebook.metadata
    calls = 0
    for cell in notebook.cells:
        if cell.cell_type != "code":
            continue
        assert cell.execution_count is None and not cell.outputs, path
        source = "\n".join(line for line in cell.source.splitlines() if not line.lstrip().startswith(("%", "!")))
        tree = ast.parse(source)
        calls += sum(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "TODO" for node in ast.walk(tree))
    relative = path.relative_to(ROOT).as_posix()
    notebooks[relative] = notebook
    todo_counts[relative] = calls

student = notebooks["common/course-1/notebooks/optional-labs.student.ipynb"]
answers = notebooks["common/course-1/notebooks/optional-labs.answers.ipynb"]
assert len(student.cells) == len(answers.cells) == 578
assert todo_counts["common/course-1/notebooks/optional-labs.student.ipynb"] == 81
assert todo_counts["common/course-1/notebooks/optional-labs.answers.ipynb"] == 0
week_labs = {}
for edition in ["student", "answers"]:
    combined = notebooks[f"common/course-1/notebooks/optional-labs.{edition}.ipynb"]
    by_id = {cell.id: cell for cell in combined.cells[4:]}
    included = []
    for week, expected in [(1, 4), (2, 6), (3, 9)]:
        notebook = notebooks[f"weekly/week-{week:02d}/notebooks/optional-labs.{edition}.ipynb"]
        assert notebook.cells[2:4] == combined.cells[2:4]
        for cell in notebook.cells[4:]:
            assert cell == by_id[cell.id], (week, cell.id)
        labs = {(cell.metadata.source_lab.week, cell.metadata.source_lab.lab) for cell in notebook.cells if "source_lab" in cell.metadata}
        assert len(labs) == expected and all(w == week for w, _ in labs)
        included.extend(cell.id for cell in notebook.cells[4:])
        week_labs[str(week)] = len(labs)
    assert len(included) == len(set(included)) == len(combined.cells)-4

pdf_pages = {}
for path in files:
    if path.suffix == ".pdf":
        reader = PdfReader(path)
        assert len(reader.pages) > 0
        pdf_pages[path.relative_to(ROOT).as_posix()] = len(reader.pages)
assert pdf_pages["weekly/week-03/handouts/sigmoid-logistic.worksheet.ko.pdf"] == 9
assert pdf_pages["weekly/week-03/handouts/sigmoid-logistic.answers.ko.pdf"] == 9
pdf_student = "\n".join(page.extract_text() or "" for page in PdfReader(ROOT / "weekly/week-03/handouts/sigmoid-logistic.worksheet.ko.pdf").pages)
pdf_answers = "\n".join(page.extract_text() or "" for page in PdfReader(ROOT / "weekly/week-03/handouts/sigmoid-logistic.answers.ko.pdf").pages)
for text in [pdf_student, pdf_answers]:
    assert "1015" in text and "104" in text and "27" in text

slide_counts = {}
for path in files:
    if path.suffix == ".pptx":
        with zipfile.ZipFile(path) as package:
            assert package.testzip() is None
            for name in package.namelist():
                if name.endswith(".xml"):
                    ET.fromstring(package.read(name))
            slide_counts[path.relative_to(ROOT).as_posix()] = len([n for n in package.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)])

math = json.loads((ROOT / "weekly/week-03/data/calculation-checks.json").read_text(encoding="utf-8"))
x, y = np.array(math["x"], dtype=float), np.array(math["y"], dtype=float)
assert x.tolist() == [1, 2, 6, 8, 9, 10, 27] and y.tolist() == [0, 0, 1, 0, 1, 1, 1]
design = np.column_stack([x, np.ones(len(x))])
np.testing.assert_allclose(np.linalg.lstsq(design[:6], y[:6], rcond=None)[0], [.1, -.1], atol=1e-12)
np.testing.assert_allclose(np.linalg.lstsq(design, y, rcond=None)[0], [1/28, 1/4], atol=1e-12)
assert math["mse_nonconvex_witness"]["midpoint_cost"] > math["mse_nonconvex_witness"]["endpoint_average"]
for edition in ["worksheet", "answers"]:
    source = (ROOT / f"weekly/week-03/source/sigmoid-logistic.{edition}.ko.tex").read_text(encoding="utf-8")
    assert len(re.findall(r"\\q\{\d+\}", source)) == 28
    assert "1015w^2-104w+4" in source
    assert not any(ord(c) < 32 and c not in "\r\n\t" for c in source)

result = {
    "catalog_files": len(catalog["materials"]), "notebooks": len(notebooks),
    "student_exercises": 81, "weekly_labs": week_labs, "pdf_pages": pdf_pages,
    "presentation_slides": slide_counts, "relative_document_links": "passed",
    "weekly_notebook_cells_preserved": True, "sigmoid_data_and_fits": "passed",
    "scope": "Static publication checks; no new Colab runtime execution.",
}
print(json.dumps(result, indent=2))
