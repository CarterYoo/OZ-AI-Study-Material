# Publication checks

The public package was assembled on October 21, 2026.

| Check | Result |
| :--- | :--- |
| Printable handouts | 13 Korean and 13 English handouts; 144 pages rendered for visual review |
| Compiler diagnostics | No overflowing boxes or missing-character warnings in the rebuilt handouts |
| Notebook files | 18 notebook schemas checked; public copies have no saved execution outputs |
| Optional labs | 19 labs, with 81 mathematical exercises in the combined student copy |
| Weekly split | 4 labs in Week 1, 6 in Week 2, 9 in Week 3; lab cells and setup cells match the combined copies |
| Sigmoid worksheet and answers | Both use the revised seven-point dataset; fitted lines and the MSE nonconvexity example checked independently |
| Course slide export | 169 slides retained in both note-language editions; all English notes translated; slide XML and media preserved byte for byte |
| Detailed speaker script | 164 sections and 1,215 source sentences retained in the English translation; 12 representative sections independently reviewed |
| Presentations | Six PowerPoint packages checked; translated safety decks rendered and reviewed for wrapping and overlap |
| Transformer introduction | 24 English slides translated from the adapted Korean edition, including 182 instructional text blocks and all speaker notes |
| Korean optional labs | Explanations translated; all executable cells and notebook math retained; navigation checked in each weekly copy |
| Navigation | Relative Markdown links checked against the published files |
| File catalog | SHA-256 checksums recorded in `materials.json` |

The lab execution history is described in the separate [Colab validation record](optional-lab-validation.md). Publication checks did not execute a new Colab runtime or test every interactive control.

The bilingual review corrected three inherited prose errors in the optional labs: min-max scaling maps to [0, 1], a weight near zero contributes little to the current prediction, and new prediction inputs use the training-set normalization statistics. Executable cells were preserved. Escaped `J` labels were also repaired in the published Korean sigmoid handout sources without changing their calculations.

Run `python tools/check_materials.py` and `python tools/check_translations.py` from the repository root to repeat the static checks.
