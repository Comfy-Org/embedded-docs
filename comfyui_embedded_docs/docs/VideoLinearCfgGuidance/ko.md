
VideoLinearCFGGuidance 노드는 비디오 모델에 선형 조건 가이드 스케일을 적용하여, 조건부 및 비조건부 구성 요소의 영향을 지정된 범위 내에서 조정합니다. 이를 통해 생성 프로세스에 대한 동적 제어가 가능하며, 원하는 조건 수준에 따라 모델의 출력을 미세 조정할 수 있습니다.

## 입력

| 매개변수  | 데이터 유형 | 설명                                                                                                                                                                                             |
| --------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`   | MODEL       | 모델 매개변수는 선형 CFG 가이드가 적용될 비디오 모델을 나타냅니다. 이는 가이드 스케일로 수정될 기본 모델을 정의하는 데 중요합니다.                                                               |
| `min_cfg` | `FLOAT`     | min_cfg 매개변수는 적용될 최소 조건 가이드 스케일을 지정하며, 선형 스케일 조정의 시작점을 제공합니다. 이는 가이드 스케일의 하한을 결정하는 데 중요한 역할을 하며, 모델의 출력에 영향을 미칩니다. |

## 출력

| 매개변수 | 데이터 유형 | 설명                                                                                                                                                                |
| -------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`  | MODEL       | 출력은 입력 모델의 수정된 버전으로, 선형 CFG 가이드 스케일이 적용됩니다. 이 조정된 모델은 지정된 가이드 스케일에 따라 다양한 조건 수준의 출력을 생성할 수 있습니다. |
