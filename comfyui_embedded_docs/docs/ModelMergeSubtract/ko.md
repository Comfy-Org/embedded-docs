
이 노드는 고급 모델 병합 작업을 위해 설계되었으며, 특정 배수를 기반으로 한 모델의 매개변수를 다른 모델에서 빼는 기능을 제공합니다. 이는 한 모델의 매개변수가 다른 모델에 미치는 영향을 조정하여 새로운 하이브리드 모델을 생성할 수 있도록 모델 동작을 사용자 정의할 수 있게 합니다.

## 입력

| 매개변수     | 데이터 유형 | 설명                                                                   |
| ------------ | ----------- | ---------------------------------------------------------------------- |
| `model1`     | `MODEL`     | 매개변수가 빼질 기본 모델입니다.                                       |
| `model2`     | `MODEL`     | 기본 모델에서 매개변수가 빼질 모델입니다.                              |
| `multiplier` | `FLOAT`     | 기본 모델의 매개변수에 대한 빼기 효과를 조정하는 부동 소수점 값입니다. |

## 출력

| 매개변수 | 데이터 유형 | 설명                                                                   |
| -------- | ----------- | ---------------------------------------------------------------------- |
| `model`  | MODEL       | 한 모델의 매개변수를 다른 모델에서 빼고 배수로 조정한 결과 모델입니다. |
