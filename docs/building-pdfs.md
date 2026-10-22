# Building the handouts

The finished PDFs are ready to print. To edit a handout, change its matching `.tex` file under `source/` and rebuild it.

## Requirements

Install Python 3 and a TeX distribution with **XeLaTeX**, such as TeX Live or MiKTeX. The sources use common packages including `fontspec`, `amsmath`, `tikz`, `tabularx`, and `fancyhdr`. Noto Sans KR fonts and their license are included under `common/assets/fonts/`; the source files use relative paths to them.

From the repository root, build one handout:

```sh
python tools/build_pdfs.py weekly/week-03/source/sigmoid-logistic.worksheet.ko.tex
```

Build all handouts:

```sh
python tools/build_pdfs.py
```

The builder runs XeLaTeX twice, keeps intermediate files under `.build/`, and writes the resulting PDF into the corresponding `handouts/` folder. It reports missing glyphs or overflowing boxes so you can inspect them before distribution.

## Checks

```sh
python -m pip install -r tools/requirements.txt
python tools/check_materials.py
```

The check validates notebook schemas, the weekly notebook split, exercise counts, PDF readability, slide packages, relative documentation links, and catalog checksums. It also checks the revised sigmoid dataset and its fitted lines. It does not run unfinished student notebooks or simulate every plot interaction.
