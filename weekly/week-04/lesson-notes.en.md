# Week 04 / Multiple Features and Feature Scaling

English teaching notes matched to the OZ classroom slide order.
The explanations are instructional adaptations, not verbatim lecture transcripts.

## Canva page 74 / ML source slide 66 / Gradient Descent for Linear Regression

So far, we have examined the model, cost, and gradient descent separately.
Now we will differentiate the linear-regression cost and substitute the result into the update rule.
Connecting these three parts lets us provide data and train a model.

Source slide 66: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p70
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 75 / ML source slide 67 / Predict, Measure, and Update

First, use f(x)=wx+b to calculate a prediction for each example.
Subtract the actual y from each prediction to obtain that example's error.
The derivative with respect to w is the average of each error multiplied by that example's x.
The derivative with respect to b is the average of the errors themselves.
Use the prediction equation to consider why only the w derivative includes x.
If w changes by 0.1, the prediction at x=1 changes by 0.1, while the prediction at x=10 changes by 1.
The influence of w therefore depends on input x.
By contrast, changing b by 0.1 changes every prediction by exactly 0.1.
That is why the parameter sensitivities multiply w's error term by x and b's error term by 1.
One training step multiplies these derivatives by the learning rate and subtracts the results from the old values.

Source slide 67: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p71
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 76 / ML source slide 68 / Where the Derivatives Come From

This slide is an optional explanation of how the derivative expressions are obtained.
Temporarily write one example's error in the shorter form e=wx+b−y.
Differentiating e² gives 2e multiplied by the derivative of the expression inside e.
With respect to w, the derivative of wx+b−y is x.
Each example therefore contributes 2(wx+b−y)x.
The 2 cancels the 2 in the factor 1/(2m), leaving (1/m)Σ(wx+b−y)x.
With respect to b, the inner derivative is 1, so the final x is absent.
The result is (1/m)Σ(wx+b−y).
The reason we included 1/2 in the cost was to simplify the expression here.
If differentiation is unfamiliar, you can first understand the calculation procedure: the average of error×x for w, and the average error for b.

Source slide 68: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p72
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 77 / ML source slide 69 / The Linear Regression Update Rule

We will perform one update using the earlier examples (1,1), (2,2), and (3,3).
Starting with w=0 and b=0 makes every prediction 0, giving errors −1, −2, and −3.
The derivative for w is (−1×1−2×2−3×3)/3=−14/3.
The derivative for b is (−1−2−3)/3=−2.
With α=0.1, the new w is 0−0.1×(−14/3), or about 0.467.
The new b is 0−0.1×(−2)=0.2.
Check that both values were calculated from the errors before the update.
Now recalculate the predictions with the new model f(x)≈0.467x+0.2.
Recalculate the derivatives from the new errors and repeat the procedure.
Reusing the first derivative forever would not move according to the direction at the current position.

Source slide 69: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p73
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 78 / ML source slide 70 / More than One Local Minimum

A general cost function may have several valleys, as in the diagram.
Because gradient descent uses the slope around its current position, different starting points can lead to different destinations.
Entering one valley does not guarantee that it is better than every other candidate.
That is why we distinguished a local minimum from a global minimum.
Should we worry about the same problem in the linear regression model we just built?
The answer depends on the cost used with the model, rather than only on the model's name.

Source slide 70: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p74
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 79 / ML source slide 71 / A Convex Cost and Its Global Minimum

Combining linear regression with the current MSE-based cost gives a function that is convex in its parameters.
Think of a bowl that curves downward into its center, as in the diagram.
The important property is that it does not have separate, worse local minima to get trapped in.
With an appropriate learning rate, we can approach a global minimum.
Depending on the data, the minimum cost may be 0 or positive.
Successful training means finding good values within the chosen model and cost function.
It does not mean that every real relationship is a straight line, or that the model will predict new data perfectly.
We will return to that distinction when evaluating model performance later.

Source slide 71: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p75
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 80 / ML source slide 72 / Running Gradient Descent

Now we will follow training on the house-price data.
The left-hand plot shows the prediction line, while the upper-right and lower plots show two representations of the same cost.
Watch the new line and point added on each slide to see what one update changes.
Earlier lines remain as traces that let us compare previous states.

Source slide 72: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p76
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 81 / ML source slide 73 / Starting with a Poor Fit

To make the changes visible, this example starts at w=−0.1 and b=900.
We could normally start at 0, but here we have deliberately chosen a poor fit.
The initial line lies above most house prices and slopes downward as size increases.
The point on the right gives the (w,b) position corresponding to that line.
The height of the lower surface is the cost calculated with the same parameters.
We will now keep the data fixed and change only the parameters.

Source slide 73: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p77
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 82 / ML source slide 74 / The First Gradient Descent Update

One update adds the orange prediction line.
It is closer to the data overall than the previous line, and the cost decreases.
The new point on the right gives the w and b that determine this new line.
The displayed cost falls from about 77,237 to about 45,401.
The line changes on one side and the point moves on the other, but both are results of the same update.

Source slide 74: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p78
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 83 / ML source slide 75 / Lowering Cost Step by Step

We calculate the derivatives again at the new parameters and move to the next step.
The green line is added, and the cost falls to about 29,109.
Predictions for individual houses do not all improve by the same proportion.
We check whether the cost calculated over all the examples has decreased.
The line still points in a different direction from the data's trend, so there is more to learn.

Source slide 75: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p79
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 84 / ML source slide 76 / Changing the Slope and Intercept

Adding the red line also changes the difference between predictions for large and small houses.
Changing b alone moves every prediction up or down by the same amount.
If w changes as well, the prediction change depends on x.
Here we adjust both parameters to move to a lower cost.
The connected points on the right trace the path of parameter values selected so far.

Source slide 76: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p80
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 85 / ML source slide 77 / The Line Becomes Flatter

The new line is less steep than the previous one.
We are gradually correcting the initial negative slope, which did not fit the data.
The new point also moves lower on the cost surface below.
We do not judge the line as better merely because it looks less steep.
We check that the overall cost relative to the actual values also decreases.

Source slide 77: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p81
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 86 / ML source slide 78 / Approaching a Horizontal Line

The line has now become almost horizontal.
A horizontal line is not the goal; this is an intermediate state on the way to a better line.
An almost horizontal line predicts similar prices for houses of different sizes.
However, the data has an increasing trend with size, so further improvement is possible.
Continue the updates while watching whether the cost on the right keeps decreasing.

Source slide 78: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p82
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 87 / ML source slide 79 / Finding a Positive Slope

With further updates, an upward-sloping line appears.
The model now predicts higher prices for larger houses.
No person separately instructed it to make w positive.
This is the result of following errors and derivatives calculated from the data.
Here, saying that training reflects the relationship in the data means this change in the parameters.

Source slide 79: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p83
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 88 / ML source slide 80 / Approaching the Best Fit

The new lines are approaching the central trend in the data.
The point on the right is also moving closer to the center of the contours.
Near the center, there is less opportunity to reduce the cost by a large amount.
Changes from additional updates may therefore become smaller.
Watching this progress helps us decide whether to stop or continue training.

Source slide 80: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p84
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 89 / ML source slide 81 / Predicting with the Learned Line

We will use the final line to predict the price of a new house.
Find size 1,250 on the horizontal axis and read the height where it meets the current prediction line.
The diagram gives about $250,000.
This differs from the earlier prediction made by another line because the parameters are different.
We still do not know the actual sale price, but we have applied the learned relationship to a new input.
Finding the parameters is training, and calculating f(x) using those parameters is prediction.

Source slide 81: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p85
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 90 / ML source slide 82 / Learning from Every Training Example

The derivative expressions so far have used every example, from i=1 to m, on each step.
Using the entire training set for one update is called batch gradient descent.
With 47 examples, we collect information from all 47 to obtain one correction.
Distinguish this from updating after looking at just one example.
Other methods use only part of the data, but for now we will learn the principle using the full dataset.
We have completed the sequence of predicting with a line, evaluating with a cost, and improving it through gradient descent.
Next, we will increase the number of inputs and perform the same calculations more efficiently.

Source slide 82: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p86
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 91 / ML source slide 83 / Linear Regression with Many Features

Last week, we predicted a house's price from its size alone.
However, even equally sized houses may have different prices because of their room counts or construction years.
This time, we will extend linear regression to use several pieces of information together.
Think of it as adding more inputs to the equation we already use, rather than building an entirely unrelated model.

Source slide 83: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p88
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 92 / ML source slide 84 / Reviewing the Single Feature Model

First, we will review the model we already know.
In the table, house size is input x and the actual sale price is the target y.
Given one house's size, f(x)=wx+b returns one predicted price.
Here, w determines how much the predicted price changes for a one-unit increase in size, while b determines the overall height of the line.
The current model always predicts the same price for two houses of equal size.
In reality, houses with more rooms or more recent construction may sell for different prices.
If size is the only input, the model has no information that lets it distinguish those differences.
We therefore want to add information that may help prediction, such as room count, floor count, and house age.

Source slide 84: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p89
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 93 / ML source slide 85 / Reading Rows, Features, and Examples

The input part of the table now represents one house using four numbers.
The feature x₁ is size, x₂ is room count, x₃ is floor count, and x₄ is house age.
Each input item is called a feature, and we write the number of features as n.
Here there are four features, so n=4.
The complete input for the second house, x⁽²⁾, is a vector collecting 1416, 3, 2, and 40.
If the word vector is unfamiliar, think of it as an ordered list of numbers describing one house.
The value x₃⁽²⁾ is the third item in that list, so it represents the second house's floor count, 2.
The parenthesized 2 above identifies the second house, and the 3 below identifies the third feature.
Neither mark represents a square or multiplication.
Even when expressions become longer, the superscript identifies a data row and the subscript identifies an input column.

Source slide 85: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p90
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 94 / ML source slide 86 / Giving Each Feature a Weight

With four inputs, multiply each input by its own weight and add all the results.
In the slide's example, size is multiplied by 0.1, room count by 4, floor count by 10, and house age by −2, before adding 80 at the end.
Because prices are in thousands of dollars, the room-count coefficient 4 means that one more room increases the predicted price by $4,000 when the other inputs are held fixed.
The coefficient −2 on house age means that an additional year lowers the predicted price by $2,000 when the other inputs remain the same.
These are relationships expressed by this model, not a guarantee that adding a room will increase the actual sale price by exactly that amount.
The final b adjusts the overall prediction level after the effects of the inputs are added.
When every input is 0, the expression equals b, but such a house does not need to exist in reality.
Each w is a control that determines how much, and in which direction, its input contributes to the prediction.
The next step is to learn these values to reduce a cost function, rather than having a person continually choose them.

Source slide 86: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p91
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 95 / ML source slide 87 / Writing the Model with Vectors

Writing every term becomes cumbersome as the number of features grows.
We will therefore collect the weights into a vector w and one house's inputs into a vector x.
The dot product w·x multiplies numbers in corresponding positions and adds the results.
Thus w·x+b performs exactly the same calculation as w₁x₁+w₂x₂+w₃x₃+w₄x₄+b.
The notation is shorter, but the model's behavior is unchanged.
With n inputs, w and x each contain n values, and the result is one predicted price.
The bias b is a separate single number added to those vectors' dot product.
This model with several inputs is called multiple linear regression.
The output is still one house price; multiple refers to using several inputs.

Source slide 87: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p92
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 96 / ML source slide 88 / Gradient Descent with Many Features

Now we will train a model that uses several features.
We need to make predictions with the model, calculate the cost, and update each parameter.
We will retain the single-input sequence and extend the part that now contains several weights.

Source slide 88: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p98
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 97 / ML source slide 89 / The Same Model in Vector Notation

The left-hand formula writes every input and weight separately, while the right-hand formula collects them into vectors.
Either form takes one house's inputs and calculates one prediction.
The cost function subtracts the actual price from each house's predicted price, squares the result, and adds these terms.
As before, we add the squared errors for m houses and divide by 2m.
Having more inputs does not make the target y or the prediction a vector.
What changes is the set of cost-adjustment controls: instead of one w and b, we have several weights and b.
With two weights, we must find w₁, w₂, and b together.
Think of this as extending the bowl-shaped cost we have drawn into more directions.
Although high-dimensional problems are hard to draw completely, the derivative-based update rule still applies.

Source slide 89: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p99
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 98 / ML source slide 90 / Updating Every Feature Weight

With one input, the derivative for w was the average prediction error multiplied by x.
For the jth weight wⱼ, multiply each example's prediction error by its jth input xⱼ.
Adding these results over m examples and dividing by m gives the derivative for that weight.
The prediction errors are shared, but each weight's derivative differs because it multiplies a different feature.
For b, average the prediction errors without multiplying an input.
In this expression, i identifies the house and j identifies the feature.
First use all the current w values and b to calculate prediction errors, then calculate every derivative at that same state.
Next, subtract the learning rate times each parameter's own derivative from that parameter.
This differs from updating w₁ and then using its new value to calculate w₂'s derivative.
Within one update, every parameter must use a derivative calculated from the same starting position.
Repeating this calculation moves toward lower cost while using several inputs together.

Source slide 90: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p100
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 99 / ML source slide 91 / Why Feature Scaling Helps

Training can take unnecessarily long even when the model and update expressions are correct.
One cause is large differences in the numerical scales of the inputs.
Feature scaling adjusts these differences to help gradient descent move more easily.

Source slide 91: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p102
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 100 / ML source slide 92 / Feature Size and Weight Size

House sizes range from hundreds to thousands, while room counts are usually only a few.
The two inputs begin with very different numerical ranges.
For a house with size 2000 and 5 rooms, substitute w₁=50, w₂=0.1, and b=50.
The prediction is 50×2000+0.1×5+50, giving 100050.5 in units of thousands of dollars.
Conversely, w₁=0.1, w₂=50, and b=50 give 200+250+50=500.
The second combination predicts $500,000, matching the actual price in this example.
We can see that a numerically large input may need a relatively small weight, while a numerically small input may need a relatively large weight.
Therefore, do not compare weights alone to decide which feature is more important.
The input's units and range also affect the magnitude of its weight.
This difference also affects the cost landscape through which gradient descent moves.

Source slide 92: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p103
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 101 / ML source slide 93 / Why the Cost Surface Gets Stretched

The horizontal and vertical axes here are weights w₁ and w₂, not house size and room count.
Each contour connects weight combinations with equal cost.
A small change in a weight multiplying a large input, such as house size, can produce a large prediction change.
Cost can then be sensitive to movement in that weight's direction.
In the other direction, a larger weight change may be needed to produce a similar cost change.
The contours become long and narrow rather than approximately circular.
Imagine descending a long, narrow valley.
You need to move carefully across its steep sides, yet progress along the floor can be slow.
This shape is connected to gradient descent's zigzag movement.

Source slide 93: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p104
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 102 / ML source slide 94 / Scaling Helps Gradient Descent

On the left, gradient descent travels downward while crossing back and forth across a narrow valley.
A large learning rate may overshoot to the opposite side, while a small one may take a long time to reach the goal.
On the right, the features have been adjusted to similar numerical scales.
This can reduce differences in sensitivity across weight directions and produce more balanced contours.
The movement can then approach the same goal with less unnecessary zigzagging.
Feature scaling changes the numerical units used to represent inputs, rather than changing the target house prices.
It is like expressing a length in centimeters instead of meters without changing the object itself.
Of course, if inputs are strongly related, scaling alone will not make the contours perfect circles.
The aim is to reduce scale differences that make training difficult, rather than to force every plot into the same shape.

Source slide 94: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p105
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 103 / ML source slide 95 / How to Scale Features

There are several methods of feature scaling.
We will look in order at dividing by a maximum, subtracting a mean, and using a standard deviation.
Instead of only memorizing the expressions, watch how changing one input affects its numerical range and center.

Source slide 95: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p106
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 104 / ML source slide 96 / Dividing by Each Feature's Maximum

A simple approach divides each feature by a representative large value of that feature.
If the maximum house size is 2000, divide the sizes by 2000.
A house of size 1000 becomes 0.5, and one of size 2000 becomes 1.
If the maximum room count is 5, divide room counts by 5, making 3 rooms become 0.6.
An original size range of 300 to 2000 becomes 0.15 to 1.
The room-count range changes from 0 to 5 into 0 to 1.
Even without identical ranges, the resulting numerical scales are much more similar.
The ordering is preserved too: larger houses still have larger values than smaller houses.
When predicting a new house, divide by the same training values, 2000 and 5, to express its inputs on the same basis.

Source slide 96: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p107
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 105 / ML source slide 97 / Centering Features around the Mean

This time, we will subtract each feature's mean before dividing.
This is mean normalization; the slide divides the centered value by the difference between the maximum and minimum.
If the mean house size is 600, a house of size 600 moves to 0.
Houses below the mean become negative, and those above the mean become positive.
Size 300 becomes (300−600)/(2000−300), or about −0.18.
Size 2000 becomes about 0.82 using the same expression.
Subtracting the mean room count 2.3 and dividing by its range 5 changes its range to about −0.46 to 0.54.
A negative value does not mean a house literally has a negative number of rooms; it means fewer rooms than average.
Subtracting the mean shifts the center, while dividing by the range adjusts the numerical scale.
The transformed values therefore do not have to reach both −1 and 1 or be symmetric around 0.

Source slide 97: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p108
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 106 / ML source slide 98 / Scaling by the Standard Deviation

Z-score normalization also starts by subtracting the mean, but divides by standard deviation σ instead of the range.
Standard deviation measures how spread out values are around their mean.
If house size has mean 600 and standard deviation 450, size 1050 becomes 1 because it is one standard deviation above the mean.
Size 300 becomes (300−600)/450, or about −0.67.
Size 2000 becomes about 3.1, showing that this method does not always produce values between −1 and 1.
Room counts separately use that feature's mean 2.3 and standard deviation 1.4.
We do not use the same mean or standard deviation for house size and room count.
The transformation lets us compare how far each value lies from its own feature's mean using a similar basis.
It does not automatically turn the data distribution itself into a bell curve.
Store the mean and standard deviation calculated from training data and apply those same values to new inputs.

Source slide 98: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p109
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 107 / ML source slide 99 / Choosing Similar Feature Ranges

Feature scaling does not aim to force every input into one exact interval.
If scales are broadly similar, ranges such as −1 to 1 or −3 to 3 can both work.
On the other hand, an input in the hundreds and another around 0.001 have very different scales.
In that situation, there is a clear reason to apply scaling.
Some features, such as body temperature, may have only small differences while their values cluster around 100.
Subtracting the mean to shift the center can help in that situation.
Whatever method you choose, determine the reference values separately for each feature and use the same references during training and prediction.
You do not need to memorize that a particular formula must always be applied even to inputs with similar ranges.
First examine the actual input values and judge whether their scales are convenient for gradient descent.

Source slide 99: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p110
Course: Andrew Ng, DeepLearning.AI, Stanford Online
