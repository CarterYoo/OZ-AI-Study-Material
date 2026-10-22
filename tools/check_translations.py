"""Check paired language editions and the preservation of calculations and code."""

import ast
from collections import Counter
import json
import re
import zipfile
from pathlib import Path

import nbformat
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
MATH = re.compile(r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|(?<!\\)\$(?:\\.|[^$\n])+(?<!\\)\$")
handouts = []
for korean in sorted(ROOT.glob("**/source/*.ko.tex")):
    english = korean.with_name(korean.name.replace(".ko.tex", ".en.tex"))
    ko = korean.read_text(encoding="utf-8")
    en = english.read_text(encoding="utf-8")
    assert not re.search("[가-힣]", en), english
    assert re.findall(r"\\(?:q|question)\{(\d+)\}", ko) == re.findall(r"\\(?:q|question)\{(\d+)\}", en)
    drawing = re.compile(r"^\s*\\(?:draw|fill|path|clip)\b[^\n]*", re.M)
    assert drawing.findall(ko) == drawing.findall(en), english
    ko_pdf = korean.parent.parent / "handouts" / korean.with_suffix(".pdf").name
    en_pdf = english.parent.parent / "handouts" / english.with_suffix(".pdf").name
    original, translated = PdfReader(ko_pdf), PdfReader(en_pdf)
    assert len(original.pages) == len(translated.pages), english
    assert not re.search("[가-힣]", "\n".join(page.extract_text() or "" for page in translated.pages)), en_pdf
    handouts.append({"english": en_pdf.relative_to(ROOT).as_posix(), "pages": len(translated.pages)})

notebook_pairs = []
for english in sorted(ROOT.glob("**/notebooks/optional-labs.*.ipynb")):
    if ".ko." in english.name:
        continue
    korean = english.with_name(english.name.replace(".ipynb", ".ko.ipynb"))
    en, ko = nbformat.read(english, as_version=4), nbformat.read(korean, as_version=4)
    assert len(en.cells) == len(ko.cells)
    for a, b in zip(en.cells, ko.cells):
        assert a.cell_type == b.cell_type and a.id == b.id
        if a.cell_type == "code":
            assert a == b, (korean, a.id)
        else:
            assert "ZXQ" not in b.source
            if a not in en.cells[:4]:
                assert Counter(MATH.findall(a.source)) == Counter(MATH.findall(b.source)), (korean, a.id)
    anchors = set(re.findall(r'<a (?:id|name)=["\']([^"\']+)', "\n".join(c.source for c in ko.cells)))
    for anchor in re.findall(r"\]\(#(week\d+lab\d+)\)", ko.cells[1].source):
        assert anchor in anchors, (korean, anchor)
    notebook_pairs.append(korean.relative_to(ROOT).as_posix())


class RemoveVisibleText(ast.NodeTransformer):
    def visit_Constant(self, node):
        return ast.copy_location(ast.Constant(value="TEXT"), node) if isinstance(node.value, str) else node


cost_en = nbformat.read(ROOT / "weekly/week-01/notebooks/cost-function.interactive.en.ipynb", as_version=4)
cost_ko = nbformat.read(ROOT / "weekly/week-01/notebooks/cost-function.interactive.ko.ipynb", as_version=4)
assert len(cost_en.cells) == len(cost_ko.cells)
for english, korean in zip(cost_en.cells, cost_ko.cells):
    assert english.cell_type == korean.cell_type and english.id == korean.id
    if english.cell_type == "code":
        a, b = ast.parse(english.source), ast.parse(korean.source)
        assert ast.dump(RemoveVisibleText().visit(a)) == ast.dump(RemoveVisibleText().visit(b))
    else:
        assert Counter(MATH.findall(english.source)) == Counter(MATH.findall(korean.source))

course_en = ROOT / "common/course-1/slides/course-1-weeks-01-to-03.en.pptx"
course_ko = ROOT / "common/course-1/slides/course-1-weeks-01-to-03.pptx"
with zipfile.ZipFile(course_en) as en, zipfile.ZipFile(course_ko) as ko:
    assert set(en.namelist()) == set(ko.namelist())
    changed = [name for name in en.namelist() if en.read(name) != ko.read(name)]
    assert len(changed) == 169 and all(re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", n) for n in changed)
for relative in ["common/course-1/teaching-notes.en.md", "common/transformers/teaching-notes.en.md", "common/ai-safety/notes/technical-solutions.en.md"]:
    assert not re.search("[가-힣]", (ROOT / relative).read_text(encoding="utf-8"))

transformer_en = PdfReader(ROOT / "common/transformers/slides/transformer-from-scratch.en.pdf")
assert len(transformer_en.pages) == 24
assert not re.search("[가-힣]", "\n".join(page.extract_text() or "" for page in transformer_en.pages))
print(json.dumps({"handout_pairs": len(handouts), "english_handout_pages": sum(r["pages"] for r in handouts),
                  "optional_notebook_pairs": len(notebook_pairs), "optional_code_cells_identical": True,
                  "notebook_math_preserved": True, "cost_notebook_nontext_code_identical": True,
                  "course_english_note_bodies": 169, "course_slide_images_unchanged": True,
                  "transformer_english_slides": 24}, indent=2))
