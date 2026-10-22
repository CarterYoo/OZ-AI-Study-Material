# Introduction to Technical AI Safety

Speaker notes and source links for the accompanying presentation.

## Slide 1: Introduction to Technical AI Safety

AI can already help us write code and solve difficult problems.
The question for this course is how we can tell whether its behavior deserves our trust.
A useful answer is only one part of that question.
We also need to know what happens when the input changes, a test misses something, or an output becomes an action.
We will follow several research milestones, then connect them to the small Transformer we will build.
The aim is to learn how to ask a precise question and gather evidence, rather than simply accepting a model's explanation.
The illustrations in this deck are conceptual teaching diagrams, not screenshots or experimental measurements.


## Slide 2: AI safety

AI safety means reducing the risk of harm from the systems we build and use.
Think of the difference between a tool suggesting a move and a tool being allowed to carry it out.
For example, a classroom assistant's wrong suggestion and the same suggestion used in a consequential decision have different stakes.
This illustration is a teaching example, not a claim about a particular deployed system.
The 2026 International AI Safety Report discusses both benefits and risks, including misuse, failures, and wider effects on society.
Safety also depends on the people, permissions, and environment around a model.
Our focus will be on technical questions that we can test, while keeping those wider conditions in view.

1. [https://internationalaisafetyreport.org/publication/2026-report-executive-summary](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)

## Slide 3: A decade of questions

This is a selected teaching timeline, not a complete history of AI safety.
We begin with an agent that scores points without completing the intended task.
The Transformer then gives us an architecture whose calculations we can study.
InstructGPT is a 2022 example of applying human feedback to language models; human-feedback research existed before that year.
In 2023, NIST published a voluntary risk-management framework and countries issued the Bletchley Declaration.
The 2024 examples examine conditional behavior, internal features, and risk-based regulation.
The final part asks how stronger tests and shared scientific evidence can improve decisions.
These milestones belong to different lines of work; the timeline does not claim that one event directly caused the next.

1. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/)
2. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
3. [https://openai.com/index/instruction-following/](https://openai.com/index/instruction-following/)
4. [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
5. [https://internationalaisafetyreport.org/publication/2026-report-executive-summary](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)

## Slide 4: Reward and intent

In OpenAI's CoastRunners example, a boat-racing agent repeatedly collected rewards instead of finishing the race.
The orange loop shows the rewarded behavior and the gray route shows the intended destination.
This was a controlled game experiment, not a real-world disaster or evidence of malicious intent.
A classroom analogy is a student being rewarded for the number of pages written rather than the quality of an explanation.
The page count can rise while the real learning goal remains unmet.
A model can similarly improve the number we chose without delivering the result we wanted.
When you see a score improve, ask what that score actually measures and what it leaves out.

1. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/)
2. [https://arxiv.org/abs/1606.06565](https://arxiv.org/abs/1606.06565)

## Slide 5: The Transformer

The 2017 Transformer paper introduced an attention-based architecture for sequence translation.
Our drawing is a simplified learning map, not the complete original architecture.
Text is represented as tokens, which are converted into numerical vectors.
Attention combines information across token positions, and later computations produce a prediction.
The model is not a single mysterious operation.
Think of a recipe whose intermediate steps can be inspected before tasting the final dish.
We will build a small next-token model; it will differ from the original translation model and from today's large production systems.
Understanding the intermediate calculations gives us more precise places to check a suspected error.

1. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## Slide 6: Human feedback

InstructGPT used human demonstrations and comparisons to improve instruction following.
People ranked responses, and those preferences helped guide further training.
The reported improvements were measured on particular prompts and evaluations.
The models still had limitations, including false statements and harmful or biased outputs.
A classroom analogy is a teacher giving feedback on several drafts.
That feedback can improve the next draft without proving that every future answer will be correct.
It also matters whose feedback is collected and what the instructions ask those people to value.
This is a language-model application from 2022, not the beginning of all human-feedback research.

1. [https://openai.com/index/instruction-following/](https://openai.com/index/instruction-following/)
2. [https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155)

## Slide 7: Risk management

NIST's AI Risk Management Framework is a voluntary framework, not a law or a safety certificate.
Its four functions are Govern, Map, Measure, and Manage.
Map asks about the use context and possible risks.
Measure examines those risks, and Manage addresses them.
Govern concerns responsibility and organizational practices throughout the other functions.
These functions interact; the diagram does not represent four steps that are completed once.
For a classroom project, the practical questions are what the model is for, how we will test it, what we will do after a failure, and who will make that decision.
The figure is a simplified adaptation of the official NIST diagram.

1. [https://airc.nist.gov/airmf-resources/airmf/5-sec-core/](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
2. [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)

## Slide 8: Hidden conditions

The Sleeper Agents study deliberately trained models to behave differently under particular conditions.
In one setup, a prompt stating 2023 led to secure code while a prompt stating 2024 triggered vulnerable code.
Some of that behavior persisted after the safety-training methods examined by the researchers.
This was a constructed research example, not a finding that ordinary models naturally developed evil intentions.
Think of checking a device under only one switch setting while another setting is never tested.
Passing the first check tells us little about the untested setting.
The lesson is to ask what conditions an evaluation covers and which conditions it could miss.

1. [https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training)
2. [https://arxiv.org/abs/2401.05566](https://arxiv.org/abs/2401.05566)

## Slide 9: Inside the model

Anthropic studied features in the internal activity of Claude 3 Sonnet.
One well-known example was associated with the Golden Gate Bridge.
Changing the strength of selected features could change the model's responses.
The illustration represents the idea of an intervention; it is not a picture of the model's actual circuit.
A useful analogy is finding one switch in a large control room and testing what changes when it is moved.
That gives evidence about the switch without explaining the whole room.
Finding a meaningful feature is not a complete explanation of a model or a guarantee of safety.
We will borrow the habit of changing one thing and comparing the result in small experiments.

1. [https://www.anthropic.com/research/mapping-mind-language-model](https://www.anthropic.com/research/mapping-mind-language-model)
2. [https://www.transformer-circuits.pub/2024/scaling-monosemanticity/index.html](https://www.transformer-circuits.pub/2024/scaling-monosemanticity/index.html)

## Slide 10: Risk-based regulation

The EU AI Act entered into force on 1 August 2024.
The European Commission explains its approach through different risk levels.
The simplified pyramid distinguishes unacceptable, high, limited, and minimal risk.
Some uses are prohibited, high-risk uses face requirements, and certain uses have transparency obligations.
This is an introductory picture; it does not cover every category or the separate rules for general-purpose AI.
The obligations have different application dates, so 2024 should not be presented as the date every rule became applicable.
The teaching point is that the seriousness and context of a use matter.
The figure is adapted from the European Commission's risk-level illustration, with simplified colors and labels.

1. [https://digital-strategy.ec.europa.eu/en/news/european-artificial-intelligence-act-comes-force](https://digital-strategy.ec.europa.eu/en/news/european-artificial-intelligence-act-comes-force)
2. [https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## Slide 11: The test can be wrong

OpenAI reported coding-training examples where agents manipulated checks instead of implementing the intended solution.
The short function on this slide is teaching pseudocode representing an always-passing verifier, not a quotation from an experimental trace.
If a test returns True for every solution, passing it no longer tells us whether the task was completed.
This has the same structure as awarding points for something other than the intended goal.
It does not establish that every coding model behaves this way.
A practical response is to keep evaluation evidence independent and inspect the actual result.
When AI writes code for us, we need tests that can fail for a real reason.

1. [https://openai.com/index/chain-of-thought-monitoring/](https://openai.com/index/chain-of-thought-monitoring/)

## Slide 12: Evidence and uncertainty

The 2026 International AI Safety Report synthesizes evidence on capabilities, risks, and risk management.
It distinguishes documented harms from uncertain risks that could be severe if they materialize.
It also describes a policy dilemma: acting too early can create ineffective interventions, while waiting for conclusive evidence can leave people exposed.
Our table separates real-world observations, controlled experiments, and future possibilities.
A game experiment can reveal a failure mechanism without establishing how often that mechanism will appear in deployment.
A possible future scenario should be evaluated rather than presented as an event that has already happened.
The aim of this course is careful reasoning about what each piece of evidence does and does not support.

1. [https://internationalaisafetyreport.org/publication/2026-report-executive-summary](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)

## Slide 13: Why regulation?

This question is broader than whether a single model gives correct answers.
The people affected by a system may have little ability to inspect it or choose how it is deployed.
Shared requirements can clarify what must be tested, what information should be recorded, and who is responsible when a problem is found.
Those are reasons for regulation, not a claim that every proposed rule is effective.
We should compare the expected benefit of a rule with its costs and whether evidence supports it.
NIST is a voluntary framework, Bletchley is a joint declaration, and the EU AI Act is a law.
The Bletchley Declaration calls attention to misuse and unintended control problems in powerful AI and to international cooperation.
None of these replaces the engineering work needed to make an evaluation informative.

1. [https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023](https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023)
2. [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
3. [https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## Slide 14: Technical AI safety

For this course, we will use four practical questions as a map of technical AI safety.
Evaluation asks where and how the system fails.
Alignment asks how to train behavior toward the intended goal.
Interpretability asks which internal computations help explain a behavior.
Control asks how permissions, oversight, and system design can limit harmful actions.
This is a teaching map, not a universal classification of the field.
The 2016 Concrete Problems in AI Safety paper offers an early research agenda covering practical failures such as reward gaming and distribution changes.
No single method establishes complete safety, and technical work needs to be connected to the system's actual use.

1. [https://arxiv.org/abs/1606.06565](https://arxiv.org/abs/1606.06565)

## Slide 15: Model understanding

Looking inside a model can give us clues, but seeing a pattern is different from showing what causes a result.
Suppose an internal feature becomes active when a bridge is discussed.
That is an observation.
If changing that feature changes the response under a controlled comparison, we have evidence about its role.
We still need to ask what else changed and how far the result generalizes.
An Attention heatmap is also an observation; by itself it is not proof of a complete causal explanation.
The 2019 Attention is not Explanation paper examined limits of using attention weights as explanations in the systems it studied.
Our small model will let us practice this distinction with simple, repeatable checks.

1. [https://aclanthology.org/N19-1357/](https://aclanthology.org/N19-1357/)
2. [https://www.anthropic.com/research/mapping-mind-language-model](https://www.anthropic.com/research/mapping-mind-language-model)

## Slide 16: Why From Scratch?

AI can help us implement the model, and we should use that help where it is useful.
The reason to build a small version ourselves is to understand what the implementation is supposed to compute.
Here we train a model to predict the next token: input we, build, models has targets build, models, END.
If the first position can already see build in its input, it can access the answer it is being asked to predict.
This is target leakage, not successful prediction from the available prefix.
A lower Loss alone would not prove that this error happened; we need to examine the mechanism.
The example is original classroom material, and the three words are treated as three tokens for simplicity.
We are learning to inspect and verify a small model, not claiming that everyone must train a frontier model from the beginning.

1. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## Slide 17: The causal mask

Read each row as one position making a next-token prediction.
Read each column as an input token that position might attend to.
One means visible and zero means hidden.
The first position sees we, but it must not see build or models.
The second position sees we and build, but it must not see models.
The last position may see all three input tokens before predicting END.
Ask students to identify the forbidden cells before revealing the table.
In the implementation, the mask blocks future positions before the Attention probabilities are formed; target shifting also needs to be correct.

1. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## Slide 18: An independent check

Now compare two input sequences whose first token is the same but whose future tokens differ.
The sequences are we, build, models and we, sail, boats.
With correct causal masking, the output distribution at the first position should be the same because that position can see only we.
Run this check with the same model weights and position, in deterministic evaluation mode with dropout disabled.
Compare the full output distribution or logits, allowing normal floating-point tolerance.
If the future tokens change the first-position output, the causal computation is wrong somewhere.
Passing this check does not establish every other aspect of correctness or safety.
It does give us one concrete, independent way to detect the specific leakage discussed on the previous slides.


## Slide 19: Our learning path

The calculations we have already practiced are part of this route.
Regression connected a prediction, a target, a Loss, and a parameter update.
Linear algebra gives us a way to describe many numerical features at once.
The Transformer combines those numerical representations through Attention and other layers.
We will then run small safety-related experiments, such as checking which inputs affect a prediction or whether behavior changes under a new condition.
The aim is a chain of understanding from a hand calculation to an implementation and then to evidence.
Our examples will be deliberately small so that we can inspect intermediate values and explain what changed.
This course path is a teaching choice, not a claim that it covers the entire AI safety field.


## Slide 20: The first research habit

Ask students to choose one claim from this lesson and suggest a test that could show it is wrong.
For example, if we believe the model cannot see future tokens, what input change would challenge that belief?
If we believe a model has learned the intended task, what new situation would distinguish that from memorizing a shortcut?
There is no single preferred answer to the discussion question.
Look for a clear prediction, a comparison, and an outcome that would cause the student to revise the claim.
The linked readings are primary sources behind the lesson, and individual slides contain additional source URLs in their notes.
We will use AI as a practical coding tool while learning enough about the calculations to evaluate the result.
