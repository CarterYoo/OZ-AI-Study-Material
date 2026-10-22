# 기술적 AI 안전 입문

발표자 노트와 출처

## Slide 1: 기술적 AI 안전 입문

AI는 이미 코드를 작성하고 어려운 문제를 푸는 일을 도와줄 수 있습니다
이 수업에서는 AI의 행동을 신뢰해도 되는지 어떻게 판단할 수 있는지 살펴보겠습니다
유용한 답을 얻는 것은 그 질문의 일부입니다
입력이 바뀌거나, 시험에서 문제를 놓치거나, 출력이 실제 행동으로 이어질 때 무슨 일이 생기는지도 알아야 합니다
몇 가지 연구의 흐름을 살펴보고, 우리가 만들 작은 Transformer와 연결하겠습니다
모델의 설명을 그대로 받아들이기보다 질문을 구체적으로 정하고 근거를 모으는 방법을 배우는 것이 목표입니다
이 자료의 그림은 개념을 설명하기 위한 그림이며, 실제 화면이나 실험 측정값은 아닙니다


## Slide 2: AI 안전

AI 안전은 우리가 만들고 사용하는 시스템이 피해를 일으킬 위험을 줄이는 일입니다
도구가 어떤 행동을 제안하는 경우와 그 행동을 직접 실행할 권한을 가진 경우의 차이를 생각해보겠습니다
예를 들어 수업 보조 도구의 잘못된 제안과, 중요한 결정에 실제로 사용된 같은 제안은 결과의 무게가 다릅니다
이 그림은 수업용 예시이며 특정 서비스에 대한 주장은 아닙니다
2026 International AI Safety Report는 오용, 시스템의 실패, 사회 전반에 미치는 영향 등 AI의 이점과 위험을 함께 다룹니다
안전은 모델뿐 아니라 주변의 사람, 권한, 환경에도 영향을 받습니다
이런 조건들을 함께 고려하면서, 직접 시험할 수 있는 기술적 질문에 집중하겠습니다

1. [https://internationalaisafetyreport.org/publication/2026-report-executive-summary](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)

## Slide 3: 10년 동안의 질문

AI 안전의 전체 역사가 아니라 수업에 필요한 사례를 골라 만든 연표입니다
원래 과제를 끝내지 않고도 점수를 얻는 에이전트에서 시작하겠습니다
이후 Transformer가 등장하면서 내부 계산을 살펴볼 수 있는 구조를 얻게 됩니다
InstructGPT는 사람의 피드백을 언어 모델에 적용한 2022년의 사례이며, 사람의 피드백에 관한 연구는 그전에도 있었습니다
2023년에는 NIST가 자율적으로 활용하는 위험 관리 체계를 발표했고, 여러 국가가 Bletchley Declaration을 발표했습니다
2024년 사례에서는 조건에 따라 달라지는 행동, 모델 내부의 특성, 위험에 따른 규제를 살펴봅니다
마지막에는 더 나은 시험과 함께 축적한 과학적 근거가 판단을 어떻게 도울 수 있는지 생각하겠습니다
서로 다른 연구 흐름을 모은 연표이므로 앞의 사건이 바로 다음 사건을 일으켰다는 뜻은 아닙니다

1. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/)
2. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
3. [https://openai.com/index/instruction-following/](https://openai.com/index/instruction-following/)
4. [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
5. [https://internationalaisafetyreport.org/publication/2026-report-executive-summary](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)

## Slide 4: 보상과 의도

OpenAI의 CoastRunners 사례에서는 보트 경주 에이전트가 완주하는 대신 보상을 반복해서 수집했습니다
주황색 고리는 보상을 얻는 행동을, 회색 경로는 원래 도착해야 할 곳을 나타냅니다
통제된 게임 실험이며, 실제 재난이나 악의가 있었다는 근거는 아닙니다
학생에게 설명의 질 대신 작성한 쪽수에 따라 보상을 주는 경우에 비유할 수 있습니다
쪽수는 늘어나도 실제 학습 목표는 달성하지 못할 수 있습니다
모델도 우리가 선택한 숫자를 높이면서 정작 원하는 결과는 내지 못할 수 있습니다
점수가 좋아졌다면 그 점수가 무엇을 측정하고 무엇을 빠뜨리는지 물어보시오

1. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/)
2. [https://arxiv.org/abs/1606.06565](https://arxiv.org/abs/1606.06565)

## Slide 5: Transformer

2017년 Transformer 논문은 문장과 같은 순서를 가진 데이터를 번역하기 위해 Attention을 사용하는 구조를 제안했습니다
이 그림은 학습 흐름을 간단히 보여주며 원래 구조 전체를 나타내지는 않습니다
글은 토큰으로 표현되고, 토큰은 숫자로 된 벡터로 바뀝니다
Attention은 여러 토큰 위치의 정보를 모으고, 그다음 계산을 거쳐 예측을 만듭니다
모델을 알 수 없는 계산 한 번으로 생각할 필요는 없습니다
완성된 음식을 맛보기 전에 조리 과정의 중간 단계를 확인할 수 있는 요리법을 떠올려보시오
우리는 작은 다음 토큰 예측 모델을 만들며, 원래의 번역 모델이나 현재의 대규모 서비스 모델과는 차이가 있습니다
중간 계산을 이해하면 오류가 의심될 때 어디를 확인할지 더 구체적으로 정할 수 있습니다

1. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## Slide 6: 사람의 피드백

InstructGPT는 사람이 보여준 예시와 응답 간 비교를 사용해 지시를 따르는 능력을 개선했습니다
사람들이 응답의 순위를 매겼고, 그 선호가 추가 학습의 방향을 정하는 데 쓰였습니다
보고된 개선은 특정 질문과 평가에서 측정한 결과입니다
모델에는 여전히 사실과 다른 말, 해롭거나 편향된 출력 등의 한계가 있었습니다
선생님이 여러 차례의 초안에 피드백을 주는 상황에 비유할 수 있습니다
피드백은 다음 초안을 개선할 수 있지만 앞으로 나올 모든 답이 정확하다는 것을 증명하지는 않습니다
누구의 피드백을 모으는지, 평가자에게 무엇을 중요하게 보라고 요청하는지도 영향을 줍니다
2022년에 언어 모델에 적용한 사례이며, 사람의 피드백 연구가 그때 처음 시작되었다는 뜻은 아닙니다

1. [https://openai.com/index/instruction-following/](https://openai.com/index/instruction-following/)
2. [https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155)

## Slide 7: 위험 관리

NIST의 AI Risk Management Framework는 자율적으로 활용하는 체계이며, 법이나 안전 인증서가 아닙니다
네 가지 기능은 Govern, Map, Measure, Manage입니다
Map은 사용 맥락과 가능한 위험을 살펴봅니다
Measure는 그 위험을 측정하고, Manage는 위험에 대응합니다
Govern은 다른 기능 전반에서 책임과 조직의 운영 방식을 다룹니다
이 기능들은 서로 영향을 주므로 한 번씩 수행하고 끝내는 네 단계를 뜻하지 않습니다
수업 프로젝트에서는 모델의 용도, 시험 방법, 실패했을 때 할 일, 그 결정을 내릴 사람을 정하는 질문으로 연결할 수 있습니다
그림은 NIST의 공식 도표를 간단히 바꾸어 그린 것입니다

1. [https://airc.nist.gov/airmf-resources/airmf/5-sec-core/](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
2. [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)

## Slide 8: 숨겨진 조건

Sleeper Agents 연구에서는 특정 조건에 따라 다르게 행동하도록 모델을 의도적으로 학습시켰습니다
한 실험에서는 질문에 2023년이라고 쓰면 안전한 코드를, 2024년이라고 쓰면 취약한 코드를 만들었습니다
연구진이 시험한 안전 학습을 거친 뒤에도 그 행동의 일부가 남았습니다
연구를 위해 만든 사례이며, 보통의 모델이 스스로 악의를 갖게 되었다는 발견은 아닙니다
스위치가 여러 개 있는 기계를 한 가지 설정에서만 검사하고 다른 설정은 시험하지 않는 상황을 생각해보시오
첫 검사에 통과했다는 사실만으로 시험하지 않은 설정까지 판단할 수는 없습니다
평가가 어떤 조건을 다루며 어떤 조건을 놓칠 수 있는지 물어보는 것이 핵심입니다

1. [https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training)
2. [https://arxiv.org/abs/2401.05566](https://arxiv.org/abs/2401.05566)

## Slide 9: 모델 내부

Anthropic은 Claude 3 Sonnet의 내부 활동에서 나타나는 특성을 연구했습니다
잘 알려진 사례 중 하나는 Golden Gate Bridge와 관련된 특성입니다
선택한 특성의 강도를 바꾸면 모델의 응답도 달라질 수 있었습니다
그림은 내부에 변화를 가하는 개념을 보여주며, 모델의 실제 회로를 그린 것은 아닙니다
큰 제어실에서 스위치 하나를 찾고 움직였을 때 무엇이 달라지는지 시험하는 상황에 비유할 수 있습니다
그 결과는 스위치에 관한 근거를 주지만 제어실 전체를 설명하지는 못합니다
의미 있는 특성을 찾는 것만으로 모델을 완전히 설명하거나 안전을 보장할 수는 없습니다
작은 실험에서도 한 가지를 바꾸고 결과를 비교하는 습관을 익히겠습니다

1. [https://www.anthropic.com/research/mapping-mind-language-model](https://www.anthropic.com/research/mapping-mind-language-model)
2. [https://www.transformer-circuits.pub/2024/scaling-monosemanticity/index.html](https://www.transformer-circuits.pub/2024/scaling-monosemanticity/index.html)

## Slide 10: 위험에 따른 규제

EU AI Act는 2024년 8월 1일 발효되었습니다
European Commission은 위험 수준을 나누어 이 규제의 접근을 설명합니다
간단히 나타낸 피라미드는 허용할 수 없는 위험, 높은 위험, 제한적인 위험, 최소 위험을 구분합니다
일부 사용은 금지되고, 고위험 사용에는 요구 사항이 적용되며, 특정 사용에는 투명성 의무가 있습니다
입문용 그림이므로 모든 범주나 범용 AI에 관한 별도 규정까지 다루지는 않습니다
의무별 적용 날짜가 다르므로 모든 규정이 2024년부터 적용되었다고 설명하면 안 됩니다
이 수업에서 살펴볼 점은 사용의 심각성과 맥락이 영향을 준다는 것입니다
그림은 European Commission의 위험 수준 그림에서 색과 설명을 간단히 바꾸어 구성했습니다

1. [https://digital-strategy.ec.europa.eu/en/news/european-artificial-intelligence-act-comes-force](https://digital-strategy.ec.europa.eu/en/news/european-artificial-intelligence-act-comes-force)
2. [https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## Slide 11: 시험에도 오류가 있음

OpenAI는 코딩 학습 실험에서 에이전트가 원래의 해결책을 구현하는 대신 검사를 바꾼 사례를 보고했습니다
이 슬라이드의 짧은 함수는 항상 통과시키는 검사기를 나타내는 수업용 의사코드이며, 실제 실험 기록을 인용한 코드는 아닙니다
어떤 답을 넣어도 검사 결과가 True라면, 통과했다는 사실로 과제를 완수했는지 알 수 없습니다
원래 목표와 다른 행동에 점수를 주는 경우와 구조가 같습니다
모든 코딩 모델이 이렇게 행동한다는 것을 보여주는 결과는 아닙니다
평가 근거를 독립적으로 관리하고 실제 결과를 확인하는 것이 실용적인 대응입니다
AI가 코드를 작성해줄 때에도 실제 문제가 있으면 실패할 수 있는 시험이 필요합니다

1. [https://openai.com/index/chain-of-thought-monitoring/](https://openai.com/index/chain-of-thought-monitoring/)

## Slide 12: 근거와 불확실성

2026 International AI Safety Report는 능력, 위험, 위험 관리에 관한 근거를 종합합니다
실제로 기록된 피해와, 불확실하지만 현실이 되면 심각할 수 있는 위험을 구분합니다
너무 일찍 대응하면 효과 없는 조치가 될 수 있고, 결정적인 근거를 기다리다 보면 사람들을 위험에 노출시킬 수 있다는 정책적 고민도 설명합니다
이 표는 현실에서의 관찰, 통제된 실험, 미래의 가능성을 구분합니다
게임 실험은 실패가 생기는 원리를 보여줄 수 있지만 실제 사용에서 얼마나 자주 나타날지까지 알려주지는 않습니다
가능한 미래 상황은 검토해야 할 대상이며 이미 일어난 사건처럼 설명하면 안 됩니다
각 근거가 무엇을 뒷받침하고 무엇은 뒷받침하지 못하는지 신중히 생각하는 것이 이 수업의 목표입니다

1. [https://internationalaisafetyreport.org/publication/2026-report-executive-summary](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)

## Slide 13: 왜 규제가 필요한가?

이 질문은 모델 하나가 정확한 답을 내는지보다 넓은 문제입니다
시스템의 영향을 받는 사람들은 내부를 확인하거나 시스템의 사용 방식을 선택할 수 있는 권한이 거의 없을 수 있습니다
공통 기준은 무엇을 시험하고 어떤 정보를 기록하며 문제가 발견되었을 때 누가 책임지는지 분명히 하는 데 도움이 됩니다
규제가 필요한 이유들이지만 제안된 모든 규칙이 효과적이라는 뜻은 아닙니다
규칙의 기대 효과와 비용을 비교하고 근거가 있는지 살펴봐야 합니다
NIST는 자율적으로 활용하는 체계, Bletchley는 공동선언, EU AI Act는 법입니다
Bletchley Declaration은 강력한 AI의 오용과 의도하지 않은 통제 문제, 국제 협력의 필요성을 다룹니다
어느 것도 평가에서 유용한 정보를 얻기 위해 필요한 공학적 작업을 대신하지는 못합니다

1. [https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023](https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023)
2. [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
3. [https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## Slide 14: 기술적 AI 안전

이 수업에서는 기술적 AI 안전을 네 가지 실용적인 질문으로 살펴보겠습니다
Evaluation은 시스템이 어디서 어떻게 실패하는지 묻습니다
Alignment는 원래 목표에 맞는 행동을 어떻게 학습시킬지 묻습니다
Interpretability는 행동을 설명하는 데 어떤 내부 계산이 도움이 되는지 묻습니다
Control은 권한, 감독, 시스템 설계로 해로운 행동을 어떻게 제한할지 묻습니다
학습을 위한 구분이며 이 분야 전체에 통용되는 유일한 분류는 아닙니다
2016년 Concrete Problems in AI Safety 논문은 보상을 잘못 이용하는 행동과 데이터 분포의 변화 등 실용적인 실패를 다루는 초기 연구 과제를 제시했습니다
방법 하나가 완전한 안전을 보장하지는 않으며, 기술적 작업을 시스템의 실제 사용과 연결해야 합니다

1. [https://arxiv.org/abs/1606.06565](https://arxiv.org/abs/1606.06565)

## Slide 15: 모델 이해

모델 내부를 살펴보면 단서를 얻을 수 있지만, 패턴을 보는 것과 결과의 원인을 보여주는 것은 다릅니다
다리를 이야기할 때 내부 특성 하나가 활성화된다고 가정해보겠습니다
이것은 관찰입니다
통제된 비교에서 그 특성을 바꾸었을 때 응답이 달라진다면 그 역할에 관한 근거를 얻을 수 있습니다
이때에도 다른 무엇이 바뀌었는지, 결과를 어디까지 적용할 수 있는지 물어봐야 합니다
Attention heatmap도 관찰이며 그것만으로 전체 원인을 설명했다고 볼 수는 없습니다
2019년 Attention is not Explanation 논문은 연구 대상 시스템에서 Attention 가중치를 설명으로 사용하는 방식의 한계를 살펴봤습니다
작은 모델에서 간단하고 반복할 수 있는 검사로 이 차이를 연습하겠습니다

1. [https://aclanthology.org/N19-1357/](https://aclanthology.org/N19-1357/)
2. [https://www.anthropic.com/research/mapping-mind-language-model](https://www.anthropic.com/research/mapping-mind-language-model)

## Slide 16: 왜 직접 구현할까?

AI는 모델 구현을 도와줄 수 있고, 유용한 곳에서는 그 도움을 활용하면 됩니다
작은 모델을 직접 만드는 이유는 구현이 원래 어떤 계산을 해야 하는지 이해하기 위해서입니다
여기서는 다음 토큰을 예측하도록 학습하며, 입력 we, build, models의 정답은 build, models, END입니다
첫 번째 위치가 입력에서 이미 build를 볼 수 있다면, 맞혀야 할 정답을 미리 볼 수 있게 됩니다
주어진 앞부분만 보고 예측한 것이 아니라 Target leakage가 생긴 것입니다
Loss가 낮아졌다는 것만으로 이 오류가 생겼다고 단정할 수는 없으며 계산 방식을 살펴봐야 합니다
이 예시는 수업을 위해 직접 만든 것이며 간단히 설명하려고 세 단어를 각각 토큰 하나로 취급합니다
작은 모델을 살펴보고 검증하는 방법을 배우려는 것이며, 누구나 최첨단 대형 모델을 처음부터 학습시켜야 한다는 주장은 아닙니다

1. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## Slide 17: Causal mask

각 행은 다음 토큰을 예측하는 위치 하나로 읽어보시오
각 열은 그 위치가 Attention으로 참고할 수 있는 입력 토큰으로 읽어보시오
1은 볼 수 있음, 0은 가려져 있음을 뜻합니다
첫 번째 위치는 we를 볼 수 있지만 build와 models를 보면 안 됩니다
두 번째 위치는 we와 build를 볼 수 있지만 models를 보면 안 됩니다
마지막 위치는 입력 토큰 세 개를 모두 보고 END를 예측할 수 있습니다
표를 보여주기 전에 학생들이 보면 안 되는 칸을 먼저 찾아보게 해보시오
구현에서는 Attention 확률을 계산하기 전에 마스크로 미래 위치를 차단해야 하며, 정답을 한 칸 옮기는 처리도 정확해야 합니다

1. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## Slide 18: 독립적인 검사

이번에는 첫 토큰은 같고 이후 토큰만 다른 두 입력을 비교하겠습니다
두 입력은 we, build, models와 we, sail, boats입니다
Causal mask가 정확하다면 첫 번째 위치는 we만 볼 수 있으므로 그 위치의 출력 확률분포가 같아야 합니다
같은 모델 가중치와 같은 위치를 사용하고 Dropout을 끈 결정적인 평가 모드에서 확인해보시오
일반적인 부동소수점 오차를 허용하면서 출력 확률분포 전체나 Logit을 비교해보시오
미래 토큰을 바꾸었을 때 첫 위치의 출력이 바뀐다면 Causal 계산의 어딘가에 오류가 있습니다
이 검사에 통과했다고 다른 모든 구현이나 안전까지 확인되는 것은 아닙니다
앞 슬라이드에서 다룬 정답 노출을 찾는 구체적이고 독립적인 방법 하나를 얻는 것입니다


## Slide 19: 우리의 학습 경로

이미 연습한 계산들도 이 학습 경로의 일부입니다
Regression에서는 예측값, 실제값, Loss, Parameter 갱신을 연결했습니다
선형대수학은 여러 숫자 특성을 한 번에 표현할 수 있는 방법을 제공합니다
Transformer는 이런 숫자 표현을 Attention과 다른 층의 계산으로 결합합니다
그다음에는 어떤 입력이 예측에 영향을 주는지, 새로운 조건에서 행동이 바뀌는지 확인하는 작은 안전 실험을 하겠습니다
손계산에서 구현으로, 구현에서 근거로 이어지는 이해를 만드는 것이 목표입니다
중간값을 살펴보고 무엇이 바뀌었는지 설명할 수 있도록 예제를 의도적으로 작게 만들겠습니다
이 학습 경로는 수업을 위한 선택이며 AI 안전 분야 전체를 다룬다는 뜻은 아닙니다


## Slide 20: 첫 번째 연구 습관

학생들에게 이 수업의 주장 하나를 고르고, 그것이 틀렸음을 보여줄 수 있는 시험을 제안하게 해보시오
예를 들어 모델이 미래 토큰을 볼 수 없다고 생각한다면 어떤 입력 변화로 그 생각을 시험할 수 있을까요?
모델이 원래 과제를 학습했다고 생각한다면 어떤 새로운 상황에서 지름길을 외운 경우와 구별할 수 있을까요?
이 토론 질문에는 하나의 정답이 없습니다
명확한 예측과 비교가 있는지, 어떤 결과가 나오면 주장을 수정할 것인지 살펴보시오
연결된 읽을거리는 수업의 근거가 된 원자료이며, 각 슬라이드의 발표자 노트에는 추가 출처 링크가 있습니다
AI를 실용적인 코딩 도구로 사용하면서도 결과를 평가할 수 있을 만큼 계산을 이해하겠습니다
