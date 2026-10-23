# Week 05 / Feature Engineering and Classification

English teaching notes matched to the OZ classroom slide order.
The explanations are instructional adaptations, not verbatim lecture transcripts.

## Canva page 108 / ML source slide 100 / Feature Engineering

So far, we have used the given features directly.
Combining the original inputs into new features can let a model express more useful relationships.
This is called feature engineering: designing which numbers to show the model.

Source slide 100: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p117
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 109 / ML source slide 101 / Creating Area from Width and Depth

In this example, the inputs are a plot of land's frontage width and depth.
Initially, we can predict its price by weighting width x₁ and depth x₂ separately.
However, even at a fixed depth, the area added by a change in width depends on the land's dimensions.
Simply adding separate effects for width and depth may not represent this relationship adequately.
Creating the new feature x₃=x₁×x₂ lets us provide the land's area as an input.
We calculate area from two inputs we already have, rather than obtaining it from the target price.
The model can use width, depth, and area together and learn their respective weights.
A person proposes that an area representation might help, while the data determines how strongly it contributes.
Adding a feature does not guarantee better predictions, so actual performance must also be checked.
The key is that, even with the same raw data, the numerical representation can change which relationships are easy for the model to learn.

Source slide 101: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p118
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 110 / ML source slide 102 / Polynomial Regression

Feature engineering can let linear regression represent curved relationships too.
One approach makes x² or x³ into additional features alongside x itself.
A model using these polynomial terms is called polynomial regression.

Source slide 102: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p119
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 111 / ML source slide 103 / Using Powers of x as Features

Suppose a single straight line does not fit the relationship between house size and price well.
Adding x² lets us construct a curve such as f(x)=w₁x+w₂x²+b.
The quadratic curve on the slide turns downward beyond a certain point, which may not match the relationship we expect.
Adding x³ allows a wider variety of curve shapes.
We calculate x² and x³ as separate features and provide them to the model.
The name linear regression applies because the weights multiply features and are added linearly, rather than being multiplied together or squared themselves.
Thus, even if the model is curved with respect to input x, we can use the weight-update method we have learned.
If size x is 1000, x² is one million and x³ is one billion, making the scale differences even larger.
Feature scaling becomes especially important when we create these inputs.
Adding more terms does not always produce a better model; next week we will study the problem of excessive complexity.

Source slide 103: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p120
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 112 / ML source slide 104 / Feature Choices Shape the Curve

A new feature does not have to be a square or a cube.
For example, √x can help express a relationship whose increase becomes smaller as x grows.
The function √x keeps increasing, but its curve becomes progressively gentler.
However, the final prediction also depends on the other terms and their weights, so adding √x does not force the whole model to have that same shape.
Choose suitable representations using both your understanding of the problem and evaluation on actual data.
This week's methods connect to representing inputs well and learning weights while reducing cost steadily.
Inputs may be multiple values or transformed features, but the basic training sequence remains the same.
Next, we will move from predicting continuous quantities such as house prices to classification: predicting membership in a category.

Source slide 104: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p121
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 113 / ML source slide 106 / Why Classification Needs a New Model

So far, we have predicted continuous numbers such as house prices.
Now we will predict one of a few categories, such as whether an email is spam or a transaction is legitimate.
First, we will see what problems arise if we use familiar linear regression directly.
Understanding its limits will explain why we need the logistic regression model that follows.

Source slide 106: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p123
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 114 / ML source slide 107 / Two Labels for Two Classes

A problem with two possible answer categories, such as spam detection or fraud detection, is called binary classification.
We usually label the categories 0 and 1 to make them convenient for computation.
For example, we can assign 1 to spam and 0 to email that is not spam.
In the tumor example, 1 indicates malignancy and 0 indicates no malignancy.
Conventionally, 0 is called the negative class and 1 the positive class.
Positive does not mean a desirable outcome; it means that the property we chose to mark is present.
Spam or disease can be the positive class if that is what the task aims to detect.
The numbers 0 and 1 are labels naming categories; at this point they do not represent probabilities.
Our model needs to distinguish these two categories for new inputs.

Source slide 107: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p124
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 115 / ML source slide 108 / Two Views of the Same Class Labels

In the upper graph, the horizontal axis is tumor size and the vertical axis is the actual label.
Nonmalignant examples appear at y=0, and malignant examples appear at y=1.
Unlike the house-price graph, this vertical axis has only two possible correct answers.
The lower diagram represents the same data on one line, using circles and crosses to distinguish the categories.
The points sharing a vertical position in the lower diagram does not mean their answers are the same.
Here the symbol shape communicates the category instead of vertical position.
In either representation, the input is size and the answer to predict is its corresponding category.
We now need a rule for choosing which label to predict for a new tumor size.

Source slide 108: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p125
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 116 / ML source slide 109 / Limits of a Line and a Threshold

At first, we might think we can fit a straight line to this data too.
Suppose we predict 1 when the line's output is at least 0.5, and 0 when it is smaller.
The position where the line passes through height 0.5 then becomes the threshold separating the categories.
In the initial diagram, this rule appears to separate the data reasonably well.
What happens if we add one malignant example far to the right?
Linear regression tries to reduce squared errors including that new point, changing the line's slope and position.
The position where it reaches 0.5 also moves, potentially misclassifying points that were previously classified correctly.
The new example is simply farther to the right than existing malignant cases, yet it shifts a previously useful boundary.
The line can also output values below 0 or above 1, which makes those values difficult to interpret directly as probabilities.
We will therefore use an output form and training criterion suited to classification.

Source slide 109: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p126
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 117 / ML source slide 110 / Logistic Regression

We will now introduce logistic regression.
Despite regression appearing in its name, its purpose here is binary classification.
We attach a transformation after the existing w·x+b calculation, allowing the output to be interpreted as a probability between 0 and 1.

Source slide 110: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p127
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 118 / ML source slide 111 / The Sigmoid Function

The S-shaped curve on the right is the sigmoid function.
Writing its input as z, we calculate its output as g(z)=1/(1+e^(−z)).
For any real input z, its output lies between 0 and 1.
A large positive z produces an output close to 1, while a large negative z produces one close to 0.
At the center, z=0 gives e⁰=1, so the output is 1/2, or 0.5.
Notice that it changes smoothly, rather than jumping abruptly from 0 to 1 like a step.
The data plot on the left has tumor size x on its horizontal axis, while the sigmoid plot on the right has the transformed score z.
Reading those two horizontal axes as identical can make the calculation confusing.
The next slide connects the original input x to the score z that we put into this curve.

Source slide 111: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p128
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 119 / ML source slide 112 / From a Linear Score to a Probability

Logistic regression is easier to understand as two calculation steps.
First, combine the inputs into one score z=w·x+b.
This step is the same calculation we used in linear regression.
Then put the score z into sigmoid to calculate f(x)=g(z).
For example, if the first calculation returns 0, the final output is 0.5.
A score of 2 gives an output of about 0.88, while −2 gives about 0.12.
The structure assigns a higher probability to y=1 as the score increases.
In the equation, e is a mathematical constant of about 2.718, and the exponent contains the negative of the entire score z.
When writing code, carefully check the scope of the parentheses in −(w·x+b).
Changing w and b now changes the score and therefore changes the predicted probability.
We still learn w and b; we do not choose a new sigmoid formula on each iteration.

Source slide 112: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p129
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 120 / ML source slide 113 / Interpreting Predicted Probabilities

Suppose the model outputs 0.7 for a particular input.
This means the current model predicts a 70% probability that this input has label 1.
It does not mean the actual label is 0.7; the actual answer is still 0 or 1.
Nor does it mean an accuracy of 70% over the entire dataset.
We are looking at a predicted probability for one particular input.
Because there are only two categories, the probability of y=0 is 1−0.7=0.3.
The notation P(y=1|x;w,b) on the right means the probability of y=1 calculated using the current w and b, given input x.
The x after the vertical bar identifies the input we are conditioning on.
A high probability means the model considers that category more likely; we have not yet selected a final label of 0 or 1.
We will add that selection rule next.

Source slide 113: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p130
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 121 / ML source slide 114 / Decision Boundaries

The model outputs probabilities, but sometimes we need to choose either 0 or 1.
Applying a threshold to the probability divides the input space into two regions.
The boundary between those regions is the decision boundary.

Source slide 114: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p131
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 122 / ML source slide 115 / Why Probability 0.5 Means Score 0

Here, we will predict 1 when the probability is at least 0.5 and 0 when it is below 0.5.
Sigmoid passes through exactly 0.5 at z=0, and its output increases as z increases.
Checking whether the probability is at least 0.5 is therefore equivalent to checking whether z is at least 0.
Since z=w·x+b, we predict 1 in the region where w·x+b≥0.
Conversely, we predict 0 where that value is negative.
The boundary where the decision changes is w·x+b=0.
Applying this rule to the slide's probabilities 0.7 and 0.3 gives final predictions 1 and 0, respectively.
Distinguish calculating a probability from applying a threshold to that probability to choose a label.
We use 0.5 here, but other thresholds can be chosen for different purposes.
The next diagrams show boundaries for a threshold of 0.5.

Source slide 115: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p132
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 123 / ML source slide 116 / A Straight Decision Boundary

This example has two inputs, x₁ and x₂, both with weight 1, and b=−3.
The score entering sigmoid is therefore z=x₁+x₂−3.
The decision boundary has z=0, giving the straight line x₁+x₂=3.
When x₁=0, x₂=3, and when x₂=0, x₁=3, so we can draw the line through those two intercepts.
For example, input (2,2) gives a positive score z=1, so we predict 1.
Input (1,1) gives a negative score z=−1, so we predict 0.
On the line, the probability is exactly 0.5, which our at-least rule classifies as 1.
The axes in this diagram are inputs x₁ and x₂, rather than parameters w₁ and w₂.
It shows which inputs the current model assigns to each category, rather than a cost graph comparing parameter quality.
Changing w and b also changes the slope or position of this boundary.

Source slide 116: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p133
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 124 / ML source slide 117 / A Circular Decision Boundary

A decision boundary does not always have to be a straight line.
As we learned earlier, try using x₁² and x₂² as new features.
Giving both weight 1 and setting b=−1 produces z=x₁²+x₂²−1.
On the boundary z=0, so x₁²+x₂²=1.
This is a circle centered at the origin with radius 1.
Inside the circle, the sum of the squares is below 1, making z negative, so we predict 0.
Outside the circle, z is positive, so we predict 1.
For example, (0,0) is inside and predicts 0, while (2,0) is outside and predicts 1.
The sigmoid formula is unchanged, but changing the features calculated before it has produced a circular boundary.
This is where feature engineering connects to classification.

Source slide 117: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p134
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 125 / ML source slide 118 / More Flexible Decision Boundaries

Adding squared terms or an interaction such as x₁x₂ allows a wider variety of boundaries.
The upper annotations illustrate an ellipse, and the lower annotations illustrate a more complex closed boundary.
The shape depends on the selected features and learned weights.
The principle is still to collect inputs whose score entering sigmoid equals 0.
Distinguish sigmoid's own S-shaped curve from the decision boundary in input space.
Sigmoid converts one score to a probability, while a decision boundary identifies where a decision changes among multiple inputs.
Using sigmoid therefore does not require the boundary in input space to be S-shaped.
More varied features can represent more complex patterns, but greater complexity is not always better.
We will first learn how to train the weights of such boundaries, then consider problems caused by overly complex models.

Source slide 118: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p135
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 126 / ML source slide 119 / Cost for Logistic Regression

So far, we have assumed w and b are given while examining predictions and boundaries.
Now we need to choose good values of w and b from data.
To do that, we must first define a cost function evaluating logistic-regression predictions.

Source slide 119: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p136
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 127 / ML source slide 120 / Reading the Classification Dataset

Each table row is a training example, whose inputs include features such as tumor size and age.
The number of examples is m, and the number of features is n.
Each row's correct answer y is 1 for malignancy and 0 otherwise.
Using the current w and b, we can calculate a predicted probability f(x) between 0 and 1 for each input.
We need a numerical evaluation of how well these predictions agree with the targets to compare parameter choices.
We want high probabilities for examples with target 1 and low probabilities for examples with target 0.
Simply counting correct labels, however, does not adequately represent gradual improvements in probability.
For example, when the target is 1, increasing a prediction from 0.1 to 0.4 is meaningful even though both are below the threshold 0.5.
We will construct a function that evaluates the probabilities themselves to reflect these changes too.

Source slide 120: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p137
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 128 / ML source slide 121 / Why Squared Error Is Harder Here

We might first consider applying the same MSE form used in linear regression.
It is possible to calculate the squared difference between a predicted probability and the target.
However, once sigmoid is inside the prediction function, the cost is no longer guaranteed to be a simple bowl in its parameters.
It can be nonconvex with several bends, as illustrated on the right.
That can make finding a good position with gradient descent more difficult.
We will therefore use another function suited to logistic regression.
First, we define a loss evaluating the prediction for one example.
The cost J is the average of those losses over the entire training dataset.
Distinguishing loss from cost makes it easier to see whether an expression evaluates one example or all of them.
We will begin with the case where the correct answer is 1.

Source slide 121: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p138
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 129 / ML source slide 122 / Logistic Loss When y Is 1

If the target is y=1, a model probability p closer to 1 is better.
For this case, define the loss as −log(p).
The horizontal axis is the model's predicted probability, rather than tumor size.
As p approaches 1, log(p) approaches 0, and the loss becomes small.
Conversely, as p approaches 0, the loss becomes very large.
The actual answer is 1, but the model assigns almost no probability to 1, so we give it a large penalty.
Here log is the natural logarithm; for example, p=0.9 gives a loss of about 0.105.
At p=0.5 it is about 0.693, and at p=0.1 it rises to about 2.303.
All three predictions are evaluated against target 1, but stronger confidence in the wrong direction receives a larger penalty.
This curve is the first case, applying only to examples whose target is 1.

Source slide 122: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p139
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 130 / ML source slide 123 / Logistic Loss When y Is 0

Now consider an example whose target is y=0.
Here, a predicted probability p of y=1 closer to 0 is better.
We therefore define its loss as −log(1−p).
When p is near 0, 1−p is near 1 and the loss is small.
When p is near 1, 1−p is near 0 and the loss is very large.
This shape gives a large penalty for confidently predicting 1 when the correct answer is 0.
For example, p=0.1 gives a loss of about 0.105, while p=0.9 gives about 2.303.
The direction of a good prediction has reversed compared with the previous y=1 case.
The same probability 0.9 is good when the target is 1 and bad when it is 0.
We therefore need both the predicted probability and actual label when calculating loss.

Source slide 123: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p140
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 131 / ML source slide 124 / From Individual Loss to Average Cost

Now select one of the two expressions according to the target.
For y=1 calculate −log(p), and for y=0 calculate −log(1−p).
Calculate this loss for each training example, add them all, and divide by m to obtain cost.
The model adjusts w and b to give good probabilities on average across the examples.
Standard logistic regression using this cost is a convex optimization problem for a fixed set of features.
We obtain the kind of structure familiar from linear regression, where following descent directions can find a good solution.
The two loss curves evaluate the probability of one example, while convexity here describes the overall cost as a function of parameters.
Distinguishing the horizontal axes of these graphs reduces confusion.
Next, we will combine the two target-dependent expressions into one.

Source slide 124: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p141
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 132 / ML source slide 125 / A Single Formula for Logistic Cost

The loss is currently written in separate cases for y=1 and y=0.
Using the fact that y is either 0 or 1, we can put both cases in one expression.
It may look long at first, but substituting the target leaves only one term active.

Source slide 125: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p142
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 133 / ML source slide 126 / The Combined Loss When y Is 1

The combined loss is −y log(p)−(1−y)log(1−p).
First substitute the target y=1.
The first term is multiplied by 1, leaving −log(p).
The second term is multiplied by 1−1=0, so it disappears.
The complete expression therefore matches the loss previously defined for y=1.
Think of y and 1−y as switches that turn the two terms on or off.
When the target is 1, only the first switch is on.
Here p is the current model's predicted probability, while y is the target already provided in the data.
We are using the target to evaluate the prediction, rather than setting the two equal.

Source slide 126: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p143
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 134 / ML source slide 127 / The Combined Loss When y Is 0

This time, substitute y=0 into exactly the same expression.
The first term is multiplied by 0 and disappears.
The second term has 1−0=1, leaving −log(1−p).
This case also exactly matches the loss previously defined for y=0.
Changing the target changes which term evaluates the probability; it does not change the model that interprets the input as a probability.
For example, if the model outputs p=0.8, target 1 gives −log(0.8), while target 0 gives −log(0.2).
The second value is much larger, so predicting 0.8 for an example with target 0 receives a larger penalty.
Combining both cases into one expression also makes array-based computation over the full dataset convenient.

Source slide 127: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p144
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 135 / ML source slide 128 / The Logistic Regression Cost

Cost is the average obtained by applying the new loss to every example.
The summation index i means to examine examples from the first through the mth.
For each example, substitute its own probability f(x⁽ⁱ⁾) and its own target y⁽ⁱ⁾ into the same expression.
The formula is therefore −1/m multiplied by the sum of y log(p)+(1−y)log(1−p).
We do not include the factor 1/2 used in the linear-regression cost here.
This loss is also called binary cross entropy.
Intuitively, it trains the model to give high probability to the answer actually observed.
The expression combines two requirements: raise p for target 1, and raise 1−p for target 0.
We must reduce average loss over all the data with shared w and b, rather than only fitting the probability of one example.
Now that the objective is defined, we will update the parameters with gradient descent.

Source slide 128: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p145
Course: Andrew Ng, DeepLearning.AI, Stanford Online
