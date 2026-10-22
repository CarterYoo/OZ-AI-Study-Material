# Week 01 / Linear regression and gradient descent

Calculate predictions and compare them with targets. Turn those errors into a cost, draw its shape, and then use the slope to update a weight.

## Handouts

| Activity | English worksheet | English answers | 한국어 문제 | 한국어 풀이 |
| :--- | :--- | :--- | :--- | :--- |
| Cost function and cost surface | [PDF](handouts/cost-function.worksheet.en.pdf) | [PDF](handouts/cost-function.answers.en.pdf) | [PDF](handouts/cost-function.worksheet.ko.pdf) | [PDF](handouts/cost-function.answers.ko.pdf) |
| Implementing gradient descent | [PDF](handouts/gradient-descent.worksheet.en.pdf) | [PDF](handouts/gradient-descent.answers.en.pdf) | [PDF](handouts/gradient-descent.worksheet.ko.pdf) | [PDF](handouts/gradient-descent.answers.ko.pdf) |

Concept check: [English](handouts/concept-check.en.pdf) · [한국어](handouts/concept-check.ko.pdf). Ten multiple-choice questions, a pseudocode debugging exercise, and an open-response question.

The cost-surface worksheet uses eight input/target pairs. The gradient-descent worksheet uses five hand-calculated steps for each learning rate, in the order **divergence, very slow movement, convergence**, with one large `w, J(w)` graph for each case. Red answers show the intermediate calculations.

## Colab

| Notebook | Open |
| :--- | :--- |
| Four optional labs, student edition | [Open in Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/optional-labs.student.ipynb) |
| Four optional labs, answer edition | [Open in Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/optional-labs.answers.ipynb) |
| Cell-by-cell cost-function exploration | [Open in Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/cost-function.interactive.ko.ipynb) |

한국어 Optional Labs: [학생용](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/optional-labs.student.ko.ipynb) · [답안](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/optional-labs.answers.ko.ipynb)

English interactive cost lab: [Open in Colab](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-01/notebooks/cost-function.interactive.en.ipynb)

The optional labs and interactive cost lab have both English and Korean explanations. The interactive lab uses eight actual Auto MPG observations, comparing targets, predictions, and errors with different colors. Run its cells in order before using the sliders.

[English teaching notes](teaching-notes.en.md) · [한국어 강의 노트](teaching-notes.ko.md) · [LaTeX source and figure assets](source/) · [Dataset](data/auto-mpg.csv)

The earlier standalone HTML demonstration is archived in [English](demos/cost-function.legacy.en.html) and [한국어](demos/cost-function.legacy.ko.html). Use the cell-by-cell Colab for the classroom activity.
