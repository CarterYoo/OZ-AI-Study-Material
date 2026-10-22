# MLS Course 1 Detailed English Speaker Notes

English translation of the detailed Korean teaching script based on the annotated source slides and official lesson sequence.
The translation retains the notation, worked examples, visual relationships, questions, and lesson transitions.
This is an instructional adaptation, not a verbatim transcript translation.
Slide numbers follow the classroom Google Slides deck. Each spoken sentence has its own line.

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
