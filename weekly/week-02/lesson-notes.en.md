# Week 02 / Machine Learning Foundations

English teaching notes matched to the OZ classroom slide order.
The explanations are instructional adaptations, not verbatim lecture transcripts.

## Canva page 9 / ML source slide 1 / Welcome to Machine Learning

We will start with how machine learning solves problems.
The name may be unfamiliar, but you already use this technology when you see search results or receive video recommendations.
Other examples include voice input that turns a friend's speech into text and tools that filter spam email.
To build these features, would a person have to write a rule for every possible situation?
Voices, photographs, and sentences have too many possible variations for that approach to work well.
In machine learning, we provide examples and let a system find useful relationships in them.
We will learn this process using data we can see directly, such as house sizes and prices.
Connect the steps: what information goes in, what we predict, and what changes when a prediction is wrong.
Our goal is for you to implement this process in code by the end.

Source slide 1: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p2
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 10 / ML source slide 2 / Learning to Recognize Spam

Imagine receiving an email saying you have won a large cash prize.
The message sounds welcome, but its sender or wording may look suspicious.
An email service can automatically place this kind of message in the spam folder.
The input we give the computer is an email, and the answer we want is whether it is spam.
A person could write a rule that always marks a particular word as spam, but ordinary emails may contain that word too.
A simple rule also has limits because a small change in wording can get around it.
Instead, we use examples of spam and ordinary email to learn patterns that help distinguish them.
After training, we apply those patterns to an email that has not yet been classified.
Remember this sequence: learn relationships from examples, then use them on new inputs.

Source slide 2: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p4
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 11 / ML source slide 3 / Machine Learning Applications

Machine learning is used in more than email and recommendation services.
Factories can inspect product photographs for defects, and farms can use observations to examine crop conditions.
It is also used to analyze medical images and manage energy production more efficiently.
These problems share a feature: people can describe what they want, but writing every decision rule in code is difficult.
That is why learning rules from data is useful.
However, being able to run an algorithm does not guarantee a good result.
We also need to know which data to use, what to treat as the correct answer, and what to check first when performance is poor.
This course will cover both the principles of the algorithms and ways to make them work in practice.

Source slide 3: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p5
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 12 / ML source slide 4 / What Is Machine Learning?

Having seen several applications, we will define machine learning more precisely.
The key question is whether a computer can improve its performance through experience, rather than whether it thinks like a person.
We will use a game to compare this with a program whose rules are all specified in advance.

Source slide 4: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p6
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 13 / ML source slide 5 / Learning from Experience

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

Source slide 5: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p7
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 14 / ML source slide 6 / A Map of Machine Learning

We will first look at a broad map of the methods we will encounter.
Supervised learning learns from inputs paired with correct answers.
Unsupervised learning looks for structure or patterns in data without an answer key.
Recommender systems and reinforcement learning are also important topics, but for now we will distinguish the first two.
You do not need to memorize all the algorithm names at once.
When you encounter a problem, start by asking whether correct answers are available and what you want to predict.
Knowing an algorithm and applying it well are also different abilities.
Owning a hammer and a drill does not immediately enable you to build a house.
You also need to learn how to choose a tool, check its result, and find the cause of a problem.

Source slide 6: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p9
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 15 / ML source slide 7 / Supervised Learning

We will first look more closely at supervised learning.
Think of studying examples that include both questions and their correct answers.
We will begin by telling the computer which part is the question and which part is the answer.

Source slide 7: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p10
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 16 / ML source slide 8 / Learning from Inputs and Labels

We will write an input as x and its corresponding correct answer as y.
In email classification, x is the email and y indicates whether it is spam.
During training, we provide more than emails: we also identify which messages are spam and which are ordinary email.
The algorithm examines many pairs of x and y to find their relationship.
The name for this correct-answer information is a label.
An important point is that the information available during training differs from what is available when we use the model.
During training, it learns relationships by seeing the answers; in actual use, it does not know the answer for a new input.
Learning is useful only if the system can predict an appropriate y from an x it has not seen before.
Simply storing the answers to the examples would not solve new problems.

Source slide 8: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p11
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 17 / ML source slide 9 / Examples of Supervised Learning

For each row of the table, first identify the input and its matching output.
Speech recognition takes sound as input and produces text representing that sound.
Translation takes a sentence in one language and produces a sentence in another.
In advertising, we can use an advertisement and information about a user to predict whether the user will click.
To understand a vehicle's surroundings, camera and sensor information can help estimate where other cars are.
In product inspection, the input is a product photograph and the output indicates whether a defect is present.
Neither the input nor the output has to be a single number.
They can take forms such as sentences, images, or positions, but eventually we represent them in a form the model can process.
Although these problems look different, they all learn relationships between inputs and outputs from examples with known answers.

Source slide 9: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p12
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 18 / ML source slide 10 / Regression Predicts Numbers

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

Source slide 10: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p13
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 19 / ML source slide 11 / Classification

We have just predicted a number: a price.
Now we will look at classification, which predicts which category something belongs to.
Watch how the nature of the answer we want changes, rather than focusing only on the model's input.

Source slide 11: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p14
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 20 / ML source slide 12 / Predicting One of Two Classes

This example classifies a tumor as benign or malignant from its size.
Here, benign tumors have the label 0 and malignant tumors have the label 1.
The horizontal axis shows tumor size, and the vertical axis has only the two values 0 and 1.
We want to predict one of two categories, rather than a continuous quantity such as a price.
The lower diagram places the same examples on one line and distinguishes their labels with circles and crosses.
The information previously shown by vertical position is now represented by the kind of symbol, so the data has the same meaning.
Given a new patient's tumor size, we can use the learned relationship to predict its category.
For understanding the concept, this example simplifies the input to size alone.

Source slide 12: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p15
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 21 / ML source slide 13 / Classification with More Classes

Classification does not always mean choosing between only two types.
We might distinguish three categories, such as benign, malignant type 1, and malignant type 2.
We could also classify objects in photographs as cats, dogs, cars, and other types.
Assigning numbers to categories gives them convenient names for computation.
Writing them as 0, 1, and 2 does not create an intermediate category called 1.5.
Therefore, the fact that a result is written as a number is not enough to call the problem regression.
Check whether the number represents the magnitude of a quantity or the name of a distinct category.

Source slide 13: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p16
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 22 / ML source slide 14 / Using More than One Input

If tumor size alone does not distinguish the categories well, we can use other information too.
Here, age has been added as a second input.
Each point represents a patient, and its coordinates give that patient's tumor size and age.
Patients with the same tumor size but different ages appear at different positions on the graph.
The algorithm finds a boundary in the data that separates the circles from the crosses.
We can classify a new patient by plotting the two values and checking which side of the boundary they fall on.
Drawing two axes does not mean we can use at most two inputs.
With more inputs, the data becomes harder to draw, but the principle of computing with several pieces of information stays the same.

Source slide 14: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p17
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 23 / ML source slide 15 / Regression and Classification

Both problems we have seen so far provide inputs and correct answers during training.
That shared property makes both of them supervised learning.
Predicting a numerical quantity, such as a house price, is regression.
Choosing a predefined category, such as benign or malignant, is classification.
For example, a photograph can be an input for regression if we predict age, or for classification if we predict whether it shows a person or an animal.
The distinction depends on what output we request, rather than what the input looks like.
Keeping this criterion in mind makes it easier to decide what kind of model a new problem needs.

Source slide 15: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p18
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 24 / ML source slide 16 / Unsupervised Learning

Now we will move to a situation with inputs but no correct-answer labels.
Does having no answer key mean we cannot learn anything?
We can still find similarities and differences among the examples.

Source slide 16: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p19
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 25 / ML source slide 17 / From Labels to Unlabeled Data

In the supervised-learning examples, each training example came with an answer to predict.
If we hide those answers and keep only the inputs, we have the situation we will study next.
Some inputs may be similar to one another, while others may be far from the rest.
Unsupervised learning analyzes those relationships to find structure.
It means there is no answer key, not that the computation has no criteria or human design.

Source slide 17: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p20
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 26 / ML source slide 18 / Learning with and without Labels

On the left, the circles and crosses tell us which category each example belongs to.
On the right, we have only size and age, so we do not know whether an example is benign or malignant.
Even so, we can see that the points form several groups rather than spreading evenly across the space.
Grouping similar examples is called clustering.
Instead of a person specifying that a particular point must belong to the first group, the method uses relationships in the data to form groups.
We must separately interpret what the discovered groups mean.
Finding two groups does not immediately let us call one benign and the other malignant.
Discovering groups and predicting predefined disease labels are different tasks.

Source slide 18: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p21
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 27 / ML source slide 19 / Grouping News by Story

Several news organizations can report the same event with different headlines and wording.
Articles about a panda giving birth to twins might share words such as panda, zoo, and cubs.
Grouping articles with similar descriptions lets users see several reports of the same event together.
News topics change daily, so it is difficult for a person to define every topic in advance.
Clustering can use similarities among that day's incoming articles to discover groups.
In practice, we would not automatically decide that two articles cover the same story just because they share a word.
Other information and the similarity of their overall descriptions can also be considered.
The key here is that the groups are formed from relationships among examples without first providing a list of correct article groupings.

Source slide 19: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p22
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 28 / ML source slide 20 / Finding Groups in Gene Data

In this diagram, each column represents a person and each row represents a gene.
The color of each cell indicates how actively that gene is expressed.
Each person is represented by the activity pattern of many genes, rather than by just one or two numbers.
Grouping columns with similar color patterns can reveal groups of people with similar characteristics.
We have not defined type names in advance and asked the algorithm to predict them.
We are exploring whether the measurements contain repeated structure.
This illustrates how comparing collections of numbers can uncover useful patterns even when their meaning is initially unclear.

Source slide 20: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p23
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 29 / ML source slide 21 / Grouping Customers by Interests

People taking the same AI course may have different goals.
Some want practical skills, while others are preparing for a career change or trying to understand recent technology.
Analyzing users' interests or behavior and grouping similar people can help us consider what resources each group needs.
For example, someone who wants to implement a model may need different resources from someone seeking an overview.
We can look for these groups in the patterns without first labeling every person's goal.
This does not mean that real people separate perfectly into a few fixed types.
A group is one way of representing data to help us understand it for a particular purpose.
For now, focus on the process of finding shared features and forming groups without an answer key.

Source slide 21: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p24
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 30 / ML source slide 22 / Beyond Clustering

We have examined clustering as an example of unsupervised learning.
But grouping is not the only thing we can do with data that has no answer key.
We will look at two other common purposes as well.

Source slide 22: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p25
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 31 / ML source slide 23 / Clustering, Anomalies, and Compression

Clustering collects similar examples into groups.
Anomaly detection looks for examples that are unusually different from others.
For example, it can identify an unusual payment pattern for additional review.
An unusual event is not necessarily wrong, but identifying it helps us decide where to investigate.
Dimensionality reduction reduces the number of values used to represent data.
It expresses many measurements using fewer numbers while trying to preserve important structure.
Think of compressing a photograph into a shorter description that retains information useful for computation or visualization.
These methods have distinct purposes: finding groups, finding unusual examples, and reducing a representation; they are not grouped merely because their names sound similar.

Source slide 23: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p26
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 32 / ML source slide 24 / Which Problems Need Labels?

For each example, first check whether correct answers are provided along with the inputs.
The first example learns from emails already marked as spam or ordinary email, so it is supervised learning.
The second provides articles and asks the system to group reports of the same event, so it is unsupervised learning.
The third also asks the system to discover customer groups, so it is unsupervised learning.
The last provides diabetes diagnoses as correct answers, so it is supervised learning.
The answers to this question are therefore the second and third examples.
Even with the same email or patient data, the approach can change depending on what information we provide and what we ask the system to do.

Source slide 24: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p27
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 33 / ML source slide 25 / Linear Regression with One Feature

Now we will move from broad categories to the first model we will actually calculate.
Linear regression represents the relationship between an input and an output with a straight line.
It is a simple model, but it is useful for learning the difference between prediction and training, and how to reduce error.
We will keep using these principles when we build much more complex models later.

Source slide 25: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p29
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 34 / ML source slide 26 / Predicting House Prices

Imagine that you are helping a client who wants to sell a house.
Collecting house sizes and prices from past transactions gives the red points on the screen.
Find a house's size on the horizontal axis and read its sale price on the vertical axis.
For a house that has not yet sold, we do not know the price, so we must estimate it from the pattern in earlier examples.
After fitting a straight line, the height of the line at size 1,250 gives a prediction of about $220,000.
This is the current model's prediction, rather than the actual sale price itself.
Different data or a different line could produce a different prediction.
Because actual sale prices were used as correct answers during training, this is supervised learning.
Because the output is a numerical price, it is specifically regression.

Source slide 26: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p30
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 35 / ML source slide 27 / From a Plot to a Data Table

We will look at the same data as a graph and a table side by side.
The first row on the right describes a house with size 2,104 and price 400.
Finding the point at horizontal coordinate 2,104 and vertical coordinate 400 on the left identifies the same house.
Prices are in thousands of dollars, so 400 means $400,000.
If the table contains 47 rows, the graph also contains 47 transaction examples.
A table helps us check exact values, while a graph helps us see the overall trend and unusual examples.
When the computer performs calculations, it mainly works with values in this table-like form.
We will also draw those values to understand what the calculations mean.

Source slide 27: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p31
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 36 / ML source slide 28 / Reading Training Data Notation

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

Source slide 28: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p32
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 37 / ML source slide 29 / Using a Linear Regression Model

Now that we know what training data is, we will look at what training produces.
Providing data does not simply produce more data: it produces a model that can answer new inputs.
We will represent that model by a function f.

Source slide 29: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p33
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 38 / ML source slide 30 / Training a Model to Make Predictions

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

Source slide 30: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p34
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 39 / ML source slide 31 / The Cost Function

We can now construct a line, but we have not yet decided which line to choose.
We need to turn the judgment that a line looks reasonable into a number a computer can use.
A cost function evaluates how well a model fits the data.
From here on, we will adjust the model in a direction that lowers this score.

Source slide 31: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p35
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 40 / ML source slide 32 / The Two Parameters of a Line

The x and y values in the table are the data we observed.
By contrast, w and b in the equation are values the model can adjust during training.
These adjustable values are called parameters.
Even for the same house size, different values of w and b produce different predicted prices.
Think of them as two controls for adjusting the line.
One tilts the line, and the other changes the height of the entire line.
During training, we do not alter the actual sale prices y to fit the model.
We change the parameters to bring predictions closer to the given data.
The next diagram shows exactly what each of these two values does.

Source slide 32: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p36
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 41 / ML source slide 33 / Changing the Slope and Intercept

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

Source slide 33: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p37
Course: Andrew Ng, DeepLearning.AI, Stanford Online

## Canva page 42 / ML source slide 34 / The Squared Error Cost Function

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

Source slide 34: https://docs.google.com/presentation/d/1UQmTComnPEBzHNvITBWBa4iKPUHCRxiFNsufahSHrKE/edit#slide=id.p38
Course: Andrew Ng, DeepLearning.AI, Stanford Online
