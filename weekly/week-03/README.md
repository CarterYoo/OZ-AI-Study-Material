# Week 03 / Sigmoid and logistic regression

Compare a linear model with a probability model. Calculate sigmoid values, plot predictions, find a decision boundary, and compare how two different losses shape the cost.

| Language | Student PDF | Worked answers |
| :--- | :--- | :--- |
| English | [Worksheet](handouts/sigmoid-logistic.worksheet.en.pdf) | [Answer key](handouts/sigmoid-logistic.answers.en.pdf) |
| 한국어 | [문제](handouts/sigmoid-logistic.worksheet.ko.pdf) | [풀이](handouts/sigmoid-logistic.answers.ko.pdf) |

Concept check: [English](handouts/concept-check.en.pdf) · [한국어](handouts/concept-check.ko.pdf). Ten multiple-choice questions, a pseudocode debugging exercise, and an open-response question.

The nine-page worksheet has 28 questions. Its seven-point synthetic dataset has irregular input spacing and a boundary-near exception. Actual targets stay binary; model predictions are plotted separately. Both editions use the same data and calculations.

The sequence covers the limits of linear-regression outputs, sigmoid probabilities, a straight decision boundary, sigmoid with MSE, and logistic loss with a convex parameter cost. Nonlinear decision boundaries are outside this worksheet's scope.

## Colab

[Student notebook](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.student.ipynb) · [Answer notebook](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.answers.ipynb)

한국어 Colab: [학생용](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.student.ko.ipynb) · [답안](https://colab.research.google.com/github/CarterYoo/OZ-AI-Study-Material/blob/main/weekly/week-03/notebooks/optional-labs.answers.ko.ipynb)

The nine optional labs also cover logistic gradient descent, scikit-learn, overfitting, and regularization. They extend beyond the hand-calculation worksheet. English and Korean notebooks use the same executable code.

[English teaching notes](teaching-notes.en.md) · [한국어 강의 노트](teaching-notes.ko.md) · [Editable LaTeX sources](source/) · [Arithmetic reference](data/calculation-checks.json)
