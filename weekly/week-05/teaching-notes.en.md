# Course 1 / Week 3 / English speaker notes

English teaching script. Slide numbers refer to the shared classroom deck; source pages identify matching pages in the export.

## Slide 117 | W3 | Source page 1

This week, we will again use course materials from DeepLearning.AI and Stanford Online.  
Starting from models that predict numerical values, we will examine models that distinguish categories and then study overfitting.  

## Slide 118 | W3 | Source page 2

So far, we have predicted continuous numbers such as house prices.  
Now we will predict one of a few categories, such as whether an email is spam or a transaction is legitimate.  
First, we will see what problems arise if we use familiar linear regression directly.  
Understanding its limits will explain why we need the logistic regression model that follows.  

## Slide 119 | W3 | Source page 3

A problem with two possible answer categories, such as spam detection or fraud detection, is called binary classification.  
We usually label the categories 0 and 1 to make them convenient for computation.  
For example, we can assign 1 to spam and 0 to email that is not spam.  
In the tumor example, 1 indicates malignancy and 0 indicates no malignancy.  
Conventionally, 0 is called the negative class and 1 the positive class.  
Positive does not mean a desirable outcome; it means that the property we chose to mark is present.  
Spam or disease can be the positive class if that is what the task aims to detect.  
The numbers 0 and 1 are labels naming categories; at this point they do not represent probabilities.  
Our model needs to distinguish these two categories for new inputs.  

## Slide 120 | W3 | Source page 4

In the upper graph, the horizontal axis is tumor size and the vertical axis is the actual label.  
Nonmalignant examples appear at y=0, and malignant examples appear at y=1.  
Unlike the house-price graph, this vertical axis has only two possible correct answers.  
The lower diagram represents the same data on one line, using circles and crosses to distinguish the categories.  
The points sharing a vertical position in the lower diagram does not mean their answers are the same.  
Here the symbol shape communicates the category instead of vertical position.  
In either representation, the input is size and the answer to predict is its corresponding category.  
We now need a rule for choosing which label to predict for a new tumor size.  

## Slide 121 | W3 | Source page 5

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

## Slide 122 | W3 | Source page 6

We will now introduce logistic regression.  
Despite regression appearing in its name, its purpose here is binary classification.  
We attach a transformation after the existing w·x+b calculation, allowing the output to be interpreted as a probability between 0 and 1.  

## Slide 123 | W3 | Source page 7

The S-shaped curve on the right is the sigmoid function.  
Writing its input as z, we calculate its output as g(z)=1/(1+e^(−z)).  
For any real input z, its output lies between 0 and 1.  
A large positive z produces an output close to 1, while a large negative z produces one close to 0.  
At the center, z=0 gives e⁰=1, so the output is 1/2, or 0.5.  
Notice that it changes smoothly, rather than jumping abruptly from 0 to 1 like a step.  
The data plot on the left has tumor size x on its horizontal axis, while the sigmoid plot on the right has the transformed score z.  
Reading those two horizontal axes as identical can make the calculation confusing.  
The next slide connects the original input x to the score z that we put into this curve.  

## Slide 124 | W3 | Source page 8

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

## Slide 125 | W3 | Source page 9

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

## Slide 126 | W3 | Source page 10

The model outputs probabilities, but sometimes we need to choose either 0 or 1.  
Applying a threshold to the probability divides the input space into two regions.  
The boundary between those regions is the decision boundary.  

## Slide 127 | W3 | Source page 11

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

## Slide 128 | W3 | Source page 12

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

## Slide 129 | W3 | Source page 13

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

## Slide 130 | W3 | Source page 14

Adding squared terms or an interaction such as x₁x₂ allows a wider variety of boundaries.  
The upper annotations illustrate an ellipse, and the lower annotations illustrate a more complex closed boundary.  
The shape depends on the selected features and learned weights.  
The principle is still to collect inputs whose score entering sigmoid equals 0.  
Distinguish sigmoid's own S-shaped curve from the decision boundary in input space.  
Sigmoid converts one score to a probability, while a decision boundary identifies where a decision changes among multiple inputs.  
Using sigmoid therefore does not require the boundary in input space to be S-shaped.  
More varied features can represent more complex patterns, but greater complexity is not always better.  
We will first learn how to train the weights of such boundaries, then consider problems caused by overly complex models.  

## Slide 131 | W3 | Source page 15

So far, we have assumed w and b are given while examining predictions and boundaries.  
Now we need to choose good values of w and b from data.  
To do that, we must first define a cost function evaluating logistic-regression predictions.  

## Slide 132 | W3 | Source page 16

Each table row is a training example, whose inputs include features such as tumor size and age.  
The number of examples is m, and the number of features is n.  
Each row's correct answer y is 1 for malignancy and 0 otherwise.  
Using the current w and b, we can calculate a predicted probability f(x) between 0 and 1 for each input.  
We need a numerical evaluation of how well these predictions agree with the targets to compare parameter choices.  
We want high probabilities for examples with target 1 and low probabilities for examples with target 0.  
Simply counting correct labels, however, does not adequately represent gradual improvements in probability.  
For example, when the target is 1, increasing a prediction from 0.1 to 0.4 is meaningful even though both are below the threshold 0.5.  
We will construct a function that evaluates the probabilities themselves to reflect these changes too.  

## Slide 133 | W3 | Source page 17

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

## Slide 134 | W3 | Source page 18

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

## Slide 135 | W3 | Source page 19

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

## Slide 136 | W3 | Source page 20

Now select one of the two expressions according to the target.  
For y=1 calculate −log(p), and for y=0 calculate −log(1−p).  
Calculate this loss for each training example, add them all, and divide by m to obtain cost.  
The model adjusts w and b to give good probabilities on average across the examples.  
Standard logistic regression using this cost is a convex optimization problem for a fixed set of features.  
We obtain the kind of structure familiar from linear regression, where following descent directions can find a good solution.  
The two loss curves evaluate the probability of one example, while convexity here describes the overall cost as a function of parameters.  
Distinguishing the horizontal axes of these graphs reduces confusion.  
Next, we will combine the two target-dependent expressions into one.  

## Slide 137 | W3 | Source page 21

The loss is currently written in separate cases for y=1 and y=0.  
Using the fact that y is either 0 or 1, we can put both cases in one expression.  
It may look long at first, but substituting the target leaves only one term active.  

## Slide 138 | W3 | Source page 22

The combined loss is −y log(p)−(1−y)log(1−p).  
First substitute the target y=1.  
The first term is multiplied by 1, leaving −log(p).  
The second term is multiplied by 1−1=0, so it disappears.  
The complete expression therefore matches the loss previously defined for y=1.  
Think of y and 1−y as switches that turn the two terms on or off.  
When the target is 1, only the first switch is on.  
Here p is the current model's predicted probability, while y is the target already provided in the data.  
We are using the target to evaluate the prediction, rather than setting the two equal.  

## Slide 139 | W3 | Source page 23

This time, substitute y=0 into exactly the same expression.  
The first term is multiplied by 0 and disappears.  
The second term has 1−0=1, leaving −log(1−p).  
This case also exactly matches the loss previously defined for y=0.  
Changing the target changes which term evaluates the probability; it does not change the model that interprets the input as a probability.  
For example, if the model outputs p=0.8, target 1 gives −log(0.8), while target 0 gives −log(0.2).  
The second value is much larger, so predicting 0.8 for an example with target 0 receives a larger penalty.  
Combining both cases into one expression also makes array-based computation over the full dataset convenient.  

## Slide 140 | W3 | Source page 24

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

## Slide 141 | W3 | Source page 25

Gradient descent is also the basic training tool for logistic regression.  
Predict with the current parameters, calculate derivatives of the cost, and update in a direction that reduces cost.  
The model and cost expressions have changed, but the overall training sequence is the same.  

## Slide 142 | W3 | Source page 26

The model predicts f(x)=1/(1+e^(−(w·x+b))).  
The cost function is the average loss comparing those predicted probabilities with the targets.  
During training, we have both inputs and correct answers, so we can calculate how wrong the current model is.  
We use that information to repeatedly adjust w and b.  
After training, we use the same model equation to calculate a probability for a new input x.  
If needed, apply a threshold such as 0.5 to that probability to select a final label.  
Distinguish the probabilities used in training from the final 0-or-1 decisions shown to the user.  
Thresholding predicted probabilities into 0 and 1 before calculating gradient descent would change the calculation from training the cost we defined.  
During training, we will use the probability values directly.  

## Slide 143 | W3 | Source page 27

Differentiating the logistic-regression cost gives the update rule on the screen.  
For each weight wⱼ, the derivative is the average difference between predicted probability and target multiplied by its feature xⱼ.  
The derivative for b is the average difference between predicted probabilities and targets alone.  
That difference is negative when the target is 1 but the predicted probability is low, and positive when the target is 0 but the predicted probability is high.  
Using derivatives calculated with the inputs, we move the parameters in a direction that reduces average loss.  
For each update, multiply every derivative by learning rate α and subtract the result from its current parameter.  
Calculate all derivatives first using the same current w and b.  
Then update all parameters, following the same simultaneous-update principle as before.  
The value substituted for f(x) is the probability from sigmoid, rather than a label thresholded to 0 or 1.  
An advantage of this model is that differentiating a cost containing logarithms and sigmoid still produces a relatively simple expression.  

## Slide 144 | W3 | Source page 28

The update rule looks very similar to the one for linear regression.  
However, f(x) means something different, so the two procedures do not train the same model.  
Linear regression uses f(x)=w·x+b, while logistic regression applies sigmoid to that value.  
The two models also use different cost functions for evaluation.  
When adapting code, check that you have changed the prediction function too, rather than only looking at the update expression.  
We can also use vectorization to organize calculations as arrays and feature scaling to adjust input sizes.  
Choose a learning rate and check whether cost decreases steadily over iterations.  
The prediction function, cost, and gradient descent are now connected into one training process.  
Next, we will see why a model that fits training data well can fail on new data.  

## Slide 145 | W3 | Source page 29

Getting correct answers on training data and making good predictions on unseen data are different achievements.  
Think of a student who memorizes practice answers versus one who understands the method.  
We will examine overfitting, where a model follows the training data too closely, and underfitting, where it fails to learn enough.  

## Slide 146 | W3 | Source page 30

The three diagrams fit the same house-price data using models of different complexity.  
The straight line on the left does not adequately follow the curved relationship in the data.  
When a model is too simple even to express important patterns in its training data, we call it underfitting.  
This problem is also called high bias.  
The quadratic curve in the middle does not pass through every point exactly, but follows the overall trend well.  
The higher-degree curve on the right passes through the training points very precisely.  
However, its unnecessary bends between points can lead to strange predictions for new houses.  
Following even the sample's incidental fluctuations in this way is overfitting.  
It is also called high variance because a small change in the training data can cause a large change in the fitted model.  
Like the Goldilocks story in which porridge should be neither too hot nor too cold, we want enough complexity to capture the needed pattern.  
We should not select the right-hand model merely because its training cost is the smallest.  
Our ultimate objective also includes good predictions on data the model has not seen.  

## Slide 147 | W3 | Source page 31

The same problem appears in classification.  
The straight boundary on the left does not adequately separate a category arranged in a rounded pattern.  
The middle boundary follows the overall distribution and separates the categories reasonably naturally.  
The right-hand boundary bends in many places to classify individual points.  
This can leave almost no mistakes on the training examples.  
However, a new point may fall into the wrong category because of a small bend created by chance.  
In regression, the curve fluctuated excessively; in classification, the boundary became excessively complicated.  
A smooth-looking diagram alone does not establish that a model is good.  
In practice, check how well it predicts data that was not used for training.  
These diagrams illustrate why perfectly matching training answers is an insufficient objective by itself.  

## Slide 148 | W3 | Source page 32

How can we reduce overfitting when a model shows it?  
We will examine three approaches: collect more data, use fewer features, and apply regularization.  
Compare what information each approach adds or what freedom it removes from the model.  

## Slide 149 | W3 | Source page 33

The first approach is to collect more training data.  
With only a few examples, it is easy to construct a complicated curve through every point.  
When new data appears in varied positions, the arbitrary bends between earlier points also have to be evaluated.  
A model following the overall relationship can then be favored over one that happens to fit just a few examples.  
It is like showing a wider range of exercises to a student who memorized the answers to only a few practice questions.  
We need examples containing new information, rather than simply copying existing data to increase the count.  
Of course, collecting more data can require substantial time or money.  
If the model is itself too simple and underfits, more data alone does not fix its lack of expressive capacity.  
Here we are considering additional data as a way to reduce overfitting by a model that is too complex relative to the available examples.  

## Slide 150 | W3 | Source page 34

The second approach reduces the number of features used.  
Suppose house-price prediction includes many inputs besides size, room count, and age.  
More features let the model express varied relationships, but also give it more freedom to follow chance differences in a small dataset.  
We can therefore consider retaining only a useful subset of the features.  
For example, we might select a few important inputs, such as size, room count, and age, from hundreds of candidates.  
Fewer adjustment controls reduce the model's freedom to fit the data excessively.  
However, it is not always easy to know in advance which information is necessary or unnecessary.  
Removing the wrong features can discard useful predictive information and worsen performance.  
We therefore also need an approach that limits excessive complexity without deleting features.  

## Slide 151 | W3 | Source page 35

The third approach is regularization.  
It retains features but attaches a cost to unnecessarily large weights.  
It is like limiting excessive volume for individual instruments instead of removing every instrument's sound.  
The model can still use a needed feature, but a large effect must justify itself with enough improvement in prediction.  
In polynomial regression, making higher-degree weights smaller can reduce excessive bending of the curve.  
Making weights smaller does not mean fixing every weight to exactly 0.  
The L2 regularization we will study encourages smaller values, while retaining weights needed by the data.  
Because input units also affect weight magnitudes, consider regularization together with feature scaling.  
We will now define a cost that evaluates both prediction errors and weight magnitudes.  

## Slide 152 | W3 | Source page 36

Let us compare what each of the three approaches changes.  
Collecting more data gives the model more evidence to learn from.  
Reducing features simplifies the representation by removing some information the model uses.  
Regularization retains the information but changes the training criterion to discourage excessively large weights.  
If additional data is easy to obtain, the first approach may help.  
If unnecessary features are clearly identifiable, removing them can help.  
Regularization is especially useful when we want to retain many features.  
These approaches are not mutually exclusive and can be combined when appropriate.  
Next, we will see exactly how regularization enters the equations and gradient descent.  

## Slide 153 | W3 | Source page 37

To apply regularization, add a term evaluating weight magnitudes to the original cost.  
We then consider both fitting the data and avoiding excessive model complexity.  
We will begin with a simple example that shrinks only two higher-degree terms.  

## Slide 154 | W3 | Source page 38

The quadratic model on the left follows the overall pattern well, while the fourth-degree model on the right bends considerably between examples.  
What would happen if we made the right-hand model's weights w₃ and w₄ on x³ and x⁴ small?  
Those terms would have less influence, potentially making the model closer to a quadratic.  
An example of encoding that idea is to add 1000w₃²+1000w₄² to the existing J.  
If w₃ or w₄ becomes large, it adds a large extra cost even if predictions on the data improve.  
For example, w₃=1 adds 1000 from that term alone, while w₃=0.1 adds 10.  
Training to reduce total cost therefore applies pressure to keep both weights small.  
Squaring penalizes large negative values as well as large positive values.  
The value 1000 illustrates the effect; it is not a constant to use unchanged for every problem.  
Instead of manually deleting weights by setting them to 0 first, we train while considering both predictive improvement and the extra cost.  

## Slide 155 | W3 | Source page 39

In real problems, we usually do not know in advance which weights to shrink, so we typically penalize the sum of all squared weights.  
The new cost's first term is the original prediction-error cost, while the second is λ/(2m) times the sum of wⱼ².  
The first summation index i visits training examples, and the second index j visits weights.  
With m examples and n features, the sums therefore end at m and n, respectively.  
The nonnegative value λ controls the strength of regularization.  
A larger λ assigns a greater penalty to large weights.  
The value λ sets the balance within the training objective, while learning rate α sets the movement toward that objective; they have different roles.  
The annotation says b may be included or excluded, but the calculations that follow penalize only the weights.  
The bias b shifts the curve's overall height; here we focus on controlling complexity created by the weights rather than that height itself.  
Thus b affects J(w,b), but the regularization sum does not contain b².  
To obtain a small total cost, the model must fit the data without unnecessarily large weights.  

## Slide 156 | W3 | Source page 40

When λ=0, the regularization term disappears and we recover the original cost.  
If the model is sufficiently complex and data is limited, overfitting may produce a curve like the one in the annotations.  
However, not every model with λ=0 necessarily overfits.  
Conversely, making λ extremely large, such as ten billion, adds a very large cost even for modest weights.  
Training then tries to make the weights almost 0 to avoid that cost.  
As the right-hand expression shows, f(x) becomes nearly the constant b and may miss important patterns.  
This is underfitting caused by excessively strong regularization.  
We want a suitable balance between fitting the data and suppressing weight magnitudes.  
When selecting λ, it is important to check predictive performance on data not used for training.  
Different λ values also change the penalty included in the objective, so do not choose between them by simply comparing total cost numbers.  

## Slide 157 | W3 | Source page 41

Now we will train regularized linear regression using gradient descent.  
Since we added a term to the cost, its derivative must also enter the update rule.  
We will examine what is added to the earlier calculation, one part at a time.  

## Slide 158 | W3 | Source page 42

The new derivative for weight wⱼ has two parts.  
The first is the usual average of prediction errors multiplied by the feature.  
The second is (λ/m)wⱼ, coming from regularization.  
Because the overall cost is a sum of two terms, its derivative is also the sum of their derivatives.  
Gradient descent multiplies this sum by α and subtracts it from the current weight.  
If wⱼ is positive, the extra derivative is positive, so subtracting it moves the weight toward 0.  
If wⱼ is negative, the extra derivative is negative, so subtracting it again moves the weight toward 0.  
It therefore discourages large weights regardless of their sign.  
Because regularization was not applied to b, its derivative expression stays the same.  
One update combines the change requested by the data with a change pulling the weights toward 0.  

## Slide 159 | W3 | Source page 43

In code, first use the current model to predict every training example.  
Calculate each weight's original derivative from prediction errors and add (λ/m)w.  
Multiply the full result by learning rate α and subtract it from the current w.  
The learning rate α applies to both the data-derived and regularization-derived parts.  
Check the expression so that you do not multiply by λ while forgetting to divide by m when adding the new term.  
Update b using the mean prediction error without adding the same regularization term.  
Also calculate all derivatives using parameters from before the update.  
The rule against mixing an already-updated weight into another derivative still applies.  
We have added one term per weight to the existing gradient descent, so we do not need to rebuild the entire training loop.  

## Slide 160 | W3 | Source page 44

This expression rearranges the previous update rule into another form.  
Collecting the part that subtracts α(λ/m)wⱼ from wⱼ gives wⱼ(1−αλ/m).  
Subtracting the data-error update afterward produces the original expression.  
For example, with α=0.01, λ=1, and m=50, the parenthesized factor is 0.9998.  
If the current weight is 10, applying this part alone gives 9.998.  
If it is −10, the result is −9.998, which also slightly reduces its magnitude.  
This calculation explains why regularization is described as gradually shrinking weights.  
However, the update for fitting the data is still applied afterward.  
If the data strongly calls for a larger particular weight, the final weight may increase instead.  
Understand this as an added force toward smaller magnitudes, rather than a guarantee that every final update makes a weight smaller.  

## Slide 161 | W3 | Source page 45

We will check why the added derivative is (λ/m)wⱼ.  
The regularization term is λ/(2m) multiplied by the sum of all squared weights.  
When differentiating with respect to wⱼ, only wⱼ² varies with that variable; the other squared weights are treated as constants.  
The derivative of wⱼ² is 2wⱼ, so the 2 cancels the preceding factor 1/2.  
The result is (λ/m)wⱼ.  
Because b is absent from that sum, differentiating with respect to b adds 0.  
The data-error term sums over m examples, but this term evaluates the list of weights.  
There is no need to add the same regularization cost again for every example and multiply it by m.  
If derivatives are still unfamiliar, first remember the connection that differentiating a square produces 2, which cancels the preceding 1/2.  
This slide checks that the expression follows from differentiating the cost, rather than being chosen arbitrarily.  

## Slide 162 | W3 | Source page 46

The same regularization idea can be applied to logistic regression.  
Add the sum of squared weights to the classification cost we used earlier.  
This encourages accurate predicted probabilities while discouraging a decision boundary from following every small fluctuation in the data.  

## Slide 163 | W3 | Source page 47

The complex boundary bends in many places to distinguish the training examples precisely.  
The simpler boundary overlaid on the same plot may work better for new data.  
To encourage this, add λ/(2m)×Σwⱼ² to logistic regression's average loss.  
The first term encourages high probability for the correct answer, while the second discourages large weights.  
This is the same sum-of-squares regularization used in linear regression.  
What differs is the sigmoid prediction function and binary-cross-entropy loss evaluating those predictions.  
It can also reduce excessively large weights when many polynomial features are used.  
However, an excessively large λ can prevent the model from representing a necessary boundary, so balance is needed.  
Check whether the model actually improves on data not used for training, rather than judging only the boundary's appearance.  

## Slide 164 | W3 | Source page 48

The final update rule combines the two calculations we have learned.  
For each wⱼ, update using the average probability-minus-target difference multiplied by its feature, plus (λ/m)wⱼ.  
For b, update using only the average difference between predicted probabilities and targets.  
Here f(x) must be the probability obtained after sigmoid, rather than linear regression's straight-line output.  
The rule that all parameter updates are calculated from the same current state still applies.  
We have now learned the complete sequence: represent inputs as numbers, predict with a model, evaluate with loss, and adjust parameters using gradient descent.  
Regularization is a mechanism within that sequence for reducing excessive fitting to the training data.  
When we study neural networks and Transformers, the structure calculating predictions will become much more complex.  
But the basic learning structure continues: compare predictions with targets to form a loss, then update parameters using derivatives.  
When you encounter the next model, again begin by identifying its inputs, predictions, loss, and trainable parameters.
