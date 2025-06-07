ConditioningConcat 노드는 조건 벡터를 연결하도록 설계되었으며, 특히 'conditioning_from' 벡터를 'conditioning_to' 벡터에 병합합니다. 이 작업은 두 소스의 조건 정보를 단일 통합 표현으로 결합해야 하는 시나리오에서 기본적입니다.

## 입력

| 매개변수             | Comfy dtype        | 설명 |
|-----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | 'conditioning_from' 벡터가 연결될 주요 조건 벡터 세트를 나타냅니다. 이는 연결 과정의 기본 역할을 합니다. |
| `conditioning_from`   | `CONDITIONING`     | 'conditioning_to' 벡터에 연결될 조건 벡터로 구성됩니다. 이 매개변수는 추가적인 조건 정보를 기존 세트에 통합할 수 있게 합니다. |

## 출력

| 매개변수            | Comfy dtype        | 설명 |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | 'conditioning_from' 벡터가 'conditioning_to' 벡터에 연결된 결과로, 통합된 조건 벡터 세트가 출력됩니다. |
