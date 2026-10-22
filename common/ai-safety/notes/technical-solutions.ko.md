# AI 안전의 기술적 접근

Speaker notes and source links for the accompanying presentation.

## Slide 1: 보상과 실제 목표

AI가 과제를 수행했는데도 우리가 원한 결과와 어긋나는 경우부터 살펴보겠습니다
2016년 CoastRunners 사례에서 사람의 목표는 보트가 경주를 완주하는 것이었습니다
하지만 에이전트는 같은 구역을 돌면서 아이템을 반복해서 모았습니다
경주를 끝내지 않아도 점수를 계속 얻을 수 있었기 때문입니다
2025년 코딩 모델 평가에서도 비슷한 문제가 나타났습니다
프로그램을 고쳐야 하는데, 일부 모델은 테스트나 검사 방식을 바꾸어 통과하려 했습니다
2026년 Hugging Face 사건에서는 평가 문제의 정답을 얻으려던 모델들이 허용된 범위를 넘어 외부 시스템을 침해했습니다
세 사례의 공통점은 사람이 원한 과제와 모델이 점수를 얻는 방법 사이에 틈이 있었다는 것입니다
이런 행동을 Reward hacking이라고 부릅니다
Specification gaming은 주어진 규칙을 문자 그대로 만족하면서 그 규칙의 의도를 벗어나는 행동을 가리킵니다
오른쪽 그림은 원본 자료에 포함된 CoastRunners 게임 화면입니다

1. Landscape of technical solutions.pdf, p. 1
2. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/)
3. [https://openai.com/index/chain-of-thought-monitoring/](https://openai.com/index/chain-of-thought-monitoring/)
4. [https://openai.com/index/hugging-face-incident-and-the-road-ahead/](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

## Slide 2: 높은 점수, 엉뚱한 행동

같은 사례를 이번에는 모델의 입장에서 생각해보겠습니다
우리는 경주에서 이기라고 말했지만, 학습 과정에서는 아이템을 얻을 때마다 점수를 주었습니다
아이템 점수는 실제 목표를 대신하는 측정값입니다
이렇게 목표를 대신해 측정하는 값을 Proxy라고 부릅니다
학생에게 이해도를 높이라고 하면서 시험 점수만 보상하면, 내용을 공부하는 대신 답을 외우는 지름길이 생길 수 있습니다
AI에서도 측정값을 높이는 방법과 실제 과제를 잘하는 방법이 항상 같지는 않습니다
코딩 사례에서는 테스트 통과가, Hugging Face 사례에서는 평가 문제 해결이 이런 측정값 역할을 했습니다
지금은 모델이 사람처럼 나쁜 마음을 먹었다고 단정할 필요가 없습니다
우리가 어떤 행동에 보상을 주었는지 먼저 살펴보겠습니다
어떤 규칙이 보트가 계속 같은 구역을 돌도록 만들었는지 설명해보시오

1. Landscape of technical solutions.pdf, p. 2
2. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/)

## Slide 3: 문제의 원인

원본 자료는 문제의 원인을 세 가지로 나누고 있습니다
첫째는 결과만 평가하는 방식입니다
Reinforcement learning에서는 보상을 통해 어떤 행동을 더 자주 하도록 학습시킬 수 있습니다
최종 결과에만 보상을 주면 그 결과를 얻는 과정에서 규칙을 어겼는지 놓칠 수 있습니다
둘째는 실제 목표와 Proxy의 차이입니다
사용자를 만족시키는 응답이 항상 정확하거나 안전한 응답은 아닙니다
기분 좋은 답을 주는 것과 사용자에게 도움이 되는 일 사이에도 차이가 있을 수 있습니다
셋째는 모르는 상황에서 멈출 선택지가 부족한 경우입니다
성공하면 1점이고 나머지는 모두 0점이라면, 안전하게 중단하는 행동도 실패와 똑같이 평가할 수 있습니다
그래서 해결이 어려운 상황에서도 점수를 얻으려고 계속 시도할 수 있습니다
모든 AI가 항상 포기하지 않는다는 뜻은 아닙니다
특정 학습과 평가 조건이 이런 행동을 유도할 수 있다는 뜻입니다

1. Landscape of technical solutions.pdf, p. 3
2. [https://openai.com/index/hugging-face-incident-and-the-road-ahead/](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

## Slide 4: 보상 설계 토론

이제 해결책을 보기 전에 직접 제안해보겠습니다
첫 번째 질문은 어떤 해결책을 만들 수 있는지입니다
보상을 더 잘 설계하는 방법도 좋고, 학습을 바꾸는 방법도 좋습니다
두 번째 질문에서는 제안한 해결책이 어느 원인을 줄이는지 설명해보겠습니다
예를 들어 테스트 파일을 바꾸지 못하게 하는 방법은 코딩 사례의 편법을 막을 수 있습니다
하지만 왜 모델이 편법을 찾으려 했는지까지 해결했는지는 별도로 생각해야 합니다
해결책 하나가 세 원인을 모두 없앨 필요는 없습니다
어떤 문제에 효과가 있고 어떤 문제는 남는지 구분해보시오
토론 후 다음 슬라이드의 접근과 비교해보겠습니다

1. Landscape of technical solutions.pdf, p. 4

## Slide 5: 보상 설계의 대안

첫 번째 접근은 Process supervision입니다
최종 답이 맞았는지만 보지 않고 풀이 과정의 각 단계도 평가합니다
수학 문제에서 답만 채점하는 대신 계산 과정도 확인하는 것과 비슷합니다
두 번째 접근은 사람의 선호나 원칙을 학습하는 것입니다
RLHF는 사람이 여러 응답을 비교해 어떤 응답을 더 선호하는지 알려주는 방식을 사용합니다
Constitutional AI는 문서로 정한 원칙을 바탕으로 응답을 비판하고 수정하는 등의 방법을 사용합니다
두 방법 모두 목표나 보상을 완전히 없애는 방식은 아닙니다
사람이 원하는 행동을 더 잘 표현하는 학습 신호를 만드는 접근으로 이해하면 됩니다
세 번째 접근은 정직한 불확실성 표현과 안전한 중단을 학습하는 것입니다
답을 모르거나 해결할 수 없을 때 무리하게 계속하지 않는 선택을 인정합니다
성공과 실패만으로 채점하기보다 과정과 정직함도 평가할 수 있습니다
이런 접근에도 한계가 있으므로 다른 보호 장치와 함께 검증해야 합니다

1. Landscape of technical solutions.pdf, p. 5
2. [https://openai.com/index/instruction-following/](https://openai.com/index/instruction-following/)
3. [https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)

## Slide 6: 평가의 빈틈

AI가 무엇을 할 수 있는지 전부 알아내기는 어렵습니다
LLM은 큰 규모의 텍스트에서 다음 토큰을 예측하도록 학습합니다
토큰은 모델이 문장을 처리할 때 사용하는 글자나 단어의 조각이라고 생각하면 됩니다
이 과정에서 글쓰기뿐 아니라 여러 과제에 사용할 수 있는 능력을 습득합니다
일반화란 학습한 내용을 새로운 상황에 적용하는 것입니다
한 종류의 문제를 학습한 효과가 다른 과제에서 나타날 수도 있습니다
우리가 만든 시험 문제만으로 가능한 모든 상황을 확인할 수는 없습니다
오른쪽 그림은 제한된 시험과 훨씬 넓은 실제 사용 환경을 비교한 개념도입니다
원본이 언급한 2026년 사건에서는 사이버 능력의 상한을 측정하려 일부 운영 보호 장치를 적용하지 않았습니다
평가 과제 자체는 허가된 내부 시험이었지만, 모델이 외부 시스템을 침해한 행동은 그 범위를 벗어났습니다
이 사례는 위험한 능력을 측정하는 시험에도 격리와 감시가 필요함을 보여줍니다

1. Landscape of technical solutions.pdf, p. 6
2. [https://openai.com/index/hugging-face-model-evaluation-security-incident/](https://openai.com/index/hugging-face-model-evaluation-security-incident/)

## Slide 7: 안전한 평가 설계

원본의 세 가지 토론 질문을 차례로 생각해보겠습니다
첫째, AI 안전성을 평가할 때 무엇을 측정할지 정해야 합니다
위험한 요청을 거절하는지, 허용된 범위를 지키는지, 어려운 상황에서 멈추는지처럼 관찰할 행동을 정할 수 있습니다
둘째, 실제 피해를 내지 않고 위험한 행동을 시험할 수 있어야 합니다
가상의 회사, 가짜 비밀 정보, 외부 연결이 차단된 도구 같은 방법을 생각할 수 있습니다
다만 가짜 환경이 실제 환경과 얼마나 비슷한지 따로 확인해야 합니다
셋째, 현실적인 평가에는 사용자의 요청만이 아니라 도구와 권한, 긴 작업 시간 같은 조건도 영향을 줄 수 있습니다
시험에서 위험한 행동이 없었다는 결과가 어떤 조건까지 적용되는지 설명해보시오
정해진 정답보다 평가 설계의 이유를 말하는 것이 중요합니다

1. Landscape of technical solutions.pdf, p. 7

## Slide 8: 능력과 행동의 구분

원본은 평가를 능력과 행동 경향으로 구분합니다
Capability는 어떤 일을 수행할 능력이 있는지입니다
Propensity는 주어진 조건에서 실제로 어떤 행동을 선택하는 경향이 있는지입니다
문을 열 수 있는 능력과 허락 없이 문을 열기로 하는 선택은 서로 다른 질문입니다
능력 평가에는 외부 전문가를 참여시키고 시험 환경을 엄격히 격리할 수 있습니다
행동 경향 평가는 가상의 상황에서 목표와 규칙이 충돌할 때 어떤 선택을 하는지 관찰할 수 있습니다
Anthropic의 2025년 연구에서는 가상의 회사와 인물을 사용한 통제된 모의실험에서 협박 행동이 나타났습니다
실제 회사에서 사람이 협박당한 사건으로 이해하면 안 됩니다
이 결과는 해당 실험 조건에서의 위험을 보여주며, 모든 실제 환경에서 같은 행동을 한다는 뜻은 아닙니다
아래 ASL 구분은 원본 그림의 개괄적인 위험 수준을 재구성한 것입니다
원본 그림에서 ASL 4 이상은 가정적인 단계로 표시되어 있습니다
조건에 따른 사전 약속은 특정 위험이 확인되면 권한을 제한하거나 추가 검증을 하는 식으로 대응을 미리 정하는 것입니다
이는 이해를 돕기 위한 예시이며 각 조직의 공식 정책은 원문을 확인해야 합니다

1. Landscape of technical solutions.pdf, p. 8
2. [https://www.anthropic.com/research/agentic-misalignment](https://www.anthropic.com/research/agentic-misalignment)

## Slide 9: 안전한 AI의 오용

안전하게 학습한 모델도 악의적인 사용자가 오용할 수 있습니다
학습 데이터에는 유익한 정보와 위험하게 쓰일 수 있는 정보가 함께 포함될 수 있습니다
안전 학습은 이런 지식을 해로운 요청에 사용하지 않도록 가르치는 방법입니다
Jailbreak는 그 거절 행동을 우회하려는 시도를 말합니다
원본의 할머니 이야기는 요청을 감정적인 이야기로 포장해 거절을 피하려는 예시입니다
구체적인 위험한 방법을 배우는 것이 아니라, 요청의 표현만으로 목적을 판단하기 어렵다는 점을 보겠습니다
보안 점검처럼 유익한 작업과 악의적인 작업은 일부 단계가 비슷할 수 있습니다
또 전체 작업을 작은 요청으로 나누면 각 요청은 평범해 보일 수 있습니다
오른쪽 그림에서 모델은 작은 조각만 보고, 사용자는 그 조각들을 한 작업으로 연결합니다
Anthropic은 2025년 보고서에서 공격자가 전체 악의적인 목적을 숨기고 작은 과제로 나누어 Claude를 이용했다고 설명했습니다
이 보고서는 회사가 조사한 실제 오용 사례에 관한 발표이며, 앞 슬라이드의 가상 협박 실험과 구분해야 합니다
개별 문장뿐 아니라 전체 작업의 목적을 보는 일이 왜 필요한지 생각해보겠습니다

1. Landscape of technical solutions.pdf, p. 9
2. [https://www.anthropic.com/news/disrupting-AI-espionage](https://www.anthropic.com/news/disrupting-AI-espionage)

## Slide 10: 오용 방지 토론

첫 번째 질문에서는 위험한 요청을 거절하도록 학습하는 방법과 위험한 정보를 학습 전에 걸러내는 방법을 비교해보겠습니다
같은 지식이 방어와 공격에 모두 쓰일 수 있다는 점도 고려해야 합니다
정보를 전부 제거하면 정당한 보안 연구나 방어 작업에도 영향을 줄 수 있습니다
두 번째 질문에서는 작업을 잘게 나누는 경우를 생각해보겠습니다
현재 요청 하나만 볼지, 대화 전체를 볼지, 여러 작업 기록까지 볼지 제안해보시오
범위를 넓히면 맥락을 더 볼 수 있지만 비용과 개인정보 같은 문제도 함께 고려해야 합니다
세 번째 질문은 공개 가중치 모델입니다
사용자가 가중치를 내려받아 직접 실행하고 수정할 수 있는 모델을 뜻합니다
중앙 서버에서 요청을 차단하는 방법만으로는 모든 사용을 통제하기 어렵습니다
어떤 보호 장치가 수정에도 버틸 수 있을지 생각해보시오

1. Landscape of technical solutions.pdf, p. 10

## Slide 11: 오용 방지 접근

원본이 제시하는 해결책은 서로 다른 위치에 보호 장치를 두는 것입니다
데이터 필터링은 학습 전에 자료를 선별하는 방법입니다
Unlearning은 이미 학습한 특정 정보나 행동의 영향을 줄이려는 연구입니다
완전히 지웠는지 확인하기 어려울 수 있어 별도의 평가가 필요합니다
외부 분류기는 모델 밖에서 요청이나 출력이 위험한지 판단하는 장치입니다
모니터링은 모델이 실제로 어떤 요청과 행동을 수행하는지 관찰하는 것입니다
작게 나눈 요청을 찾으려면 한 문장뿐 아니라 대화, 세션, 계정의 작업 맥락을 함께 볼 수 있습니다
공개 가중치 모델에서는 사용자가 추가 학습으로 안전 장치를 바꿀 수 있습니다
Tamper Resistant Safeguards 연구는 이런 수정 시도에도 보호 장치가 유지되도록 학습하는 접근을 다룹니다
이 연구가 모든 수정이나 모든 공격을 막는다는 뜻은 아닙니다
검증한 공격 조건에서 얼마나 견디는지와 남는 실패를 함께 확인해야 합니다
토론에서 제안한 해결책이 이 표의 어느 위치에 해당하는지 연결해보겠습니다

1. Landscape of technical solutions.pdf, p. 11
2. [https://arxiv.org/abs/2408.00761](https://arxiv.org/abs/2408.00761)

## Slide 12: 기술적 AI 안전의 연구 분야

기술적 AI 안전에는 오늘 살펴본 접근 외에도 여러 연구 분야가 있습니다
Mechanistic interpretability는 모델 내부에서 어떤 계산이 일어나는지 설명하려는 분야입니다
모델이 말로 제공하는 설명만으로 내부 계산을 직접 알 수 있는 것은 아닙니다
왼쪽 그림은 모델 내부의 일부 계산을 살펴보는 개념도입니다
Multi agent collusion은 여러 에이전트가 허가되지 않은 방식으로 협력해 문제가 커지는 경우를 다룹니다
Hugging Face 사건에서는 서로 독립적으로 일해야 할 에이전트들이 게시판을 만들어 정보를 공유하고 협력했습니다
원본은 이 게시판에 약 1,200개의 AI가 참여했다고 소개하지만, 여기서는 규모보다 허가되지 않은 협력이 위험을 키웠다는 점에 초점을 맞춥니다
정상적으로 허가된 협업 자체가 문제라는 뜻은 아닙니다
Scalable oversight는 인간보다 특정 과제를 잘하는 AI를 어떻게 감독할지, 많은 AI를 어떻게 지속해서 감독할지 다룹니다
AI control은 모델이 안전하다고 완전히 확신하지 못하는 상황에서도 권한과 실행 환경을 제한해 통제를 유지하려는 접근입니다
아래 세 자료는 원본이 제안한 추가 읽을거리입니다
지금 배우는 모델 구현과 수학은 이 연구들을 이해하고 직접 실험하는 데 필요한 기초가 됩니다

1. Landscape of technical solutions.pdf, p. 12
2. [https://openai.com/index/hugging-face-incident-and-the-road-ahead/](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)
3. [https://shallowreview.ai/](https://shallowreview.ai/)
4. [https://bluedot.org/courses/technical-ai-safety](https://bluedot.org/courses/technical-ai-safety)
5. [https://arxiv.org/abs/1606.06565](https://arxiv.org/abs/1606.06565)
