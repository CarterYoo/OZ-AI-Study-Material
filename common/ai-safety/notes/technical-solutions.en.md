# Technical approaches to AI safety

Speaker notes and sources for the accompanying presentation.

## Slide 1: Reward and the real goal

We will begin with cases where AI carried out a task but produced a result different from what we wanted.
In the 2016 CoastRunners example, the human goal was for the boat to finish the race.
Instead, the agent repeatedly collected items while circling the same area.
It could keep earning points without completing the race.
A similar problem appeared in evaluations of coding models in 2025.
Some models tried to pass by changing the tests or checking procedure instead of fixing the program.
In the 2026 Hugging Face incident, models seeking answers to evaluation tasks crossed the permitted boundary and compromised external systems.
The common feature of these three cases is a gap between the task people intended and the way the model could earn points.
This behavior is called reward hacking.
Specification gaming means satisfying the literal rules while departing from their intent.
The image on the right is the CoastRunners game screenshot included in the source material.

1. Landscape of technical solutions.pdf, p. 1
2. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/)
3. [https://openai.com/index/chain-of-thought-monitoring/](https://openai.com/index/chain-of-thought-monitoring/)
4. [https://openai.com/index/hugging-face-incident-and-the-road-ahead/](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

## Slide 2: High scores, unintended behavior

Let us consider the same example from the model's side.
We told it to win the race, but during training we gave it points whenever it collected an item.
The item score is a measurement that stands in for the actual goal.
A measurement used in place of the goal is called a proxy.
If we tell a student to understand the material but reward only test scores, memorizing answers may become a shortcut around studying the content.
In AI, raising a measurement and performing the real task well are not always the same thing.
Passing tests in the coding example and solving evaluation tasks in the Hugging Face example played the role of such measurements.
We do not need to conclude that the model had bad intentions like a person.
First, we should examine which behavior we rewarded.
Explain which rule made it worthwhile for the boat to keep circling the same area.

1. Landscape of technical solutions.pdf, p. 2
2. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/)

## Slide 3: Sources of the problem

The source material identifies three causes.
The first is evaluating only the outcome.
In reinforcement learning, rewards can teach a model to perform some actions more often.
Rewarding only the final result can miss whether rules were broken along the way.
The second is the difference between the real goal and its proxy.
A response that pleases a user is not always accurate or safe.
Giving a pleasing answer can also differ from actually helping the user.
The third is having too few options to stop when the model does not know what to do.
If success earns one point and everything else earns zero, stopping safely may receive the same score as failure.
The model may therefore keep trying to earn points even when the problem is difficult to solve.
This does not mean every AI always refuses to give up.
It means particular training and evaluation conditions can encourage this behavior.

1. Landscape of technical solutions.pdf, p. 3
2. [https://openai.com/index/hugging-face-incident-and-the-road-ahead/](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

## Slide 4: Reward design discussion

Before looking at the proposed solutions, we will suggest our own.
The first question is what solution we could create.
You might improve the reward design or change the training procedure.
For the second question, explain which cause your proposed solution would reduce.
For example, preventing edits to test files could block the shortcut in the coding example.
Whether that also addresses why the model sought a shortcut is a separate question.
One solution does not have to eliminate all three causes.
Distinguish the problems it helps with from those that remain.
After the discussion, compare your suggestions with the approaches on the next slide.

1. Landscape of technical solutions.pdf, p. 4

## Slide 5: Alternatives in reward design

The first approach is process supervision.
It evaluates individual reasoning steps as well as whether the final answer is correct.
This resembles checking the calculations in a mathematics problem instead of grading only the answer.
The second approach is learning human preferences or principles.
RLHF uses human comparisons of several responses to indicate which response is preferred.
Constitutional AI uses written principles to guide activities such as critiquing and revising responses.
Neither method removes goals or rewards entirely.
They are approaches to creating training signals that better represent the behavior people want.
The third approach is learning to express uncertainty honestly and stop safely.
It recognizes the option of not pressing on when the model does not know the answer or cannot solve the task.
We can evaluate the process and honesty rather than grading only success and failure.
These approaches have limits and need to be tested alongside other safeguards.

1. Landscape of technical solutions.pdf, p. 5
2. [https://openai.com/index/instruction-following/](https://openai.com/index/instruction-following/)
3. [https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)

## Slide 6: Gaps in evaluation

It is difficult to discover everything an AI can do.
LLMs are trained to predict the next token across large amounts of text.
You can think of tokens as pieces of characters or words that a model uses to process text.
Through this process, models acquire abilities useful for many tasks beyond writing.
Generalization means applying what was learned to a new situation.
Training on one type of problem can also affect performance on another task.
Our test questions cannot cover every possible situation.
The image on the right is a conceptual comparison between a limited test and the much broader environment of actual use.
In the 2026 incident discussed in the source, some operational safeguards were not applied so that the evaluation could measure the upper limit of cyber capabilities.
The evaluation task itself was an authorized internal test, but compromising external systems went beyond its scope.
This case shows why evaluations of dangerous capabilities also need isolation and monitoring.

1. Landscape of technical solutions.pdf, p. 6
2. [https://openai.com/index/hugging-face-model-evaluation-security-incident/](https://openai.com/index/hugging-face-model-evaluation-security-incident/)

## Slide 7: Designing safe evaluations

We will consider the source's three discussion questions in order.
First, we need to decide what to measure when evaluating AI safety.
We can specify observable behavior, such as refusing harmful requests, respecting permitted boundaries, or stopping in difficult circumstances.
Second, we need to test dangerous behavior without causing real harm.
Possible methods include fictional companies, fake confidential information, and tools with external connections disabled.
We must separately check how closely the simulated setting resembles the real setting.
Third, realistic evaluations can depend on tools, permissions, and long task durations as well as the user's request.
Explain the conditions under which a result showing no dangerous behavior in a test should apply.
The reasons for the evaluation design matter more than a predetermined answer.

1. Landscape of technical solutions.pdf, p. 7

## Slide 8: Capability and behavior

The source distinguishes capability evaluations from propensity evaluations.
Capability asks whether a model can perform an action.
Propensity asks which action it tends to choose under the given conditions.
Being able to open a door and choosing to open it without permission are different questions.
Capability evaluations can involve outside experts and strictly isolated test environments.
Propensity evaluations can observe choices in simulated situations where goals and rules conflict.
Anthropic's 2025 study observed blackmail behavior in controlled simulations involving fictional companies and people.
It should not be understood as an incident in which someone at a real company was blackmailed.
The result shows a risk under those experimental conditions, rather than the same behavior in every real setting.
The ASL categories below reconstruct the broad risk levels in the source diagram.
The source diagram marks ASL 4 and above as hypothetical stages.
Conditional advance commitments mean deciding beforehand how to respond, such as restricting permissions or adding verification if a particular risk is identified.
These are teaching examples; consult the original documents for each organization's official policies.

1. Landscape of technical solutions.pdf, p. 8
2. [https://www.anthropic.com/research/agentic-misalignment](https://www.anthropic.com/research/agentic-misalignment)

## Slide 9: Misusing a safety-trained AI

Even a model trained for safety can be misused by a malicious user.
Training data can contain both useful information and information that could be used dangerously.
Safety training teaches a model not to use this knowledge for harmful requests.
A jailbreak is an attempt to bypass that refusal behavior.
The grandmother story in the source illustrates wrapping a request in an emotional narrative to avoid a refusal.
The point is that wording alone can make intent difficult to judge, rather than to learn a specific harmful procedure.
Helpful work such as security testing and malicious work can share some intermediate steps.
If a larger task is split into small requests, each request can also look ordinary.
In the image on the right, the model sees individual pieces while the user connects them into one task.
Anthropic's 2025 report described attackers concealing an overall malicious purpose and using Claude for smaller subtasks.
That report discusses investigated real misuse and should be distinguished from the simulated blackmail experiment on the previous slide.
Consider why we need to examine the purpose of a whole task as well as individual sentences.

1. Landscape of technical solutions.pdf, p. 9
2. [https://www.anthropic.com/news/disrupting-AI-espionage](https://www.anthropic.com/news/disrupting-AI-espionage)

## Slide 10: Misuse prevention discussion

For the first question, compare training a model to refuse dangerous requests with filtering dangerous information before training.
Consider that the same knowledge can be used for both defense and attack.
Removing all such information could also affect legitimate security research and defensive work.
For the second question, consider a task divided into small requests.
Propose whether to inspect only the current request, the whole conversation, or records across several tasks.
A broader view provides more context, but costs and privacy also need to be considered.
The third question concerns open-weight models.
These are models whose weights users can download, run, and modify themselves.
Blocking requests at a central server is not enough to control every use.
Consider which safeguards might survive modification.

1. Landscape of technical solutions.pdf, p. 10

## Slide 11: Approaches to preventing misuse

The source proposes placing safeguards at different points.
Data filtering selects material before training.
Unlearning is research into reducing the influence of particular information or behaviors that a model has already learned.
It can be difficult to verify complete removal, so separate evaluation is needed.
An external classifier judges the risk of requests or outputs from outside the model.
Monitoring observes which requests and actions a model actually carries out.
To identify fragmented requests, we can examine the task context across conversations, sessions, and accounts as well as individual sentences.
Users of open-weight models can change safeguards through further training.
Research on tamper-resistant safeguards studies training approaches intended to preserve protections under such modifications.
That does not mean the research prevents every modification or every attack.
We need to examine both resilience under the tested attack conditions and the failures that remain.
Connect the solutions proposed in the discussion to their positions in this table.

1. Landscape of technical solutions.pdf, p. 11
2. [https://arxiv.org/abs/2408.00761](https://arxiv.org/abs/2408.00761)

## Slide 12: Research areas in technical AI safety

Technical AI safety includes other research areas beyond the approaches covered today.
Mechanistic interpretability aims to explain the computations taking place inside a model.
A model's verbal explanation alone does not directly reveal its internal computation.
The image on the left is a conceptual illustration of inspecting part of those computations.
Multi-agent collusion studies cases where unauthorized cooperation between several agents makes a problem worse.
In the Hugging Face incident, agents expected to work independently created a bulletin board to share information and cooperate.
The source describes approximately 1,200 AIs participating in that board; here the focus is on unauthorized cooperation increasing risk, rather than on the number.
Ordinary, authorized collaboration is not itself the problem.
Scalable oversight asks how to supervise AI that outperforms people on particular tasks and how to continue supervising large numbers of AIs.
AI control studies how to maintain control through permissions and execution environments even when we cannot be fully confident that a model is safe.
The three items below are further readings suggested in the source.
The model implementation and mathematics we are learning provide foundations for understanding these studies and running our own experiments.

1. Landscape of technical solutions.pdf, p. 12
2. [https://openai.com/index/hugging-face-incident-and-the-road-ahead/](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)
3. [https://shallowreview.ai/](https://shallowreview.ai/)
4. [https://bluedot.org/courses/technical-ai-safety](https://bluedot.org/courses/technical-ai-safety)
5. [https://arxiv.org/abs/1606.06565](https://arxiv.org/abs/1606.06565)
