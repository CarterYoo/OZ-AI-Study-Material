"""Compile the portable LaTeX handouts into their public PDF paths."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
engine = shutil.which("xelatex")
if engine is None:
    raise SystemExit("Install XeLaTeX and make it available on PATH.")

sources = [Path(p).resolve() for p in sys.argv[1:]] if len(sys.argv) > 1 else sorted(ROOT.glob("**/source/*.tex"))
results = []
for source in sources:
    relative = source.relative_to(ROOT)
    build = ROOT / ".build" / relative.parent.parent / source.stem
    build.mkdir(parents=True, exist_ok=True)
    command = [engine, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", f"-output-directory={build}", source.name]
    for _ in range(2):
        result = subprocess.run(command, cwd=source.parent, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode:
            raise SystemExit(result.stdout[-6000:] + result.stderr[-2000:])
    destination = source.parent.parent / "handouts" / source.with_suffix(".pdf").name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(build / source.with_suffix(".pdf").name, destination)
    warnings = [line for line in result.stdout.splitlines() if any(term in line for term in ["Overfull", "Missing character"])]
    row = {"path": destination.relative_to(ROOT).as_posix(), "warnings": warnings}
    results.append(row)
    print(json.dumps(row), flush=True)

(ROOT / ".build/pdf-build.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
