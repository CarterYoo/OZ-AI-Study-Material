# Week 06 / Technical AI Safety

Reading guide for Canva pages 136 to 148. This guide follows the examples in the classroom deck; the PDF preserves the original Korean slide text.

## Safety and security

AI safety asks whether a system behaves as intended and avoids harmful outcomes. Security asks how to protect it from attacks, unauthorized access, and data theft. These areas overlap. In the car analogy, an unintended steering failure illustrates safety; preventing theft illustrates security.

## Red teaming

A tester deliberately searches for failures. Rewording a request, introducing a misleading role-play, or checking whether an agent crosses a boundary can reveal weaknesses. Red teaming is a testing method that can be applied to several different failure types.

## Sycophancy

A model may agree with a user's belief or flatter a weak plan instead of giving a well-supported answer. Compare its answer before and after a user challenges it. A change alone is not enough to establish a problem: examine whether the change follows evidence or only the user's preference. Training rewards are one possible contributor, rather than a complete explanation of every example.

## AI control

Consider safeguards that remain useful even when a powerful model is unreliable. The workplace analogy suggests monitoring, limited permissions, and a second approval for consequential actions. In trusted monitoring, another model checks the work and suspicious cases can be escalated. The monitor also has limits, so its reliability must be evaluated.

## Prompt injection

An attacker places instructions in text the model encounters, such as a document or email, and tries to redirect the task. Distinguish the user's authorized request from external material being read as data. Check both attempted redirection and any action that actually occurred.

## Collusion between agents

Several agents may coordinate in a way that conflicts with the intended rules, including coordination that evades monitoring. An agent that passes an individual test does not establish that the group is safe. Ordinary cooperation is not sufficient evidence of collusion; examine the rules, information flow, and effects. Hidden signaling is one possible mechanism to investigate.

## Hackathon project themes

| Theme | Question to investigate |
| :--- | :--- |
| Agent interactions | How can harmful coordination, contamination, or identity changes be detected and limited? |
| Trustworthy advice | Does an assistant change its advice because of evidence or because the user wants agreement? |
| Agent attribution | What evidence distinguishes an agent's actions from human-directed behavior? |
| Threat analysis | Do cited sources support an automatically generated threat assessment? |
| Small-model training | Does a training change improve measured behavior on examples not used to make that change? |

Event descriptions and dates remain in the classroom PDF. This guide does not confirm registration dates or event availability.
