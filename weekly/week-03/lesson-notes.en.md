# Week 03 / Cost Functions and Gradient Descent

English teaching notes matched to the OZ classroom slide order.
The explanations are instructional adaptations, not verbatim lecture transcripts.

## Canva page 43 / ML source slide 35 / Understanding the Cost Function

We have read the cost formula, but how its number relates to the model's shape may still feel unfamiliar.
We will connect the two by substituting values into a small dataset ourselves.
On one side, we will look at the prediction line; on the other, we will look at the score evaluating that line.

Source slide 35: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p39
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 44 / ML source slide 36 / Simplifying to One Parameter

The left-hand expression is the original model f(x)=wx+b, where both w and b can change.
On the right, we fix b at 0 to simplify the diagram.
The model becomes f(x)=wx, leaving only w to adjust.
Substituting x=0 always gives 0, so all these lines pass through the origin.
Changing w now changes only the slope of the line.
Recalculating the errors on the same data gives the J(w) corresponding to that w.
The w written below minimize indicates which value we will change to reduce the cost.
It means we will keep x and y fixed as the evaluation data and change only w.
Returning to the original problem, we adjust both parameters together, so both w and b appear below minimize.

Source slide 36: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p40
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 45 / ML source slide 37 / The Cost of a Perfect Fit

To make the arithmetic simple, we have chosen three examples: (1,1), (2,2), and (3,3).
First, choosing w=1 gives the model f(x)=x.
For the first example, x=1 gives a prediction of 1 and the actual value is also 1, so the error is 0.
The remaining two examples are also predicted exactly as 2 and 3.
Therefore J(1)=(0²+0²+0²)/(2×3)=0.
Now we will transfer this result to the graph on the right.
Its horizontal axis is the selected parameter w rather than x, and its vertical axis is cost rather than price.
We therefore plot one point at horizontal coordinate 1 and vertical coordinate 0.
The line on the left has predictions for many x values, but evaluating that entire line produces one score.
The key idea on this slide is that one prediction line corresponds to one point on the cost graph.

Source slide 37: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p41
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 46 / ML source slide 38 / The Cost of a Smaller Slope

This time, w has changed to 0.5.
The data stays the same; only the model changes to f(x)=0.5x.
At x=1, the prediction is 0.5, so the error is 0.5−1=−0.5.
At x=2 the error is 1−2=−1, and at x=3 it is 1.5−3=−1.5.
The vertical segments in the diagram show the sizes of these differences.
Squaring them gives 0.25, 1, and 2.25, whose sum is 3.5.
Because there are three examples, we divide by 2m=6 to get J(0.5)=3.5/6, or about 0.58.
We plot (0.5,0.58) on the right.
The horizontal coordinate 0.5 represents the line's slope, not the size of a house.
Because the predictions are worse overall than at w=1, this point lies higher on the cost graph.

Source slide 38: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p42
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 47 / ML source slide 39 / Comparing Costs across Slopes

When w=0, the model always predicts 0 regardless of the input.
The errors are therefore −1, −2, and −3, whose squares are 1, 4, and 9.
Since J(0)=14/6, the cost is about 2.33.
On the right-hand graph, find the point at horizontal coordinate 0 and vertical coordinate 2.33.
Changing w to −0.5 gives predictions of −0.5, −1, and −1.5, which are farther from the actual values.
In that case, J increases to 5.25.
Conversely, choosing w close to 1 brings the line closer to the three examples and lowers the cost.
Repeating the calculation for different values of w and collecting the points produces the U-shaped curve on the right.
The prediction model can be a straight line while the function evaluating that line is curved.
That is because the two diagrams answer different questions.

Source slide 39: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p43
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 48 / ML source slide 40 / Finding the Lowest Cost

We can now read the choice of a good w from the right-hand graph.
The lowest point is at w=1, where the cost is 0.
For this dataset, a line passes through all three points exactly, so a cost of 0 is possible.
In real data, all points may not lie on a single line, so the minimum cost may be greater than 0.
The expression minimize_w J(w) asks us to find the smallest achievable cost, rather than requiring us to make it 0.
If b can also change, we compare combinations of slope and height.
We write that objective as minimize_{w,b} J(w,b).
The problem of finding good parameters is now defined numerically.

Source slide 40: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p44
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 49 / ML source slide 41 / Visualizing the Cost Function

When only w could change, one horizontal axis could represent all candidates.
Now we will remove the restriction that fixed b at 0 and return to the original model.
Changing both the slope and height of the line also requires more axes for drawing the cost.

Source slide 41: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p45
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 50 / ML source slide 42 / The Model, Cost, and Objective

Connect the model, parameters, cost, and objective in order.
The model f(x)=wx+b calculates a prediction from an input.
The values w and b are the quantities we can change.
The cost J(w,b) evaluates how far those predictions are from the actual data.
The objective is to find the combination of w and b with the smallest cost.
For example, increasing b while keeping the slope fixed raises every prediction together.
We decide whether that change is helpful by checking whether the gaps from the actual values shrink overall.
Changing a parameter and reducing the cost therefore do not mean the same thing.

Source slide 42: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p46
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 51 / ML source slide 43 / One Line, One Point on the Cost Surface

The left-hand model has w=0.06 and b=50, giving f(x)=0.06x+50.
For a house size of 1000, it predicts 110, or $110,000.
Compared with the actual points, it predicts most prices too low.
Calculating all the errors for this line gives one score, J(0.06,50).
Previously, choosing w alone was enough; now both w and b must be specified to determine a score.
The function f on the left takes house size x as input, while J on the right takes the model's parameters as input.
Although both are functions, what goes into them and what comes out are different.
Representing every combination of two parameters requires positions on a plane, with cost shown as height above that plane.

Source slide 43: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p47
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 52 / ML source slide 44 / Cost as a Surface

One axis on the floor represents w, and the other represents b.
Choosing one position on that floor is equivalent to choosing one pair of parameters.
Moving upward from that position until we meet the surface gives the height J(w,b).
The displayed w=−10 and b=−15 are simply one example of such a combination.
The surface dips toward the middle like a bowl or a hammock.
High positions represent models that fit the data poorly, while low positions represent better fits.
Training aims to move the floor coordinates to find low parts of this surface.
Moving downward here means lowering the cost, rather than always lowering predicted house prices.
Also distinguish the slope of the prediction model from the slope of the cost surface.

Source slide 44: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p48
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 53 / ML source slide 45 / From a Surface to a Contour Plot

A 3D surface helps us understand the overall landscape.
However, some areas can be hidden behind others, and comparing several positions precisely can be awkward.
If we represent heights with lines, we can view the same information on a plane.
This is a contour plot, using the same principle as the contour lines on a familiar map.

Source slide 45: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p49
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 54 / ML source slide 46 / Contours Connect Equal Heights

Imagine cutting a mountain horizontally at a fixed height.
Connecting the outline where that slice meets the mountain surface produces the red line.
Every position on that line has the same height, whether it is to the east or west.
Changing the slicing height produces another line.
Drawing these lines together shows how the mountain's height changes.
The essential idea is not that the lines are circular, but that each line connects points of equal height.

Source slide 46: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p50
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 55 / ML source slide 47 / Reading Contours from Above

This time we are looking down at the same mountain from above.
We can read the landscape from its contours even without drawing height directly on a vertical axis.
If successive contours represent equal height differences, closely spaced lines indicate that height changes quickly over a short distance.
Widely spaced lines indicate a gentler slope.
The center of a mountain may be high, but the center of the next cost plot is low.
Do not decide whether a position is high or low merely because it is central; check which function the contours represent.

Source slide 47: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p51
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 56 / ML source slide 48 / Connecting Lines, Surfaces, and Contours

The left-hand plot shows predictions as a line against input x, while the upper-right plot shows cost contours against w and b.
The 3D diagram below shows the same cost as the upper-right plot from another direction.
Points on one contour have the same J even when their w and b differ.
Consequently, two different lines on the left can receive the same overall evaluation score.
One line might make larger mistakes on small houses and another on large houses, while their average scores match.
Equal costs do not mean equal predictions.
In this diagram, inner contours represent lower costs.
Parameters near the center produce lines that fit the data better.
The lower diagram looks stretched sideways because of its axis ranges and viewing angle; it represents the same bowl-shaped landscape.

Source slide 48: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p52
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 57 / ML source slide 49 / Comparing Lines and Their Costs

Now we will choose specific parameters and examine how the prediction line relates to its cost.
First compare the line and data points on the left, then locate those parameters on the right.
Connect the three diagrams as different views of one model, rather than three separate experiments.

Source slide 49: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p53
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 58 / ML source slide 50 / A Line with the Wrong Slope

Here w=−0.15 and b=800, so the predicted price decreases as x increases.
However, the actual data generally shows larger houses selling for higher prices.
This produces predictions that are too high for small houses and too low for large houses.
For example, the prediction is 650 at x=1000 and 350 at x=3000.
The blue vertical gaps are large for many points.
The cost is half the mean of these squared errors, which is large in this case.
In the upper-right plot, horizontal coordinate −0.15 and vertical coordinate 800 identify this model.
Here, the vertical coordinate 800 is b rather than cost; cost must be read from the contour's value.

Source slide 50: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p54
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 59 / ML source slide 51 / A Constant Price Prediction

This time, we change the parameters to w=0 and b=360.
The model is f(x)=360, predicting $360,000 for every house.
It ignores differences between small and large houses, but its overall cost is lower than that of the previous incorrectly tilted line.
That does not mean every individual prediction has improved.
It means the model receives a better score when we collect and evaluate all the errors.
The selected point on the right is (w,b)=(0,360).
It has not yet reached the center of the contours, so better combinations are still available.

Source slide 51: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p55
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 60 / ML source slide 52 / Changing the Intercept

The equation is now f(x)=−0.15x+500.
Compared with the previous example with w=−0.15, the slope is unchanged and the entire line has moved downward.
However, this does not solve the problem that the data trends upward.
Lowering a line and lowering its cost are different actions.
If a prediction is already below its target, lowering it further increases the error.
Rather than only noticing that a value moved, recalculate the gaps from the actual values.
The cost graph summarizes the overall result as one score.

Source slide 52: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p56
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 61 / ML source slide 53 / A Line That Fits the Trend

Here w=0.13 and b=71, so the line follows the increasing trend in the data.
For example, it predicts 201 at size 1000 and 331 at size 2000.
Many data points lie relatively close above or below the line.
Not every error is 0, but the overall cost is lower than for the earlier candidates.
The corresponding point on the right therefore lies near the center of the contours.
When real observations are scattered, we cannot find a line that passes through every point.
We choose the available line that best satisfies the chosen evaluation criterion.
So far, a person has selected w and b, but this becomes inefficient when there are many candidates.
Next, we will learn to calculate how to move automatically toward a better choice.

Source slide 53: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p57
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 62 / ML source slide 54 / Gradient Descent

So far, we have manually chosen several w and b values and compared their costs.
Now we will calculate which direction to change the current values to improve the result.
Repeating that calculation is the method called gradient descent.
We will learn it for linear regression, but the same basic principle is used later to train neural networks.

Source slide 54: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p58
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 63 / ML source slide 55 / Repeated Updates Reduce Cost

First, choose starting values for w and b.
For the linear regression we are studying, both can start at 0.
The initial model is then a horizontal line that predicts 0 for every input.
We calculate the direction in which its cost decreases and move the parameters a little.
The situation has changed at the new position, so we calculate the direction again.
Repeating this process approaches a place where further movement hardly reduces the cost.
With several features, there are more values to adjust, such as w₁ and w₂, but the principle is unchanged.
The goal is to make the cost calculated from the parameters small, rather than to make the parameters themselves small.
The shape of the cost affects which positions can be reached and how training behaves.

Source slide 55: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p59
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 64 / ML source slide 56 / Different Starts, Different Minima

Imagine standing on top of the hill in the diagram.
Your position on the ground represents w and b, and your height represents cost.
At your current position, consider which direction goes downhill most steeply for a small movement.
Take a small step in that direction, then ask the same question at the new position.
You choose the direction again each time, rather than continuing straight along the direction chosen at the beginning.
The diagram has several valleys, so a small change in the starting position can lead into a different valley.
A valley floor that is lower than its surroundings is a local minimum.
The lowest value over the whole landscape is the global minimum.
Moving using only information around the current position does not guarantee that you will find a lower floor in another valley.
This diagram shows what a general cost function might look like; its shape differs from the cost of the linear regression we are studying.

Source slide 56: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p60
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 65 / ML source slide 57 / Implementing Gradient Descent

We will express the downhill direction and step size mathematically.
Although a new derivative symbol appears, first notice the structure of subtracting a correction from the current value.
Before memorizing the notation, read the expression in parts and identify each part's role.

Source slide 57: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p61
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 66 / ML source slide 58 / Updating Parameters Simultaneously

The expression w←w−α·∂J/∂w says to subtract a correction from the old w and store the result as the new w.
Read the equals sign on the screen as assignment in code, rather than a claim that the old and new values are equal.
For example, a=a+1 in code is an instruction to increase a by 1.
The positive learning rate α controls how far to move in the calculated direction.
The partial derivative ∂J/∂w describes how the cost changes when we change w slightly while keeping b at its current value.
We update b in the same way using ∂J/∂b.
Both corrections must be calculated using w and b from the same starting position.
It is like deciding how far to move east and north using one current position on a map.
If we update w first and then use that new value to calculate b's correction, we mix reference positions.
We can avoid this by first computing the results as tmp_w and tmp_b, as on the left, and then assigning the actual values.
A simultaneous update does not mean that the computer must literally execute two lines at the same instant.
It means that every correction is calculated from the same parameters before the update.

Source slide 58: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p62
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 67 / ML source slide 59 / Understanding Gradient Descent

We will check why the update expression contains a minus sign.
If we temporarily fix b, we can plot w and J(w) on a plane.
Follow the tangent slope to see which direction the expression actually moves us.

Source slide 59: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p63
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 68 / ML source slide 60 / Learning Rate and Derivative

Think of a straight line tangent to the cost curve at the current position.
The slope of that tangent is the derivative.
Its sign tells us whether cost increases or decreases when w increases slightly.
Its magnitude indicates how sensitively cost responds to the same small change.
The learning rate α is the step-size control multiplied by this information.
The actual movement is determined by the product of α and the derivative, rather than by α alone.
The slope here belongs to the cost curve, and has a different role from w, which we previously called the slope of the prediction line.
We calculate the cost's slope in order to adjust the model's slope w.

Source slide 60: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p64
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 69 / ML source slide 61 / Moving against the Slope

In the upper diagram, the tangent rises to the right, so the derivative is positive.
Moving right would raise the cost, so moving left is the helpful direction.
Subtracting the positive quantity α×derivative from the current w does make w smaller.
For example, if w=2, α=0.1, and the derivative is 3, the new w is 1.7.
In the lower diagram, the tangent falls to the right, so the derivative is negative.
Here we need to increase w and move right to reduce the cost.
Subtracting a negative number is equivalent to adding a positive number, so the update moves in that direction.
For example, if w=−1, the derivative is −2, and α=0.1, the new value is −0.8.
This algorithm does not always reduce w; it adjusts w in a direction that reduces cost.
This explanation concerns the direction of a small step from the current position, so choosing too large a step can cause problems.

Source slide 61: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p65
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 70 / ML source slide 62 / The Learning Rate

Even in the correct direction, moving too far at once can take us past our destination.
We will examine how the learning rate affects training.
A small value is not always better, and a large value is not always faster.

Source slide 62: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p66
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 71 / ML source slide 63 / Small and Large Learning Rates

If α is too small, as in the upper diagram, the correction obtained by multiplying the derivative is also tiny.
The cost decreases, but reaching the minimum requires many iterations.
Conversely, if α is too large, one update can jump across the valley.
Even if we change direction at the new position, another large jump can take us to a higher point on the opposite side.
The cost may then increase or keep oscillating instead of decreasing.
Approaching the minimum steadily is called convergence.
Moving farther away is called divergence.
Crossing the minimum once does not necessarily mean failure, but if the cost keeps increasing, check α.
What matters is the actual change in cost, rather than simply having a large step.

Source slide 63: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p67
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 72 / ML source slide 64 / Why Updates Stop at a Minimum

What will the next update do if we have already reached the local minimum in this diagram?
At a smooth valley floor like this, the tangent is horizontal, so the derivative is 0.
Multiplying that 0 by α gives a correction of 0.
In the example on the screen, w=5 and α=0.1 give 5−0.1×0=5.
Remaining at the same position is the desired behavior here.
However, a derivative of 0 by itself does not identify a minimum for every possible function.
This slide explains why the update stops when it is at a valley floor.

Source slide 64: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p68
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 73 / ML source slide 65 / Smaller Steps near the Minimum

You might think α must also be reduced each time we approach the minimum.
In this diagram, however, the movement becomes smaller naturally even with α fixed.
The initial steep region has a large derivative, which produces a large correction.
As we descend toward the floor, the tangent becomes gentler and the derivative's magnitude decreases.
Multiplying by the same α therefore gives a smaller result.
The learning rate and the actual step size are thus different quantities.
An appropriate fixed α can approach the minimum through progressively smaller movements.
This does not mean that an excessively large α will correct itself, so remember the earlier conditions too.

Source slide 65: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p69
Course: Andrew Ng, DeepLearning.AI, Stanford Online
