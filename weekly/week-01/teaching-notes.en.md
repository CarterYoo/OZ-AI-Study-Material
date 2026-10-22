# Course 1 / Week 1 / English speaker notes

English teaching script. Slide numbers refer to the shared classroom deck; source pages identify matching pages in the export.

## Slide 1 | W1 | Source page 2

We will start with how machine learning solves problems.  
The name may be unfamiliar, but you already use this technology when you see search results or receive video recommendations.  
Other examples include voice input that turns a friend's speech into text and tools that filter spam email.  
To build these features, would a person have to write a rule for every possible situation?  
Voices, photographs, and sentences have too many possible variations for that approach to work well.  
In machine learning, we provide examples and let a system find useful relationships in them.  
We will learn this process using data we can see directly, such as house sizes and prices.  
Connect the steps: what information goes in, what we predict, and what changes when a prediction is wrong.  
Our goal is for you to implement this process in code by the end.  

## Slide 2 | W1 | Source page 4

Imagine receiving an email saying you have won a large cash prize.  
The message sounds welcome, but its sender or wording may look suspicious.  
An email service can automatically place this kind of message in the spam folder.  
The input we give the computer is an email, and the answer we want is whether it is spam.  
A person could write a rule that always marks a particular word as spam, but ordinary emails may contain that word too.  
A simple rule also has limits because a small change in wording can get around it.  
Instead, we use examples of spam and ordinary email to learn patterns that help distinguish them.  
After training, we apply those patterns to an email that has not yet been classified.  
Remember this sequence: learn relationships from examples, then use them on new inputs.  

## Slide 3 | W1 | Source page 5

Machine learning is used in more than email and recommendation services.  
Factories can inspect product photographs for defects, and farms can use observations to examine crop conditions.  
It is also used to analyze medical images and manage energy production more efficiently.  
These problems share a feature: people can describe what they want, but writing every decision rule in code is difficult.  
That is why learning rules from data is useful.  
However, being able to run an algorithm does not guarantee a good result.  
We also need to know which data to use, what to treat as the correct answer, and what to check first when performance is poor.  
This course will cover both the principles of the algorithms and ways to make them work in practice.  

## Slide 4 | W1 | Source page 6

Having seen several applications, we will define machine learning more precisely.  
The key question is whether a computer can improve its performance through experience, rather than whether it thinks like a person.  
We will use a game to compare this with a program whose rules are all specified in advance.  

## Slide 5 | W1 | Source page 7

An important part of Arthur Samuel's definition is that a program can learn without being told every action individually.  
The example he studied was a program that played checkers.  
Listing every possible board position and writing down the best move would require an enormous number of rules.  
Instead, the program played many games and experienced which positions led to wins or losses.  
It used that experience to improve its decisions and choose favorable positions more often.  
A program created by a person does not have to make every choice less well than that person.  
By experiencing more games, it may become better than its creator.  
Learning here does not mean that the program magically invents its own rules.  
People still design how experience is represented and how performance is improved.  
The key is that, within that design, its decisions change according to the data.  

## Slide 6 | W1 | Source page 9

We will first look at a broad map of the methods we will encounter.  
Supervised learning learns from inputs paired with correct answers.  
Unsupervised learning looks for structure or patterns in data without an answer key.  
Recommender systems and reinforcement learning are also important topics, but for now we will distinguish the first two.  
You do not need to memorize all the algorithm names at once.  
When you encounter a problem, start by asking whether correct answers are available and what you want to predict.  
Knowing an algorithm and applying it well are also different abilities.  
Owning a hammer and a drill does not immediately enable you to build a house.  
You also need to learn how to choose a tool, check its result, and find the cause of a problem.  

## Slide 7 | W1 | Source page 10

We will first look more closely at supervised learning.  
Think of studying examples that include both questions and their correct answers.  
We will begin by telling the computer which part is the question and which part is the answer.  

## Slide 8 | W1 | Source page 11

We will write an input as x and its corresponding correct answer as y.  
In email classification, x is the email and y indicates whether it is spam.  
During training, we provide more than emails: we also identify which messages are spam and which are ordinary email.  
The algorithm examines many pairs of x and y to find their relationship.  
The name for this correct-answer information is a label.  
An important point is that the information available during training differs from what is available when we use the model.  
During training, it learns relationships by seeing the answers; in actual use, it does not know the answer for a new input.  
Learning is useful only if the system can predict an appropriate y from an x it has not seen before.  
Simply storing the answers to the examples would not solve new problems.  

## Slide 9 | W1 | Source page 12

For each row of the table, first identify the input and its matching output.  
Speech recognition takes sound as input and produces text representing that sound.  
Translation takes a sentence in one language and produces a sentence in another.  
In advertising, we can use an advertisement and information about a user to predict whether the user will click.  
To understand a vehicle's surroundings, camera and sensor information can help estimate where other cars are.  
In product inspection, the input is a product photograph and the output indicates whether a defect is present.  
Neither the input nor the output has to be a single number.  
They can take forms such as sentences, images, or positions, but eventually we represent them in a form the model can process.  
Although these problems look different, they all learn relationships between inputs and outputs from examples with known answers.  

## Slide 10 | W1 | Source page 13

Imagine that a friend is selling a house and asks how much they might receive.  
The horizontal axis shows house size, and the vertical axis shows the actual sale price.  
Prices are measured in thousands of dollars, so 200 on the vertical axis means $200,000.  
Each point represents one house's size and sale price.  
After fitting a straight line to these points, move upward from your friend's house size until you reach the line and read the predicted price.  
However, fitting a curve to the same data could give a different price.  
For the house of size 750 shown here, the straight line and the curve make different predictions.  
We should choose a model that works well for new houses, rather than picking the higher price because it benefits our friend.  
Predicting the magnitude of a numerical quantity, such as price or temperature, is called regression.  
Later, we will define a cost function as a way to compare which model is better.  

## Slide 11 | W1 | Source page 14

We have just predicted a number: a price.  
Now we will look at classification, which predicts which category something belongs to.  
Watch how the nature of the answer we want changes, rather than focusing only on the model's input.  

## Slide 12 | W1 | Source page 15

This example classifies a tumor as benign or malignant from its size.  
Here, benign tumors have the label 0 and malignant tumors have the label 1.  
The horizontal axis shows tumor size, and the vertical axis has only the two values 0 and 1.  
We want to predict one of two categories, rather than a continuous quantity such as a price.  
The lower diagram places the same examples on one line and distinguishes their labels with circles and crosses.  
The information previously shown by vertical position is now represented by the kind of symbol, so the data has the same meaning.  
Given a new patient's tumor size, we can use the learned relationship to predict its category.  
For understanding the concept, this example simplifies the input to size alone.  

## Slide 13 | W1 | Source page 16

Classification does not always mean choosing between only two types.  
We might distinguish three categories, such as benign, malignant type 1, and malignant type 2.  
We could also classify objects in photographs as cats, dogs, cars, and other types.  
Assigning numbers to categories gives them convenient names for computation.  
Writing them as 0, 1, and 2 does not create an intermediate category called 1.5.  
Therefore, the fact that a result is written as a number is not enough to call the problem regression.  
Check whether the number represents the magnitude of a quantity or the name of a distinct category.  

## Slide 14 | W1 | Source page 17

If tumor size alone does not distinguish the categories well, we can use other information too.  
Here, age has been added as a second input.  
Each point represents a patient, and its coordinates give that patient's tumor size and age.  
Patients with the same tumor size but different ages appear at different positions on the graph.  
The algorithm finds a boundary in the data that separates the circles from the crosses.  
We can classify a new patient by plotting the two values and checking which side of the boundary they fall on.  
Drawing two axes does not mean we can use at most two inputs.  
With more inputs, the data becomes harder to draw, but the principle of computing with several pieces of information stays the same.  

## Slide 15 | W1 | Source page 18

Both problems we have seen so far provide inputs and correct answers during training.  
That shared property makes both of them supervised learning.  
Predicting a numerical quantity, such as a house price, is regression.  
Choosing a predefined category, such as benign or malignant, is classification.  
For example, a photograph can be an input for regression if we predict age, or for classification if we predict whether it shows a person or an animal.  
The distinction depends on what output we request, rather than what the input looks like.  
Keeping this criterion in mind makes it easier to decide what kind of model a new problem needs.  

## Slide 16 | W1 | Source page 19

Now we will move to a situation with inputs but no correct-answer labels.  
Does having no answer key mean we cannot learn anything?  
We can still find similarities and differences among the examples.  

## Slide 17 | W1 | Source page 20

In the supervised-learning examples, each training example came with an answer to predict.  
If we hide those answers and keep only the inputs, we have the situation we will study next.  
Some inputs may be similar to one another, while others may be far from the rest.  
Unsupervised learning analyzes those relationships to find structure.  
It means there is no answer key, not that the computation has no criteria or human design.  

## Slide 18 | W1 | Source page 21

On the left, the circles and crosses tell us which category each example belongs to.  
On the right, we have only size and age, so we do not know whether an example is benign or malignant.  
Even so, we can see that the points form several groups rather than spreading evenly across the space.  
Grouping similar examples is called clustering.  
Instead of a person specifying that a particular point must belong to the first group, the method uses relationships in the data to form groups.  
We must separately interpret what the discovered groups mean.  
Finding two groups does not immediately let us call one benign and the other malignant.  
Discovering groups and predicting predefined disease labels are different tasks.  

## Slide 19 | W1 | Source page 22

Several news organizations can report the same event with different headlines and wording.  
Articles about a panda giving birth to twins might share words such as panda, zoo, and cubs.  
Grouping articles with similar descriptions lets users see several reports of the same event together.  
News topics change daily, so it is difficult for a person to define every topic in advance.  
Clustering can use similarities among that day's incoming articles to discover groups.  
In practice, we would not automatically decide that two articles cover the same story just because they share a word.  
Other information and the similarity of their overall descriptions can also be considered.  
The key here is that the groups are formed from relationships among examples without first providing a list of correct article groupings.  

## Slide 20 | W1 | Source page 23

In this diagram, each column represents a person and each row represents a gene.  
The color of each cell indicates how actively that gene is expressed.  
Each person is represented by the activity pattern of many genes, rather than by just one or two numbers.  
Grouping columns with similar color patterns can reveal groups of people with similar characteristics.  
We have not defined type names in advance and asked the algorithm to predict them.  
We are exploring whether the measurements contain repeated structure.  
This illustrates how comparing collections of numbers can uncover useful patterns even when their meaning is initially unclear.  

## Slide 21 | W1 | Source page 24

People taking the same AI course may have different goals.  
Some want practical skills, while others are preparing for a career change or trying to understand recent technology.  
Analyzing users' interests or behavior and grouping similar people can help us consider what resources each group needs.  
For example, someone who wants to implement a model may need different resources from someone seeking an overview.  
We can look for these groups in the patterns without first labeling every person's goal.  
This does not mean that real people separate perfectly into a few fixed types.  
A group is one way of representing data to help us understand it for a particular purpose.  
For now, focus on the process of finding shared features and forming groups without an answer key.  

## Slide 22 | W1 | Source page 25

We have examined clustering as an example of unsupervised learning.  
But grouping is not the only thing we can do with data that has no answer key.  
We will look at two other common purposes as well.  

## Slide 23 | W1 | Source page 26

Clustering collects similar examples into groups.  
Anomaly detection looks for examples that are unusually different from others.  
For example, it can identify an unusual payment pattern for additional review.  
An unusual event is not necessarily wrong, but identifying it helps us decide where to investigate.  
Dimensionality reduction reduces the number of values used to represent data.  
It expresses many measurements using fewer numbers while trying to preserve important structure.  
Think of compressing a photograph into a shorter description that retains information useful for computation or visualization.  
These methods have distinct purposes: finding groups, finding unusual examples, and reducing a representation; they are not grouped merely because their names sound similar.  

## Slide 24 | W1 | Source page 27

For each example, first check whether correct answers are provided along with the inputs.  
The first example learns from emails already marked as spam or ordinary email, so it is supervised learning.  
The second provides articles and asks the system to group reports of the same event, so it is unsupervised learning.  
The third also asks the system to discover customer groups, so it is unsupervised learning.  
The last provides diabetes diagnoses as correct answers, so it is supervised learning.  
The answers to this question are therefore the second and third examples.  
Even with the same email or patient data, the approach can change depending on what information we provide and what we ask the system to do.  

## Slide 25 | W1 | Source page 29

Now we will move from broad categories to the first model we will actually calculate.  
Linear regression represents the relationship between an input and an output with a straight line.  
It is a simple model, but it is useful for learning the difference between prediction and training, and how to reduce error.  
We will keep using these principles when we build much more complex models later.  

## Slide 26 | W1 | Source page 30

Imagine that you are helping a client who wants to sell a house.  
Collecting house sizes and prices from past transactions gives the red points on the screen.  
Find a house's size on the horizontal axis and read its sale price on the vertical axis.  
For a house that has not yet sold, we do not know the price, so we must estimate it from the pattern in earlier examples.  
After fitting a straight line, the height of the line at size 1,250 gives a prediction of about $220,000.  
This is the current model's prediction, rather than the actual sale price itself.  
Different data or a different line could produce a different prediction.  
Because actual sale prices were used as correct answers during training, this is supervised learning.  
Because the output is a numerical price, it is specifically regression.  

## Slide 27 | W1 | Source page 31

We will look at the same data as a graph and a table side by side.  
The first row on the right describes a house with size 2,104 and price 400.  
Finding the point at horizontal coordinate 2,104 and vertical coordinate 400 on the left identifies the same house.  
Prices are in thousands of dollars, so 400 means $400,000.  
If the table contains 47 rows, the graph also contains 47 transaction examples.  
A table helps us check exact values, while a graph helps us see the overall trend and unusual examples.  
When the computer performs calculations, it mainly works with values in this table-like form.  
We will also draw those values to understand what the calculations mean.  

## Slide 28 | W1 | Source page 32

The collection of examples a model uses to learn is called the training set.  
The input x is a feature, and the value y that we want to predict is the target.  
In this table, x is house size and y is sale price.  
The symbol m represents the number of examples, so here it is 47.  
One example is written as the pair (x,y).  
To distinguish which example we mean, we add a parenthesized superscript i.  
The input x⁽²⁾ comes from the second row and is 1,416, while y⁽²⁾ is the price 232 in that same row.  
Here, (2) is a row number rather than an exponent.  
Check the parentheses so that you do not confuse x² with x⁽²⁾.  
Although the notation may look unfamiliar, it is simply a convention for pointing precisely to a particular value in the table.  

## Slide 29 | W1 | Source page 33

Now that we know what training data is, we will look at what training produces.  
Providing data does not simply produce more data: it produces a model that can answer new inputs.  
We will represent that model by a function f.  

## Slide 30 | W1 | Source page 34

The training set at the top contains both inputs and correct answers.  
The learning algorithm uses those examples to adjust the relationship between inputs and outputs, producing a model f.  
At the bottom, we give the model only the size x of a new house.  
The predicted price it returns is written ŷ and read as y hat.  
The value y is the actual answer and ŷ is the model's estimate, so they may agree or differ.  
For now, we will write the model as f(x)=wx+b.  
Once we choose an x, we can substitute it into this expression to calculate a prediction.  
Changing w and b changes the line and therefore changes the prediction for the same house.  
Training is the process of finding these two values so the model fits the data well.  
The w,b written below f identify which parameters the function uses; omitting them still refers to the same model.  
Because this model uses one input, house size, it is also called univariate linear regression.  

## Slide 31 | W1 | Source page 35

We can now construct a line, but we have not yet decided which line to choose.  
We need to turn the judgment that a line looks reasonable into a number a computer can use.  
A cost function evaluates how well a model fits the data.  
From here on, we will adjust the model in a direction that lowers this score.  

## Slide 32 | W1 | Source page 36

The x and y values in the table are the data we observed.  
By contrast, w and b in the equation are values the model can adjust during training.  
These adjustable values are called parameters.  
Even for the same house size, different values of w and b produce different predicted prices.  
Think of them as two controls for adjusting the line.  
One tilts the line, and the other changes the height of the entire line.  
During training, we do not alter the actual sale prices y to fit the model.  
We change the parameters to bring predictions closer to the given data.  
The next diagram shows exactly what each of these two values does.  

## Slide 33 | W1 | Source page 37

On the left, w=0 and b=1.5, so f(x)=0×x+1.5.  
Whether x is 0 or 2, the prediction is always 1.5, giving a horizontal line.  
In the middle, w=0.5 and b=0, so f(x)=0.5x.  
It predicts 0 at x=0 and 1 at x=2.  
The prediction increases by 0.5 whenever x increases by 1, so the slope is 0.5.  
The right-hand model adds b=1 while keeping the same w as the middle model.  
Every prediction is therefore 1 larger, and the entire line moves upward by 1.  
Since f(0)=b, the value b gives the point where the line meets the vertical axis.  
Adjusting the slope w and the height b separately lets us construct many different lines.  
Next, we will evaluate which of those lines fits the data better.  

## Slide 34 | W1 | Source page 38

The red points show actual values y, while a value on the blue line at the same x is the prediction ŷ.  
First, subtract the actual value from the prediction to calculate the error ŷ−y.  
It is positive when the line lies above the point and negative when the line lies below it.  
This difference is the vertical gap in the diagram, not the shortest diagonal distance from a point to the line.  
Adding raw errors could allow a prediction that is 2 too high to cancel a prediction that is 2 too low.  
We therefore square each error before adding them.  
Squaring removes the sign and gives a larger penalty to examples with larger mistakes.  
The Σ from i=1 to m means to perform the same calculation for every example and collect the results.  
Dividing by m gives MSE, the mean of the squared errors.  
This course's cost J(w,b) multiplies that by 1/2, so it is precisely half the MSE.  
For example, if two examples have errors of 1 and −1, the MSE is 1 and J is 0.5.  
The factor 1/2 simplifies the derivative later, without changing which w and b are best.  
We can now calculate one score for the entire dataset whenever we choose a line.  

## Slide 35 | W1 | Source page 39

We have read the cost formula, but how its number relates to the model's shape may still feel unfamiliar.  
We will connect the two by substituting values into a small dataset ourselves.  
On one side, we will look at the prediction line; on the other, we will look at the score evaluating that line.  

## Slide 36 | W1 | Source page 40

The left-hand expression is the original model f(x)=wx+b, where both w and b can change.  
On the right, we fix b at 0 to simplify the diagram.  
The model becomes f(x)=wx, leaving only w to adjust.  
Substituting x=0 always gives 0, so all these lines pass through the origin.  
Changing w now changes only the slope of the line.  
Recalculating the errors on the same data gives the J(w) corresponding to that w.  
The w written below minimize indicates which value we will change to reduce the cost.  
It means we will keep x and y fixed as the evaluation data and change only w.  
Returning to the original problem, we adjust both parameters together, so both w and b appear below minimize.  

## Slide 37 | W1 | Source page 41

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

## Slide 38 | W1 | Source page 42

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

## Slide 39 | W1 | Source page 43

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

## Slide 40 | W1 | Source page 44

We can now read the choice of a good w from the right-hand graph.  
The lowest point is at w=1, where the cost is 0.  
For this dataset, a line passes through all three points exactly, so a cost of 0 is possible.  
In real data, all points may not lie on a single line, so the minimum cost may be greater than 0.  
The expression minimize_w J(w) asks us to find the smallest achievable cost, rather than requiring us to make it 0.  
If b can also change, we compare combinations of slope and height.  
We write that objective as minimize_{w,b} J(w,b).  
The problem of finding good parameters is now defined numerically.  

## Slide 41 | W1 | Source page 45

When only w could change, one horizontal axis could represent all candidates.  
Now we will remove the restriction that fixed b at 0 and return to the original model.  
Changing both the slope and height of the line also requires more axes for drawing the cost.  

## Slide 42 | W1 | Source page 46

Connect the model, parameters, cost, and objective in order.  
The model f(x)=wx+b calculates a prediction from an input.  
The values w and b are the quantities we can change.  
The cost J(w,b) evaluates how far those predictions are from the actual data.  
The objective is to find the combination of w and b with the smallest cost.  
For example, increasing b while keeping the slope fixed raises every prediction together.  
We decide whether that change is helpful by checking whether the gaps from the actual values shrink overall.  
Changing a parameter and reducing the cost therefore do not mean the same thing.  

## Slide 43 | W1 | Source page 47

The left-hand model has w=0.06 and b=50, giving f(x)=0.06x+50.  
For a house size of 1000, it predicts 110, or $110,000.  
Compared with the actual points, it predicts most prices too low.  
Calculating all the errors for this line gives one score, J(0.06,50).  
Previously, choosing w alone was enough; now both w and b must be specified to determine a score.  
The function f on the left takes house size x as input, while J on the right takes the model's parameters as input.  
Although both are functions, what goes into them and what comes out are different.  
Representing every combination of two parameters requires positions on a plane, with cost shown as height above that plane.  

## Slide 44 | W1 | Source page 48

One axis on the floor represents w, and the other represents b.  
Choosing one position on that floor is equivalent to choosing one pair of parameters.  
Moving upward from that position until we meet the surface gives the height J(w,b).  
The displayed w=−10 and b=−15 are simply one example of such a combination.  
The surface dips toward the middle like a bowl or a hammock.  
High positions represent models that fit the data poorly, while low positions represent better fits.  
Training aims to move the floor coordinates to find low parts of this surface.  
Moving downward here means lowering the cost, rather than always lowering predicted house prices.  
Also distinguish the slope of the prediction model from the slope of the cost surface.  

## Slide 45 | W1 | Source page 49

A 3D surface helps us understand the overall landscape.  
However, some areas can be hidden behind others, and comparing several positions precisely can be awkward.  
If we represent heights with lines, we can view the same information on a plane.  
This is a contour plot, using the same principle as the contour lines on a familiar map.  

## Slide 46 | W1 | Source page 50

Imagine cutting a mountain horizontally at a fixed height.  
Connecting the outline where that slice meets the mountain surface produces the red line.  
Every position on that line has the same height, whether it is to the east or west.  
Changing the slicing height produces another line.  
Drawing these lines together shows how the mountain's height changes.  
The essential idea is not that the lines are circular, but that each line connects points of equal height.  

## Slide 47 | W1 | Source page 51

This time we are looking down at the same mountain from above.  
We can read the landscape from its contours even without drawing height directly on a vertical axis.  
If successive contours represent equal height differences, closely spaced lines indicate that height changes quickly over a short distance.  
Widely spaced lines indicate a gentler slope.  
The center of a mountain may be high, but the center of the next cost plot is low.  
Do not decide whether a position is high or low merely because it is central; check which function the contours represent.  

## Slide 48 | W1 | Source page 52

The left-hand plot shows predictions as a line against input x, while the upper-right plot shows cost contours against w and b.  
The 3D diagram below shows the same cost as the upper-right plot from another direction.  
Points on one contour have the same J even when their w and b differ.  
Consequently, two different lines on the left can receive the same overall evaluation score.  
One line might make larger mistakes on small houses and another on large houses, while their average scores match.  
Equal costs do not mean equal predictions.  
In this diagram, inner contours represent lower costs.  
Parameters near the center produce lines that fit the data better.  
The lower diagram looks stretched sideways because of its axis ranges and viewing angle; it represents the same bowl-shaped landscape.  

## Slide 49 | W1 | Source page 53

Now we will choose specific parameters and examine how the prediction line relates to its cost.  
First compare the line and data points on the left, then locate those parameters on the right.  
Connect the three diagrams as different views of one model, rather than three separate experiments.  

## Slide 50 | W1 | Source page 54

Here w=−0.15 and b=800, so the predicted price decreases as x increases.  
However, the actual data generally shows larger houses selling for higher prices.  
This produces predictions that are too high for small houses and too low for large houses.  
For example, the prediction is 650 at x=1000 and 350 at x=3000.  
The blue vertical gaps are large for many points.  
The cost is half the mean of these squared errors, which is large in this case.  
In the upper-right plot, horizontal coordinate −0.15 and vertical coordinate 800 identify this model.  
Here, the vertical coordinate 800 is b rather than cost; cost must be read from the contour's value.  

## Slide 51 | W1 | Source page 55

This time, we change the parameters to w=0 and b=360.  
The model is f(x)=360, predicting $360,000 for every house.  
It ignores differences between small and large houses, but its overall cost is lower than that of the previous incorrectly tilted line.  
That does not mean every individual prediction has improved.  
It means the model receives a better score when we collect and evaluate all the errors.  
The selected point on the right is (w,b)=(0,360).  
It has not yet reached the center of the contours, so better combinations are still available.  

## Slide 52 | W1 | Source page 56

The equation is now f(x)=−0.15x+500.  
Compared with the previous example with w=−0.15, the slope is unchanged and the entire line has moved downward.  
However, this does not solve the problem that the data trends upward.  
Lowering a line and lowering its cost are different actions.  
If a prediction is already below its target, lowering it further increases the error.  
Rather than only noticing that a value moved, recalculate the gaps from the actual values.  
The cost graph summarizes the overall result as one score.  

## Slide 53 | W1 | Source page 57

Here w=0.13 and b=71, so the line follows the increasing trend in the data.  
For example, it predicts 201 at size 1000 and 331 at size 2000.  
Many data points lie relatively close above or below the line.  
Not every error is 0, but the overall cost is lower than for the earlier candidates.  
The corresponding point on the right therefore lies near the center of the contours.  
When real observations are scattered, we cannot find a line that passes through every point.  
We choose the available line that best satisfies the chosen evaluation criterion.  
So far, a person has selected w and b, but this becomes inefficient when there are many candidates.  
Next, we will learn to calculate how to move automatically toward a better choice.  

## Slide 54 | W1 | Source page 58

So far, we have manually chosen several w and b values and compared their costs.  
Now we will calculate which direction to change the current values to improve the result.  
Repeating that calculation is the method called gradient descent.  
We will learn it for linear regression, but the same basic principle is used later to train neural networks.  

## Slide 55 | W1 | Source page 59

First, choose starting values for w and b.  
For the linear regression we are studying, both can start at 0.  
The initial model is then a horizontal line that predicts 0 for every input.  
We calculate the direction in which its cost decreases and move the parameters a little.  
The situation has changed at the new position, so we calculate the direction again.  
Repeating this process approaches a place where further movement hardly reduces the cost.  
With several features, there are more values to adjust, such as w₁ and w₂, but the principle is unchanged.  
The goal is to make the cost calculated from the parameters small, rather than to make the parameters themselves small.  
The shape of the cost affects which positions can be reached and how training behaves.  

## Slide 56 | W1 | Source page 60

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

## Slide 57 | W1 | Source page 61

We will express the downhill direction and step size mathematically.  
Although a new derivative symbol appears, first notice the structure of subtracting a correction from the current value.  
Before memorizing the notation, read the expression in parts and identify each part's role.  

## Slide 58 | W1 | Source page 62

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

## Slide 59 | W1 | Source page 63

We will check why the update expression contains a minus sign.  
If we temporarily fix b, we can plot w and J(w) on a plane.  
Follow the tangent slope to see which direction the expression actually moves us.  

## Slide 60 | W1 | Source page 64

Think of a straight line tangent to the cost curve at the current position.  
The slope of that tangent is the derivative.  
Its sign tells us whether cost increases or decreases when w increases slightly.  
Its magnitude indicates how sensitively cost responds to the same small change.  
The learning rate α is the step-size control multiplied by this information.  
The actual movement is determined by the product of α and the derivative, rather than by α alone.  
The slope here belongs to the cost curve, and has a different role from w, which we previously called the slope of the prediction line.  
We calculate the cost's slope in order to adjust the model's slope w.  

## Slide 61 | W1 | Source page 65

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

## Slide 62 | W1 | Source page 66

Even in the correct direction, moving too far at once can take us past our destination.  
We will examine how the learning rate affects training.  
A small value is not always better, and a large value is not always faster.  

## Slide 63 | W1 | Source page 67

If α is too small, as in the upper diagram, the correction obtained by multiplying the derivative is also tiny.  
The cost decreases, but reaching the minimum requires many iterations.  
Conversely, if α is too large, one update can jump across the valley.  
Even if we change direction at the new position, another large jump can take us to a higher point on the opposite side.  
The cost may then increase or keep oscillating instead of decreasing.  
Approaching the minimum steadily is called convergence.  
Moving farther away is called divergence.  
Crossing the minimum once does not necessarily mean failure, but if the cost keeps increasing, check α.  
What matters is the actual change in cost, rather than simply having a large step.  

## Slide 64 | W1 | Source page 68

What will the next update do if we have already reached the local minimum in this diagram?  
At a smooth valley floor like this, the tangent is horizontal, so the derivative is 0.  
Multiplying that 0 by α gives a correction of 0.  
In the example on the screen, w=5 and α=0.1 give 5−0.1×0=5.  
Remaining at the same position is the desired behavior here.  
However, a derivative of 0 by itself does not identify a minimum for every possible function.  
This slide explains why the update stops when it is at a valley floor.  

## Slide 65 | W1 | Source page 69

You might think α must also be reduced each time we approach the minimum.  
In this diagram, however, the movement becomes smaller naturally even with α fixed.  
The initial steep region has a large derivative, which produces a large correction.  
As we descend toward the floor, the tangent becomes gentler and the derivative's magnitude decreases.  
Multiplying by the same α therefore gives a smaller result.  
The learning rate and the actual step size are thus different quantities.  
An appropriate fixed α can approach the minimum through progressively smaller movements.  
This does not mean that an excessively large α will correct itself, so remember the earlier conditions too.  

## Slide 66 | W1 | Source page 70

So far, we have examined the model, cost, and gradient descent separately.  
Now we will differentiate the linear-regression cost and substitute the result into the update rule.  
Connecting these three parts lets us provide data and train a model.  

## Slide 67 | W1 | Source page 71

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

## Slide 68 | W1 | Source page 72

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

## Slide 69 | W1 | Source page 73

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

## Slide 70 | W1 | Source page 74

A general cost function may have several valleys, as in the diagram.  
Because gradient descent uses the slope around its current position, different starting points can lead to different destinations.  
Entering one valley does not guarantee that it is better than every other candidate.  
That is why we distinguished a local minimum from a global minimum.  
Should we worry about the same problem in the linear regression model we just built?  
The answer depends on the cost used with the model, rather than only on the model's name.  

## Slide 71 | W1 | Source page 75

Combining linear regression with the current MSE-based cost gives a function that is convex in its parameters.  
Think of a bowl that curves downward into its center, as in the diagram.  
The important property is that it does not have separate, worse local minima to get trapped in.  
With an appropriate learning rate, we can approach a global minimum.  
Depending on the data, the minimum cost may be 0 or positive.  
Successful training means finding good values within the chosen model and cost function.  
It does not mean that every real relationship is a straight line, or that the model will predict new data perfectly.  
We will return to that distinction when evaluating model performance later.  

## Slide 72 | W1 | Source page 76

Now we will follow training on the house-price data.  
The left-hand plot shows the prediction line, while the upper-right and lower plots show two representations of the same cost.  
Watch the new line and point added on each slide to see what one update changes.  
Earlier lines remain as traces that let us compare previous states.  

## Slide 73 | W1 | Source page 77

To make the changes visible, this example starts at w=−0.1 and b=900.  
We could normally start at 0, but here we have deliberately chosen a poor fit.  
The initial line lies above most house prices and slopes downward as size increases.  
The point on the right gives the (w,b) position corresponding to that line.  
The height of the lower surface is the cost calculated with the same parameters.  
We will now keep the data fixed and change only the parameters.  

## Slide 74 | W1 | Source page 78

One update adds the orange prediction line.  
It is closer to the data overall than the previous line, and the cost decreases.  
The new point on the right gives the w and b that determine this new line.  
The displayed cost falls from about 77,237 to about 45,401.  
The line changes on one side and the point moves on the other, but both are results of the same update.  

## Slide 75 | W1 | Source page 79

We calculate the derivatives again at the new parameters and move to the next step.  
The green line is added, and the cost falls to about 29,109.  
Predictions for individual houses do not all improve by the same proportion.  
We check whether the cost calculated over all the examples has decreased.  
The line still points in a different direction from the data's trend, so there is more to learn.  

## Slide 76 | W1 | Source page 80

Adding the red line also changes the difference between predictions for large and small houses.  
Changing b alone moves every prediction up or down by the same amount.  
If w changes as well, the prediction change depends on x.  
Here we adjust both parameters to move to a lower cost.  
The connected points on the right trace the path of parameter values selected so far.  

## Slide 77 | W1 | Source page 81

The new line is less steep than the previous one.  
We are gradually correcting the initial negative slope, which did not fit the data.  
The new point also moves lower on the cost surface below.  
We do not judge the line as better merely because it looks less steep.  
We check that the overall cost relative to the actual values also decreases.  

## Slide 78 | W1 | Source page 82

The line has now become almost horizontal.  
A horizontal line is not the goal; this is an intermediate state on the way to a better line.  
An almost horizontal line predicts similar prices for houses of different sizes.  
However, the data has an increasing trend with size, so further improvement is possible.  
Continue the updates while watching whether the cost on the right keeps decreasing.  

## Slide 79 | W1 | Source page 83

With further updates, an upward-sloping line appears.  
The model now predicts higher prices for larger houses.  
No person separately instructed it to make w positive.  
This is the result of following errors and derivatives calculated from the data.  
Here, saying that training reflects the relationship in the data means this change in the parameters.  

## Slide 80 | W1 | Source page 84

The new lines are approaching the central trend in the data.  
The point on the right is also moving closer to the center of the contours.  
Near the center, there is less opportunity to reduce the cost by a large amount.  
Changes from additional updates may therefore become smaller.  
Watching this progress helps us decide whether to stop or continue training.  

## Slide 81 | W1 | Source page 85

We will use the final line to predict the price of a new house.  
Find size 1,250 on the horizontal axis and read the height where it meets the current prediction line.  
The diagram gives about $250,000.  
This differs from the earlier prediction made by another line because the parameters are different.  
We still do not know the actual sale price, but we have applied the learned relationship to a new input.  
Finding the parameters is training, and calculating f(x) using those parameters is prediction.  

## Slide 82 | W1 | Source page 86

The derivative expressions so far have used every example, from i=1 to m, on each step.  
Using the entire training set for one update is called batch gradient descent.  
With 47 examples, we collect information from all 47 to obtain one correction.  
Distinguish this from updating after looking at just one example.  
Other methods use only part of the data, but for now we will learn the principle using the full dataset.  
We have completed the sequence of predicting with a line, evaluating with a cost, and improving it through gradient descent.  
Next, we will increase the number of inputs and perform the same calculations more efficiently.
