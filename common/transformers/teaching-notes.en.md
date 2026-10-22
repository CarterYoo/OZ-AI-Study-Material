# Understanding Transformers from scratch

Speaker notes for learners beginning machine learning

Original slides
https://docs.google.com/presentation/d/1hai7WcMzf9eu7vCjgeS8ZYrka1Q8p3BEN9Pp4PLPO6Y/edit

Reference video
https://www.youtube.com/watch?v=11Z50mi8dSg&t=173s

These explanations were written for the slides. They are not a verbatim transcript of the video.

## 1. Understanding a Transformer from scratch

On-screen explanation

Turn text into numbers, calculate its context, and choose what comes next.

Speaker notes

Today we will follow a Transformer from its input to its output to see how it produces text.
In machine learning, a person does not write every rule by hand.
Instead, the system sees many examples and adjusts the numbers used in its calculations.
These numbers are called parameters or weights.
Training is the process of adjusting the weights; inference uses the weights already learned to calculate a result for a new input.

For example, the Korean fragment meaning "In the morning, I [bread]" naturally continues with "ate."
A language model calculates how likely different next pieces of text are.
It does not write the entire sentence in one step.
It chooses one small piece, appends that piece to the input, and calculates again.

You do not need to memorize an unfamiliar equation immediately.
Start by asking what goes in and what comes out.
The first curriculum session can focus on tokens and embeddings, the next on attention and internal calculations, and the following session on generating text.
This material covers that complete path.

Check question
How do training and inference differ?

Example answer
Training changes the weights; inference processes an input using the learned weights.

## 2. How does a language model such as ChatGPT work?

On-screen explanation

The output is a probability for each possible next token, rather than a completed sentence.

Speaker notes

First, think of a model as a program that takes an input and returns a calculated result.
The Transformer is the internal architecture of that program.
Here we study the GPT-style architecture that uses preceding text to predict the next token.
An actual conversational service adds further training and other features.

A token is a small piece of text.
It can be a word, part of a word, or punctuation.
The model receives a list of tokens and gives a score to every token that could come next.
When the scores are converted into probabilities, the probabilities across all candidates add up to 1, or 100%.
A taller bar in the graph on the right means that the model predicts that candidate with a higher probability.
The displayed candidates are only part of the complete vocabulary.

Parameters are the numbers a model adjusts during training.
Even the small GPT2 model uses about 124 million of them.
At four bytes per parameter, the weights alone occupy about 496 MB; running the model needs additional memory.
The amount of training text and the number of parameters measure different things.
The training-data figure in the original material has been corrected to approximately 40 GB of text, following the official published information.

Check question
If a token has a probability of 70%, does that mean its content has a 70% chance of being true?

Example answer
No.
It expresses how likely the model predicts that token is to come next.

Sources
https://openai.com/index/better-language-models/
https://openai.com/index/gpt-2-6-month-follow-up/

## 3. Turning text into tokens and IDs

On-screen explanation

A token is a piece of text; a token ID is the number assigned to that piece.

Speaker notes

Look at the changes in color on the left.
Each colored piece is one token.
Words separated by spaces and tokens identified by a model are not necessarily the same units.
A common word may be one token, while an unfamiliar word or Korean expression may be split into several pieces.
A space can also be grouped with the word after it.

The list of numbers below contains token IDs.
Like book numbers in a library, they are labels used to look up particular pieces.
Token 100 does not have twice as much meaning as token 50.
The model does not calculate with these IDs as though their numerical sizes were meaningful.
It uses the IDs to look up groups of numbers in the embedding table we will study later.

GPT2 and Mistral can produce different results for the same sentence because they use different tokenization rules and different ID tables.
Use the tokenizer links on the slide to enter a short English sentence and a Korean sentence.
The English example and function names shown in the code are actual runnable examples, so read them as written.

Check question
Does the same ID mean the same text in different models?

Example answer
Not necessarily.
You need to use the tokenizer and vocabulary that belong to that model.

## 4. Tokenizers and vocabularies

On-screen explanation

The vocabulary connects pieces of text with IDs.
It is different from the table that learns numerical representations.

Speaker notes

A vocabulary is a table of the tokens a model can use and the ID assigned to each one.
The cat, cattle, car, and carp examples on the right illustrate mapping text pieces to integers.
Those numbers are examples for explanation; they are not the actual GPT2 IDs.

The diagram on the left stores strings as branches that share common prefixes.
This data structure is called a trie.
The strings follow the same path through C and A, then branch according to the letters that follow.
For today, use it as a picture of which pieces are in the dictionary; you do not need to implement it.

GPT2 forms tokens using byte pair encoding, or BPE.
It merges smaller pieces that frequently occur together according to a predetermined order.
The tokenizer is prepared before training the language model and is usually kept fixed.
Distinguish this from the embedding table, whose numerical values change while the model trains.

Check question
Are the vocabulary and the embedding table the same table?

Example answer
No.
The vocabulary connects text pieces to IDs; the embedding table connects IDs to learned vectors.

## 5. A closer look at tokenizer details

On-screen explanation

Today we use the existing GPT2 tokenizer and focus on what its inputs and outputs mean.

Speaker notes

Let us look more closely at the previous diagram.
A trie can help find strings in a dictionary quickly.
However, choosing the longest string, as illustrated, is not the actual algorithm of every tokenizer.
GPT2's BPE follows a predefined priority order for merges.
Do not memorize these as the same procedure.

A tokenizer can contain special-purpose tokens in addition to ordinary text pieces.
One example is a token that marks a document boundary.
The available types differ between models.
In particular, GPT2's byte-based method does not necessarily need the usual token for an unknown word.
It can represent a new word using smaller pieces.

In the exercises, focus on loading the correct tokenizer, converting text into a list of IDs, and converting those IDs back into text.
Use this process to confirm that the model receives a list of integers rather than the string itself.
Implementing a tokenizer from scratch is not a required objective for today.

Check question
Does encountering an unfamiliar word necessarily make it impossible to enter that word?

Example answer
No.
The word can be represented by splitting it into smaller pieces.

## 6. Predicting the next token at each input position

On-screen explanation

During training, predict the next tokens at several positions together while hiding the future answers.

Speaker notes

Read the diagram from bottom to top.
The input is an ordered list of tokens, such as "The cat sat on the mat."
The box in the middle is the Transformer, and each vertical bar above it represents the output calculated at that position.
A bar represents a list of scores for the entire vocabulary, rather than one number.

The output at "The" predicts the next token.
The output at "cat" uses the text through "The cat" to predict what follows.
In this way, every position provides a next-token prediction problem.
Even when the entire training sentence is known, we block calculation paths that would let a position peek at the answer after it.
Later we will call this a causal mask.

During training, we already know the correct next tokens at several positions, so we can calculate and compare those predictions together.
When generating new text, the next token has not yet been chosen.
We choose one using the prediction at the final position and then calculate again.
Distinguish parallel calculations during training from sequential steps during generation.

Check question
May the "cat" position look ahead at "mat"?

Example answer
No.
That is future information that would not yet be available during actual generation.

## 7. RNNs and Transformers

On-screen explanation

An RNN waits for the preceding calculation.
A Transformer processes several positions together during training.

Speaker notes

The loop on the left indicates that the same calculation is repeated.
The diagram on the right unfolds that repetition in time order.
Here x is the current input and h is an internal state containing information from what has been read so far.
The same calculation unit, A, is used at several time steps.

In an RNN, the previous h is needed before the next h can be calculated.
It is like a queue in which the next person must wait for the person in front to finish a calculation before taking over.
Different sentences can be processed in a batch, but dependencies between time steps remain within each sentence.

A Transformer uses attention to calculate relationships between tokens.
During training, it is well suited to processing several positions in the given sentence together.
However, generating new tokens one at a time, as GPT does, is sequential for a Transformer too.
This does not mean that a Transformer always generates an entire sentence at once.

Check question
If a Transformer trains in parallel, does it already know future tokens when generating text?

Example answer
No.
The tokens to generate are selected one at a time.

## 8. Continuing text by choosing the next token

On-screen explanation

Predict, choose one token, and append it to the input.
Repeat this process to produce a sentence.

Speaker notes

Split the input sentence into tokens and pass them to the model.
The model returns a calculated probability for each possible next token.
We now have to decide which single token to select from that distribution.
This selection procedure is called sampling.

Choosing only the most probable token is simple.
However, always making the same choice can produce repetitive results.
Random selection according to the probabilities can produce different results from the same input.
For example, if A has 80% probability and B has 20%, drawing very many times from that same distribution selects them in approximately those proportions.
It does not mean that exactly eight of every ten draws must be A.

Temperature adjusts how peaked or even the distribution is.
Raising it can give less probable candidates more opportunities to be selected.
This does not automatically improve factual accuracy or creativity.
Append the selected token to the existing input and predict the following token again.
Stop at an end token or a predetermined length.

Check question
Why can the same model give different answers to the same question?

Example answer
It can make different selections while choosing tokens according to probabilities.

## 9. The overall architecture and residual connections

On-screen explanation

Keep the existing information and add the results calculated by attention and the MLP in turn.

Speaker notes

Read this diagram from bottom to top.
First, an embedding turns each token into a vector.
A vector is an ordered group of numbers.
A vector with 768 numbers is called a 768-dimensional vector.
Each number does not necessarily correspond to one human-readable concept, such as whether something is a cat.

The straight vertical path is called the residual stream.
Think of it as a shared notebook carrying information calculated so far.
Attention and the MLP to its side read that notebook and add newly calculated groups of numbers back to it.
Addition combines the numbers at matching positions.
The architecture does not erase all the existing information and replace it with the new result.

At the top, unembedding converts the final vector into a score for each vocabulary item.
These scores are called logits; they are not probabilities yet.
Applying softmax turns them into probabilities that sum to 1.
This diagram simplifies the flow; later diagrams add GPT2 details such as positional embeddings and normalization.

Check question
How can you explain adding x again in x + f(x)?

Example answer
It carries earlier information forward while adding the new calculation's result.

## 10. Representing token identity and position with numbers

On-screen explanation

Add a positional embedding to each token embedding to represent both what is present and where it is.

Speaker notes

A token ID is only an index, so it does not by itself provide a rich representation.
The embedding table contains a vector for each ID.
Token embedding uses the ID as a row index and retrieves that row's group of numbers.
These numbers are adjusted during training.

Order matters in a sentence too.
"The dog bit the person" and "The person bit the dog" use similar words but have different meanings.
GPT2 adds a vector prepared for each position to the token vector.
The two vectors must have the same length.
Their matching entries are added; they are not concatenated to double the length.
Other models can represent positions in other ways.

These vectors pass through several Transformer blocks and incorporate contextual information.
At the end, unembedding produces a score for each token, and softmax turns those scores into probabilities.
Softmax exponentiates each score and divides by the sum of those exponentials.
For now, remember its role: turning a list of scores into a list of probabilities.

Check question
Is an embedding a string containing a translated word?

Example answer
No.
It is a learned group of numbers used in the model's calculations.

## 11. Two calculations inside a Transformer block

On-screen explanation

Attention gathers information from other positions; the MLP processes the information at each position.

Speaker notes

A block is a calculation unit that is stacked repeatedly.
In the GPT2-style block shown here, normalized information goes into attention, and the result is added to the original stream.
The information is normalized again and passed to the MLP, whose result is also added.
The blue vertical line is the residual stream, which keeps carrying the existing information forward.

Attention calculates how much the current position should refer to earlier positions.
For example, when processing "He" in "Minsu bought an apple. He", information about Minsu may help.
The MLP processes the numbers gathered at each position.
The MLP operation itself does not directly retrieve vectors from other positions.
However, preceding attention may already have mixed contextual information into its input.

Stacking several blocks lets a later stage reuse the results of earlier stages.
Normalization adjusts the scale of numbers to make them easier to work with; we will look at its calculation on a later slide.
Follow the addition circles in the diagram and identify what is retained and what is added.

Check question
Which part directly gathers information between different positions in a sentence?

Example answer
Attention.

## 12. The calculation sequence in an MLP

On-screen explanation

Mix and expand the numbers, apply a nonlinear function, and return to the original vector length.

Speaker notes

An MLP is a small neural network that takes several numbers and calculates a new group of numbers.
The first linear layer in the diagram mixes the input numbers by multiplying them by weights and adding the results.
A matrix arranges those weights into a table.
A bias is a learnable constant added to a calculation's result.

The activation function in the middle changes each number nonlinearly.
A transformation that cannot be represented by a single straight line increases the relationships the network can express.
GPT2 uses a function from the GELU family.
The curve below shows relatively large positive inputs passing through while negative inputs are smoothly reduced.
You do not need to memorize the integral.

The final linear layer returns the vector to its original length so it can be added to the residual stream.
In the diagram, batch is the number of sentences processed together, seq is the number of tokens in a sentence, and d_model is the number of values per token.
d_mlp is the number of values in the intermediate MLP stage; in GPT2, it is usually four times d_model.
The MLP uses the same weights at each position.

Check question
Why match the final output length to d_model?

Example answer
To add matching entries to the original vector.

## 13. Does one number contain just one concept?

On-screen explanation

Several features can share overlapping directions in the same vector space.
This slide is optional further study.

Speaker notes

This slide is not required for implementing a Transformer.
It addresses the misconception that each entry of a vector must correspond to exactly one concept.
If this is new to you, it is enough to remember that several features can be represented across several numbers.

In a plane, we can choose at most two mutually perpendicular directions; in three-dimensional space, at most three.
In N dimensions, at most N nonzero vectors can be mutually orthogonal.
If we relax the requirement of perfectly right angles, we can fit many more directions that overlap slightly.
The related mathematics provides intuition for why high-dimensional spaces can help distinguish a great deal of information.

The phenomenon in which a model represents more features than it has dimensions using overlapping directions is called superposition.
Overlaps also cause interference, so the conditions under which they are useful matter.
Simple geometry alone does not establish that a larger model must perform better.
The rough exponential expression in the original material omits conditions, so it is not presented here as the exact formula of a theorem.

Check question
Does the seventeenth number of a vector always mean one fixed concept that a person can understand?

Example answer
There is no such guarantee.

Source
https://www.anthropic.com/research/toy-models-of-superposition

## 14. MLPs and activation functions

On-screen explanation

Process input information using connection weights together with a nonlinear transformation.

Speaker notes

Each circle on the left represents one number in the calculation.
Moving from the input layer at the bottom to the hidden layer in the middle, each connection multiplies by a weight, and the results are added.
"Hidden" means an intermediate calculation stage between input and output; it does not mean something specially secret.

Read the equation from the inside outward.
Mix the numbers with W1x + b1, apply the activation function denoted by σ, and transform them again using W2 and b2.
W is a weight matrix and b is a bias.
Both are adjusted during training.
On this slide, σ denotes an activation function in general, not necessarily the sigmoid function.

Without an activation function, repeated linear transformations can be combined into a single linear transformation.
A nonlinear transformation between them lets the model represent more varied relationships.
GELU and ReLU can provide similar intuition, but they are different functions.
Read the approximation in the original material only as intuition about their shapes; do not memorize it as an equality.
Φ is the cumulative probability of the standard normal distribution.
Today, focus on the function's role rather than how to calculate it.

Check question
Why place an activation function between the linear transformations?

Example answer
To express relationships that repeated linear transformations alone cannot represent.

## 15. Adjusting the scale with layer normalization

On-screen explanation

Normalize the numbers within one token's vector, then apply a learned scale and shift.

Speaker notes

Even when numbers carry the same information, very uneven scales can make training calculations harder to handle.
Layer normalization calculates the mean and variance within each token's vector and adjusts its scale.
It does not average all tokens or different sentences together.

First, subtract the mean from each value to bring the center near zero.
Next, divide by the square root of the variance plus a small positive number, ε.
The ε makes the calculation stable when the variance is very small.
Up to this point, the adjustment makes the mean zero and the variance approximately one.

Finally, multiply by learnable γ and add β.
Consequently, the final output does not always have a mean of exactly zero and a variance of exactly one.
This qualification was added because the original wording could omit that last step.
In the diagram, the normalized result is sent into attention or the MLP, and that calculation's result is added to the original residual stream.

Check question
Does LayerNorm combine all tokens in a sentence into one vector?

Example answer
No.
It normalizes each token's vector separately and preserves its length.

Source
https://arxiv.org/abs/1607.06450

## 16. Calculating one attention head

On-screen explanation

Use Q and K to determine attention weights, then mix V using those weights.

Speaker notes

Attention retrieves information from several positions in the required proportions.
Three vectors are made from the vector at each position.
As an analogy, the query Q describes what information is needed now, the key K describes which requests this position matches, and the value V contains the information to pass on.
All three are actually groups of numbers produced using learned weights.

Calculate a score by taking the dot product of the current Q with K at each position.
A dot product multiplies matching entries and adds the products.
A higher score means a stronger match in this calculation.
Scale the scores by dividing by the square root of the vector length, mask future positions, and apply softmax to obtain the proportion assigned to each position.

Take a weighted sum of the V vectors using these proportions.
For example, if two positions have weights of 0.75 and 0.25, the result is 0.75V1 + 0.25V2.
It is not simply selecting and copying one position.
The final W_O transformation gives the result the length needed for addition to the residual stream.
The simplified formula on the right shows the core calculation without the mask or final output transformation.

Check question
Are these probability-like attention weights the probabilities of the next word?

Example answer
No.
Here they describe which input positions to refer to and in what proportions.

## 17. A causal mask that prevents looking into the future

On-screen explanation

The current position can refer only to itself and earlier tokens.

Speaker notes

During training, the entire sentence is present in the input.
Without a restriction, a position asked to predict the next token could read the answer in advance.
We therefore block access to tokens after the current position.
This is the causal mask.

In the table, a row is the current position requesting information, or the query.
A column is a position being referred to, or the key.
For columns later than the row's position, set the scores to a very small value, mathematically negative infinity.
After softmax, their attention weights become zero.
Remember the order: apply the mask before softmax.

Keep the diagonal because it represents the current position itself.
The model knows the current token as input and predicts the next one.
The allowed weights in a row add up to 1.
For example, the third token can refer to the first, second, and third positions, but cannot see the fourth.

Check question
What is the attention weight from the third position to the fifth position?

Example answer
Zero, because the fifth position is still in the unavailable future.

## 18. Understanding attention through questions and answers

On-screen explanation

Where the query Q matches the key K, retrieve the content V to pass on.

Speaker notes

Each person in the drawing represents a token position.
Each person wants to refer to preceding words to predict the next word.
The question in the speech bubble represents Q, the label indicating what questions can be answered represents K, and the actual content passed on represents V.
This analogy distinguishes the roles of the calculations; it does not mean the model internally produces question sentences that people can read.

In the example "The sky is", retrieving information from "sky" can help the "is" position predict the next word.
Q and K provide relevance scores, softmax produces weights, and those weights mix the V vectors.
A position can also receive information from itself.

Check the horizontal and vertical directions of the table on the right.
Several queries are each compared with several keys.
Cells marked in red to mask the future cannot be used.
However, the heads in a real model do not necessarily have roles that a person can label, such as "find the color of the sky."

Check question
Which of Q, K, and V contains the vectors actually mixed and passed on?

Example answer
V.
Q and K determine the weights used to mix that information.

## 19. Distinguishing attention from the MLP

On-screen explanation

Attention gathers information from other positions; the MLP processes the information gathered.

Speaker notes

The people in the drawing on the left can ask questions of the people before them.
This represents attention gathering information between tokens.
The content passed on by several people is mixed according to how well their queries and keys match.
When predicting what follows "The sky is", this is the stage that retrieves preceding context.

The light bulb at the upper right represents the MLP processing information at its own position.
It does not ask other people new questions.
It calculates a new result using information already received and information originally present.
The same MLP is applied at every position, but different input vectors produce different results.

Distinguish "the MLP does not directly see other tokens" from "the MLP uses no context at all."
A vector that has passed through earlier attention may already contain information from other positions.
Across several blocks, gathering and processing information are repeated.

Check question
Can the input to an MLP contain information about an earlier word?

Example answer
Yes.
Previous attention may have brought that information to the current position.

## 20. Using several attention heads together

On-screen explanation

Several heads gather information with their own attention weights, then combine the results for the next stage.

Speaker notes

The left shows one head, while the right shows several heads being calculated together.
A head is an attention calculation unit with its own Q, K, and V weights.
Even with the same input, different weights can make heads attend to different positions.

You can compare this to several people reading the same text from different perspectives.
However, a person does not assign "grammar" to one head and "meaning" to another in advance.
Training determines what they calculate.
The results from the heads are mapped into the original vector space through output transformations and added together.

An implementation often concatenates the head results and multiplies by one large output matrix.
This can express the same calculation as splitting the output transformation by head and adding the results, as illustrated here.
b is the number of sentences in a batch, s the number of tokens, n the number of heads, h the vector length within a head, and e the residual-vector length.
Since h can mean different things in different notations, check names such as d_head in the code.

Check question
Do several heads necessarily take on different linguistic roles?

Example answer
There is no such guarantee.
The architecture gives them the opportunity to use different information.

## 21. Reviewing the five attention steps

On-screen explanation

Create Q, K, V; calculate scores; mask the future; take a weighted sum of V; apply the output transformation.

Speaker notes

Let us describe the calculation again as five steps instead of one complicated equation.
First, create Q, K, and V from each position's vector.
Second, compare the current Q with each K to produce scores and scale them.
Third, mask future positions and apply softmax.
Fourth, mix the V vectors using the resulting weights.
Fifth, return the result to the original vector length and add it to the residual stream.

Follow the arrows in the diagram from bottom to top.
Q and K meet to produce attention weights, while V follows a separate path upward to meet those weights.
The structure becomes easier to understand if you distinguish where to retrieve information from and what information to retrieve.

A higher attention weight means that the position's V has a larger coefficient in the weighted sum.
That alone does not establish that the token caused the final answer.
The contents of V, the output transformation, other heads, and subsequent calculations also matter.
At first, concentrate on learning the calculation order accurately rather than on this limitation.

Check question
Why apply an output transformation before adding the attention result to the residual stream?

Example answer
To give the retrieved information the required form and vector length.

## 22. Predictions change as context grows

On-screen explanation

Even for the same model, changing the preceding text changes the probabilities of the next tokens.

Speaker notes

In each graph, the horizontal axis lists possible next tokens and the vertical axis shows probabilities calculated by the model.
First look at the prediction after "The cat sat", then at the graphs after adding "on" and "the" to the input in turn.
As the context becomes more specific, the most likely candidates change.

Two models can assign different probabilities to the same sentence because their training data, weights, architectures, tokenizers, and other details differ.
Only some candidates are shown, so the displayed bars do not necessarily add up to 1.
The probabilities add up to 1 only when all vocabulary items are included.

Check the vertical-axis range in each graph too.
Comparing bar heights by sight alone can be misleading.
One model giving a particular candidate a higher probability in one example does not establish that it is better at every task.
The purpose of this slide is to see how the prediction distribution changes with input context and model choice.

Check question
If one more token is appended after "The cat sat", do the remaining predictions stay the same?

Example answer
No.
The probabilities of the next tokens are recalculated using the new context.

## 23. Checking tensor shapes during implementation

On-screen explanation

Check the array shape at each arrow to follow an attention implementation.

Speaker notes

A tensor arranges numbers along several axes.
A vector has one axis and a matrix has two.
Adding batch and head axes gives arrays with three or four axes.
Writing down their order and lengths helps prevent calculation mistakes.

In this diagram, b is batch size, s the number of tokens, e the model-vector length, n the number of heads, and h the head-vector length.
The input usually has shape (b, s, e).
Creating Q, K, and V introduces a head axis.
Comparing Q and K produces two token axes: the query position and the position being referred to.
The attention weights can usually be thought of as having shape (b, n, s_q, s_k).

Mixing V sums along s_k, the axis of positions being referred to.
The query-position axis, s_q, must remain.
Finally, combine the head outputs to return to (b, s, e).
The precise axis order can differ between implementations, so follow the axis names in the einsum expression.
The high-resolution source link lets you inspect the equations and axis labels more closely.

Check question
Should the token-position axis disappear from the attention result?

Example answer
No.
There should be one output vector for each query position.

## 24. Developments beyond the basic architecture

On-screen explanation

For today, understanding the basic GPT2 flow is enough.
Architectural variations are the next step.

Speaker notes

This reference slide shows that later research has modified parts of the Transformer's calculations.
The papers' English titles, covers, and source images are retained so that you can recognize the originals.
You do not need to read these papers before beginning the exercises.

To connect the names briefly, GLU and SwiGLU are families that change how information passes through the MLP, while RoPE is a way to represent position.
Mixture-of-experts architectures choose some calculation modules according to the input.
These are easier to compare after learning the basic architecture.

Summarize today's path in your own words.
Convert text to token IDs, and use embeddings to obtain numerical vectors.
Gather context with attention, process it with MLPs, and accumulate results through residual connections.
Finally, turn vocabulary scores into probabilities and select the next token.
You can now implement the components in the exercises while checking each component's input and output shapes.

Check question
What do you do after choosing one next token?

Example answer
Append it to the input and predict the next token again.

Reference
https://www.youtube.com/watch?v=11Z50mi8dSg&t=173s

This script was newly written from the original slides for beginner learners; it is not a verbatim transcript of the video's speech.
