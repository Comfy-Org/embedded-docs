이 노드는 두 개의 조건 입력을 하나의 출력으로 결합하여 정보를 효과적으로 병합합니다.

## 입력

| 매개변수            | Comfy dtype        | 설명 |
|----------------------|--------------------|-------------|
| `conditioning_1`      | `CONDITIONING`     | 결합될 첫 번째 조건 입력입니다. 결합 과정에서 `conditioning_2`와 동등한 역할을 합니다. |
| `conditioning_2`      | `CONDITIONING`     | 결합될 두 번째 조건 입력입니다. 병합 과정에서 `conditioning_1`과 동등하게 중요합니다. |

## 출력

| 매개변수            | Comfy dtype        | 설명 |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | `conditioning_1`과 `conditioning_2`를 결합한 결과로, 병합된 정보를 포함합니다. |
