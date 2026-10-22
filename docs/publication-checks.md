# Publication checks

The public package was assembled on October 21, 2026.

| Check | Result |
| :--- | :--- |
| Printable handouts | All 13 LaTeX documents rebuilt; 72 pages rendered for visual review |
| Compiler diagnostics | No overflowing boxes or missing-character warnings in the rebuilt handouts |
| Notebook files | Nine notebook schemas checked; public copies have no saved execution outputs |
| Optional labs | 19 labs, with 81 mathematical exercises in the combined student copy |
| Weekly split | 4 labs in Week 1, 6 in Week 2, 9 in Week 3; lab cells and setup cells match the combined copies |
| Sigmoid worksheet and answers | Both use the revised seven-point dataset; fitted lines and the MSE nonconvexity example checked independently |
| Course slide export | 169 slides retained; 164 speaker-note sections refreshed; slide XML and media preserved byte for byte |
| Presentations | Three PowerPoint packages checked for archive integrity and readable XML |
| Navigation | Relative Markdown links checked against the published files |
| File catalog | SHA-256 checksums recorded in `materials.json` |

The lab execution history is described in the separate [Colab validation record](optional-lab-validation.md). Publication checks did not execute a new Colab runtime or test every interactive control.

Run `python tools/check_materials.py` from the repository root to repeat the static checks.
