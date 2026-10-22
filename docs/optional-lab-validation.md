# Validation summary

All 19 Course 1 optional labs were executed in order on a restarted Colab CPU runtime. All 81 mathematical blanks were independently implemented in a separate copy. Both setup cells were included. All 207 nonempty code cells passed, including the embedded implementation checks. Five gradient functions additionally matched central finite differences of independently defined objectives on seeded random inputs.

One compatibility issue was found in two Week 2 multiple variable regression output cells: a valid Python float prediction does not have a `.shape` attribute. The checked student copy uses `np.shape(f_wb)` instead of `f_wb.shape`. Its 81 TODOs remain intact. The original Google Drive notebook was not modified.

The first audit attempt also exposed a test harness issue: capturing display output hides the display publisher hook needed by Colab widget setup. The harness was corrected to preserve the native display publisher for that setup cell; no notebook change was required for this issue.

Environment: Python 3.13.15, NumPy 2.1.3, Matplotlib 3.10.0, scikit-learn 1.6.1, ipympl 0.9.7. Complete sequential execution took 51.17 seconds, excluding restart and transfer.

The tested execution produced dependency deprecation warnings, but no numerical or runtime failures. Interactive plots were constructed successfully; browser mouse interactions and every widget callback were not manually exercised. This validates the executed examples and numerical checks, not all possible student implementations or future library versions.

The public [combined student notebook](../common/course-1/notebooks/optional-labs.student.ipynb) is based on the corrected, symbol-checked student copy. The separate [answer notebook](../common/course-1/notebooks/optional-labs.answers.ipynb) contains the completed expressions. Runtime outputs are cleared in the public notebooks so each copy can be run afresh. The week-specific notebooks preserve their corresponding lab cells and include both setup cells.

This is the record of the earlier Colab validation, rather than a new execution during repository publication. See the [publication checks](publication-checks.md) for checks performed on the distributed package.
