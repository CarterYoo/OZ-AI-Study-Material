# Week 03 / Cost Functions and Gradient Descent

Canva pages **43 to 73** in the [combined classroom deck](https://www.canva.com/design/DAHVe4UysZI/view).

[Classroom slide PDF](slides/oz-ai-study-03.pdf) (31 slides) · [Editable PowerPoint](slides/oz-ai-study-03.pptx)

Original ML source slides 35 to 65, with the OZ orange and gray theme.

[English lesson notes](lesson-notes.en.md) · [Full Korean course notes](../../common/course-1/teaching-notes.ko.md)

## Handouts

| Activity | English worksheet | English worked answers | Korean worksheet | Korean worked answers |
| :--- | :--- | :--- | :--- | :--- |
| Cost function and cost surface | [PDF](handouts/cost-function.worksheet.en.pdf) | [PDF](handouts/cost-function.answers.en.pdf) | [PDF](handouts/cost-function.worksheet.ko.pdf) | [PDF](handouts/cost-function.answers.ko.pdf) |
| Gradient descent by hand | [PDF](handouts/gradient-descent.worksheet.en.pdf) | [PDF](handouts/gradient-descent.answers.en.pdf) | [PDF](handouts/gradient-descent.worksheet.ko.pdf) | [PDF](handouts/gradient-descent.answers.ko.pdf) |

Calculate predictions and cost from eight input/target pairs. Plot `J(w)` and `J(w,b)`, compare the surface with its contours, then take five gradient descent steps for each learning rate. The cases proceed from divergence to very slow movement to convergence. Worked answers show the intermediate calculations and graph marks in red.

Concept check: [English](handouts/concept-check.en.pdf) · [Korean](handouts/concept-check.ko.pdf). This source Course 1 Week 1 review also revisits the foundations from OZ Week 2.

## Colab

| Resource | English | Korean |
| :--- | :--- | :--- |
| Course 1 source Week 1 optional labs | [Student](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.student.ipynb) · [Answers](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.answers.ipynb) | [Student](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.student.ko.ipynb) · [Answers](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.answers.ko.ipynb) |
| Cell-by-cell cost exploration | [Open](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/cost-function.interactive.en.ipynb) | [Open](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/cost-function.interactive.ko.ipynb) |

Start with **Cost Function**. The **Gradient Descent** implementation lab also supports the opening of Week 4. Python/Jupyter and Model Representation are the prerequisites used in Week 2.

Open any notebook in Colab using the notebook links below. The interactive lab uses eight actual Auto MPG observations and distinguishes targets, predictions, and errors by color.

[Source Week 1 notes, English](teaching-notes.en.md) · [Source Week 1 notes, Korean](teaching-notes.ko.md) · [Editable worksheet sources](source/) · [Dataset](data/auto-mpg.csv)
