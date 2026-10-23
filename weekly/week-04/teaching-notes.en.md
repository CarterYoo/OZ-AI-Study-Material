# Course 1 / Week 2 / English speaker notes

English teaching script. Slide numbers refer to the shared classroom deck; source pages identify matching pages in the export.

## Slide 83 | W2 | Source page 2

Last week, we predicted a house's price from its size alone.  
However, even equally sized houses may have different prices because of their room counts or construction years.  
This time, we will extend linear regression to use several pieces of information together.  
Think of it as adding more inputs to the equation we already use, rather than building an entirely unrelated model.  

## Slide 84 | W2 | Source page 3

First, we will review the model we already know.  
In the table, house size is input x and the actual sale price is the target y.  
Given one house's size, f(x)=wx+b returns one predicted price.  
Here, w determines how much the predicted price changes for a one-unit increase in size, while b determines the overall height of the line.  
The current model always predicts the same price for two houses of equal size.  
In reality, houses with more rooms or more recent construction may sell for different prices.  
If size is the only input, the model has no information that lets it distinguish those differences.  
We therefore want to add information that may help prediction, such as room count, floor count, and house age.  

## Slide 85 | W2 | Source page 4

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

## Slide 86 | W2 | Source page 5

With four inputs, multiply each input by its own weight and add all the results.  
In the slide's example, size is multiplied by 0.1, room count by 4, floor count by 10, and house age by −2, before adding 80 at the end.  
Because prices are in thousands of dollars, the room-count coefficient 4 means that one more room increases the predicted price by $4,000 when the other inputs are held fixed.  
The coefficient −2 on house age means that an additional year lowers the predicted price by $2,000 when the other inputs remain the same.  
These are relationships expressed by this model, not a guarantee that adding a room will increase the actual sale price by exactly that amount.  
The final b adjusts the overall prediction level after the effects of the inputs are added.  
When every input is 0, the expression equals b, but such a house does not need to exist in reality.  
Each w is a control that determines how much, and in which direction, its input contributes to the prediction.  
The next step is to learn these values to reduce a cost function, rather than having a person continually choose them.  

## Slide 87 | W2 | Source page 6

Writing every term becomes cumbersome as the number of features grows.  
We will therefore collect the weights into a vector w and one house's inputs into a vector x.  
The dot product w·x multiplies numbers in corresponding positions and adds the results.  
Thus w·x+b performs exactly the same calculation as w₁x₁+w₂x₂+w₃x₃+w₄x₄+b.  
The notation is shorter, but the model's behavior is unchanged.  
With n inputs, w and x each contain n values, and the result is one predicted price.  
The bias b is a separate single number added to those vectors' dot product.  
This model with several inputs is called multiple linear regression.  
The output is still one house price; multiple refers to using several inputs.  

## Slide 88 | W2 | Source page 7

Now we will see how to implement the same calculation in Python.  
Vectorization expresses operations on several numbers as array operations.  
This makes the connection between the formula and the code clearer, and can make computation more efficient as the number of values grows.  

## Slide 89 | W2 | Source page 8

The example sets w to 1, 2.5, and −3.3, x to 10, 20, and 30, and b to 4.  
Calculating directly gives 1×10+2.5×20−3.3×30+4.  
The three products sum to −39, and adding b gives the final prediction −35.  
Writing every term separately, as in the first implementation, requires changing the code each time we add features.  
A for loop can add as many terms as needed, but it still describes the calculations one at a time.  
NumPy's np.dot(w,x) expresses the matching multiplications and their sum as one array operation.  
Adding b gives np.dot(w,x)+b, corresponding to the mathematical expression w·x+b.  
All three implementations perform the same calculation and give the same answer.  
Remember that mathematics calls the first input x₁, while Python retrieves the first array item as x[0].  
Vectorization implements the same prediction formula in an array-oriented form, rather than introducing a new formula.  

## Slide 90 | W2 | Source page 9

There is an important reason to use vectorization beyond making code shorter.  
It lets us ask the computer to process many numbers efficiently.  
This diagram compares requesting calculations with a loop and requesting them as array operations.  

## Slide 91 | W2 | Source page 10

The left-hand diagram shows the products at each position being processed one by one in a loop over time.  
It calculates the first product, then the next, and gathers the results in that sequence.  
The right-hand diagram shows an array operation processing several values together.  
It is like providing the whole list of numbers at once, rather than requesting each calculation separately.  
A library such as NumPy can then use efficiently implemented operations and the hardware's processing capabilities.  
The diagram does not mean every calculation literally finishes at the same instant.  
The actual execution and speed depend on array size, the library, and the computer.  
Using np.dot also does not automatically mean a GPU is being used.  
Remember that array operations provide a concise way to describe large numerical computations and have them carried out efficiently.  

## Slide 92 | W2 | Source page 11

Vectorization can be used for gradient descent as well as prediction.  
The diagram places 16 weights in w and the corresponding 16 derivatives in d.  
The first value of d contains information about the direction and amount of change for the first weight.  
If the learning rate is 0.1, subtract 0.1 times each weight's own derivative from that weight.  
A loop applies the same update expression 16 times while changing the index.  
With arrays, w=w−0.1×d expresses those corresponding calculations together.  
The values in d must have been calculated in advance at the current weights.  
This code does not let us skip the calculation of the derivatives themselves.  
The diagram focuses on updating the weight vector; b is separately updated using its own derivative.  
The gradient-descent rule is unchanged; only its representation for several weights differs.  

## Slide 93 | W2 | Source page 12

Now we will train a model that uses several features.  
We need to make predictions with the model, calculate the cost, and update each parameter.  
We will retain the single-input sequence and extend the part that now contains several weights.  

## Slide 94 | W2 | Source page 13

The left-hand formula writes every input and weight separately, while the right-hand formula collects them into vectors.  
Either form takes one house's inputs and calculates one prediction.  
The cost function subtracts the actual price from each house's predicted price, squares the result, and adds these terms.  
As before, we add the squared errors for m houses and divide by 2m.  
Having more inputs does not make the target y or the prediction a vector.  
What changes is the set of cost-adjustment controls: instead of one w and b, we have several weights and b.  
With two weights, we must find w₁, w₂, and b together.  
Think of this as extending the bowl-shaped cost we have drawn into more directions.  
Although high-dimensional problems are hard to draw completely, the derivative-based update rule still applies.  

## Slide 95 | W2 | Source page 14

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

## Slide 96 | W2 | Source page 15

Besides gradient descent, linear regression has methods that solve for parameters using equations.  
This slide introduces one as the normal equation.  
Instead of moving in small steps, it uses the mathematical structure of linear regression to obtain parameters.  
An advantage is that it does not require choosing a learning rate or iteration count.  
However, the associated matrix calculations can become expensive when there are very many features.  
Treat the slide's figure of 10,000 as an example illustrating a problem at larger scales.  
The same method also does not apply to every model.  
Library implementations of linear regression can use several numerical methods, so they do not necessarily evaluate one fixed formula directly.  
We will focus on gradient descent because it also connects to logistic regression and neural networks later.  

## Slide 97 | W2 | Source page 16

Training can take unnecessarily long even when the model and update expressions are correct.  
One cause is large differences in the numerical scales of the inputs.  
Feature scaling adjusts these differences to help gradient descent move more easily.  

## Slide 98 | W2 | Source page 17

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

## Slide 99 | W2 | Source page 18

The horizontal and vertical axes here are weights w₁ and w₂, not house size and room count.  
Each contour connects weight combinations with equal cost.  
A small change in a weight multiplying a large input, such as house size, can produce a large prediction change.  
Cost can then be sensitive to movement in that weight's direction.  
In the other direction, a larger weight change may be needed to produce a similar cost change.  
The contours become long and narrow rather than approximately circular.  
Imagine descending a long, narrow valley.  
You need to move carefully across its steep sides, yet progress along the floor can be slow.  
This shape is connected to gradient descent's zigzag movement.  

## Slide 100 | W2 | Source page 19

On the left, gradient descent travels downward while crossing back and forth across a narrow valley.  
A large learning rate may overshoot to the opposite side, while a small one may take a long time to reach the goal.  
On the right, the features have been adjusted to similar numerical scales.  
This can reduce differences in sensitivity across weight directions and produce more balanced contours.  
The movement can then approach the same goal with less unnecessary zigzagging.  
Feature scaling changes the numerical units used to represent inputs, rather than changing the target house prices.  
It is like expressing a length in centimeters instead of meters without changing the object itself.  
Of course, if inputs are strongly related, scaling alone will not make the contours perfect circles.  
The aim is to reduce scale differences that make training difficult, rather than to force every plot into the same shape.  

## Slide 101 | W2 | Source page 20

There are several methods of feature scaling.  
We will look in order at dividing by a maximum, subtracting a mean, and using a standard deviation.  
Instead of only memorizing the expressions, watch how changing one input affects its numerical range and center.  

## Slide 102 | W2 | Source page 21

A simple approach divides each feature by a representative large value of that feature.  
If the maximum house size is 2000, divide the sizes by 2000.  
A house of size 1000 becomes 0.5, and one of size 2000 becomes 1.  
If the maximum room count is 5, divide room counts by 5, making 3 rooms become 0.6.  
An original size range of 300 to 2000 becomes 0.15 to 1.  
The room-count range changes from 0 to 5 into 0 to 1.  
Even without identical ranges, the resulting numerical scales are much more similar.  
The ordering is preserved too: larger houses still have larger values than smaller houses.  
When predicting a new house, divide by the same training values, 2000 and 5, to express its inputs on the same basis.  

## Slide 103 | W2 | Source page 22

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

## Slide 104 | W2 | Source page 23

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

## Slide 105 | W2 | Source page 24

Feature scaling does not aim to force every input into one exact interval.  
If scales are broadly similar, ranges such as −1 to 1 or −3 to 3 can both work.  
On the other hand, an input in the hundreds and another around 0.001 have very different scales.  
In that situation, there is a clear reason to apply scaling.  
Some features, such as body temperature, may have only small differences while their values cluster around 100.  
Subtracting the mean to shift the center can help in that situation.  
Whatever method you choose, determine the reference values separately for each feature and use the same references during training and prediction.  
You do not need to memorize that a particular formula must always be applied even to inputs with similar ranges.  
First examine the actual input values and judge whether their scales are convenient for gradient descent.  

## Slide 106 | W2 | Source page 25

Now we will see how to check whether training is progressing well.  
Running gradient descent does not by itself establish that we obtained the desired result.  
Recording how the cost changes on each iteration lets us inspect the training process.  

## Slide 107 | W2 | Source page 26

The expression on the screen is the gradient-descent update rule we have been using.  
Calculate derivatives at the current parameters, multiply by learning rate α, and subtract.  
Applying this to every weight and b completes one update.  
We can then calculate the cost over all the training data using the new parameters.  
Record that cost, update again, and record the cost again, repeating this sequence.  
This provides a numerical record of whether prediction errors decrease as training progresses.  
In particular, examine the actual cost changes rather than trusting the update expression alone to establish that α is appropriate.  
The next graph plots exactly this record in chronological order.  

## Slide 108 | W2 | Source page 27

The horizontal axis of this graph shows the number of gradient-descent iterations, rather than w.  
The vertical axis is the cost J calculated at each iteration.  
Where J(w) described a landscape over parameter values, this graph records the costs encountered during training.  
Cost initially falls quickly, then decreases by smaller amounts as iterations continue.  
This decreasing trend is what we can expect from batch gradient descent with an appropriate learning rate.  
The slide's automatic stopping method stops when one update reduces the cost by only a tiny amount.  
For example, it could check whether the decrease is below 0.001, but the appropriate threshold depends on the cost's scale and the problem.  
A very small learning rate can also make cost barely change, so a flat curve does not always establish that a good solution has been reached.  
Consider the size of the decrease, the final cost, and whether training has run for enough iterations.  
This graph also measures fit to the training data; performance on new data must be checked separately.  

## Slide 109 | W2 | Source page 28

The learning rate controls how strongly a derivative contributes to one update.  
If it is too large, descent can become unstable; if it is too small, training can take a long time.  
We will now use cost graphs to look for an appropriate value.  

## Slide 110 | W2 | Source page 29

If the cost increases over iterations or swings sharply up and down, as on the left, training is not progressing well.  
In the diagram on the right, one step is too large and crosses over the minimum to the other side.  
If the next step is also too large, repeated crossings can take the parameters farther away.  
In this case, try reducing the learning rate.  
However, the learning rate is not the only possible reason for an increasing cost.  
The implementation may add a value that should be subtracted, or calculate a derivative incorrectly.  
If the cost fails to decrease in the expected direction even with a very small learning rate, inspect the code and arithmetic.  
Using a small value to check for a decrease is a diagnostic method, rather than a rule to use the smallest value permanently.  
Here, we interpret these graphs for batch gradient descent, which uses the whole training dataset at each step.  

## Slide 111 | W2 | Source page 30

When choosing a learning rate, try values that increase by roughly a factor of three, such as 0.001, 0.003, 0.01, and 0.03.  
Rather than trying every value at tiny intervals, first search a broad range for a suitable order of magnitude.  
When comparing candidates, keep the data, starting parameters, and iteration count the same.  
Then examine whether cost decreases steadily and how quickly it falls within the same number of iterations.  
A very small α may be stable but make the graph descend slowly.  
A large α may descend quickly before becoming unstable, or raise the cost from the start.  
We want a value that reduces cost both steadily and reasonably quickly.  
Develop the habit of choosing from evidence in the cost graph, rather than memorizing one number as the answer to every problem.  
Also remember that changing feature scaling can change which learning rate is appropriate.  

## Slide 112 | W2 | Source page 31

So far, we have used the given features directly.  
Combining the original inputs into new features can let a model express more useful relationships.  
This is called feature engineering: designing which numbers to show the model.  

## Slide 113 | W2 | Source page 32

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

## Slide 114 | W2 | Source page 33

Feature engineering can let linear regression represent curved relationships too.  
One approach makes x² or x³ into additional features alongside x itself.  
A model using these polynomial terms is called polynomial regression.  

## Slide 115 | W2 | Source page 34

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

## Slide 116 | W2 | Source page 35

A new feature does not have to be a square or a cube.  
For example, √x can help express a relationship whose increase becomes smaller as x grows.  
The function √x keeps increasing, but its curve becomes progressively gentler.  
However, the final prediction also depends on the other terms and their weights, so adding √x does not force the whole model to have that same shape.  
Choose suitable representations using both your understanding of the problem and evaluation on actual data.  
This week's methods connect to representing inputs well and learning weights while reducing cost steadily.  
Inputs may be multiple values or transformed features, but the basic training sequence remains the same.  
Next, we will move from predicting continuous quantities such as house prices to classification: predicting membership in a category.
