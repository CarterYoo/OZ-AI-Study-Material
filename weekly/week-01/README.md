# Week 01 / Linear regression and gradient descent

Calculate predictions and compare them with targets. Turn those errors into a cost, draw its shape, and then use the slope to update a weight.

## Handouts

| Activity | Student PDF | Worked answers |
| :--- | :--- | :--- |
| Cost function and cost surface | [Worksheet](handouts/cost-function.worksheet.ko.pdf) | [Answer key](handouts/cost-function.answers.ko.pdf) |
| Implementing gradient descent | [Worksheet](handouts/gradient-descent.worksheet.ko.pdf) | [Answer key](handouts/gradient-descent.answers.ko.pdf) |

[Concept check](handouts/concept-check.ko.pdf): ten multiple-choice questions, a pseudocode debugging exercise, and an open-response question.

The cost-surface worksheet uses eight input/target pairs. The gradient-descent worksheet uses five hand-calculated steps for each learning rate, in the order **divergence, very slow movement, convergence**, with one large `w, J(w)` graph for each case. Red answers show the intermediate calculations.

## Colab

| Notebook | Open |
| :--- | :--- |
| Four optional labs, student edition | [Open in Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/optional-labs.student.ipynb) |
| Four optional labs, answer edition | [Open in Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/optional-labs.answers.ipynb) |
| Cell-by-cell cost-function exploration | [Open in Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/cost-function.interactive.ko.ipynb) |

The optional labs are in English. The interactive cost lab is in Korean and uses eight actual Auto MPG observations, comparing targets, predictions, and errors with different colors. Run its cells in order before using the sliders.

[Teaching notes](teaching-notes.ko.md) · [LaTeX source and figure assets](source/) · [Dataset](data/auto-mpg.csv)

The earlier [standalone HTML demonstration](demos/cost-function.legacy.ko.html) is preserved as an archive. Use the cell-by-cell Colab for the classroom activity.
