<img src="docs/assets/banner.svg" alt="OZ AI Study: from the first prediction to understanding models" width="100%">

# OZ AI Study Material

[English](README.md) · [한국어](README.ko.md)

Hands-on materials for students learning machine learning before building a Transformer from scratch. Start with a prediction you can calculate by hand, plot its error, and work toward models you can implement and inspect.

**[Weekly materials](weekly/README.md)** · **[Common resources](common/README.md)** · **[Student Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/common/course-1/notebooks/optional-labs.student.ipynb)** · **[Answer Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/common/course-1/notebooks/optional-labs.answers.ipynb)**

## Start here

1. Open a week's README and print the student handouts. Calculate the values and plot the points before checking the worked answers.
2. Open its student notebook in Colab. Run the two setup cells, then work through the labs in order. Each mathematical exercise needs one expression; the surrounding code is provided.
3. Use the separate answer notebook and PDF answer keys to check your steps. Speaker notes are available for instructors.

Choose English or Korean on each material's page. The optional labs run on a Colab CPU runtime. Student notebooks deliberately stop at unfinished `TODO(...)` expressions. Replace them before using **Run all**.

## Weekly materials

Week numbers follow **Machine Learning Specialization, Course 1**, rather than calendar dates. A week can span several study meetings.

| Week | Topics | Hand calculations | Coding |
| :--- | :--- | :--- | :--- |
| [01](weekly/week-01/README.md) | Linear regression, cost functions, gradient descent | Predictions, MSE, cost surfaces, five update steps with three learning rates | [Student](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/optional-labs.student.ipynb) · [Answers](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/optional-labs.answers.ipynb) |
| [02](weekly/week-02/README.md) | Multiple features, vectorization, feature scaling | Seven examples, predictions, parameter updates, contours before and after scaling | [Student](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-02/notebooks/optional-labs.student.ipynb) · [Answers](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-02/notebooks/optional-labs.answers.ipynb) |
| [03](weekly/week-03/README.md) | Classification, sigmoid, decision boundaries, logistic loss | Seven examples, sigmoid values, probability curves, MSE and logistic cost | [Student](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.student.ipynb) · [Answers](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.answers.ipynb) |

Each week also contains a concept check, teaching notes, and editable LaTeX sources. The optional labs cover the full Course 1 week; a particular worksheet may cover a smaller part.

## Common resources

| Resource | Contents | Open |
| :--- | :--- | :--- |
| AI safety | Two decks in both languages, with full speaker notes and sources | [Materials](common/ai-safety/README.md) |
| Linear algebra | A visual concept quiz with simple calculations, drawings, and a separate worked answer key | [Materials](common/linear-algebra/README.md) |
| Course 1 | The combined annotated slide deck, detailed teaching notes, and all 19 optional labs in one notebook | [Materials](common/course-1/README.md) |
| Transformers | A 24-slide introduction and beginner-oriented speaker notes | [Materials](common/transformers/README.md) |

## Languages and file formats

The teaching materials are available in **Korean and English**, including the handouts, worked answers, detailed speaker notes, adapted presentations, and Colab explanations. Korean originals are retained. `.ko` and `.en` identify language editions; existing optional-lab notebooks without a language suffix are the English editions.

Equations, datasets, examples, and worked steps are shared across translations. Executable code and its original comments remain in English in both notebook editions. The combined course slides retain their English source images and have separate Korean-note and English-note decks.

| Format | Use |
| :--- | :--- |
| `.pdf` | Print or read a finished handout |
| `.tex` | Edit the handout; see [building PDFs](docs/building-pdfs.md) |
| `.ipynb` | Open in Colab and run one cell at a time |
| `.pptx` | Import into Google Slides or open in PowerPoint |
| `.md` | Read teaching notes directly on GitHub |

Worksheet answers are kept in separate files and use red text and graph marks. Each weekly concept check contains ten multiple-choice questions, a pseudocode debugging exercise, and an open-response question.

## Repository map

```text
common/
    ai-safety/          Presentations and speaker notes
    linear-algebra/     Visual quiz and worked answers
    course-1/           Shared slides, notes, and combined notebooks
    transformers/       Transformer introduction
    assets/fonts/       Fonts and their license
weekly/
    week-01/            Linear regression and gradient descent
    week-02/            Multiple regression and feature scaling
    week-03/            Sigmoid and logistic regression
docs/                   Build instructions, sources, and validation notes
tools/                  PDF builder and repository checks
third_party/            Upstream license notices
materials.json          File catalog and SHA-256 checksums
```

## Validation and sources

The integrated labs were previously tested by filling all **81 mathematical exercises** in a separate copy and running **207 nonempty code cells** in order on a restarted Colab CPU runtime. Five gradient functions were checked independently with finite differences. See the [validation record](docs/optional-lab-validation.md) for the environment and limits of that run; it is not a guarantee for future library versions or every widget interaction.

The public package also checks notebook structure, the weekly split, source dependencies, and matching worksheet data. The sigmoid worksheet and answer key use the same revised seven-point dataset, including a boundary-near exception. The full Course 1 English script preserves all 164 detailed sections and 1,215 source sentences.

Course materials are based on Andrew Ng's Machine Learning Specialization from DeepLearning.AI and Stanford Online. Lab sources, 3Blue1Brown videos, datasets, and AI safety readings are listed in [sources and acknowledgments](docs/sources.md).

The existing [MIT license](LICENSE) covers the repository's original contributions. Third-party materials retain their own notices and terms; see [NOTICE](NOTICE.md).
