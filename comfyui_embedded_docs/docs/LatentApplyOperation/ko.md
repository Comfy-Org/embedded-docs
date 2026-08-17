# 잠재 데이터 연산 (연산 적용)

LatentApplyOperation 노드는 잠재 샘플에 지정된 연산을 적용합니다. 이 노드는 잠재 데이터와 연산을 입력으로 받아 입력 잠재 샘플을 복사하고, 연산을 잠재 텐서에 적용한 후 수정된 잠재 데이터를 반환합니다. 이 노드를 사용하면 워크플로우에서 잠재 표현을 변환하거나 조작할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `samples` | 연산으로 처리될 잠재 샘플입니다. | LATENT | 예 | - |
| `operation` | 잠재 샘플에 적용할 연산입니다. | LATENT_OPERATION | 예 | - |

참고: 이 노드는 실험적인 기능으로 표시되어 있습니다. 이 연산은 잠재 구조의 `samples` 키 아래에 저장된 잠재 텐서에 적용됩니다. 연산이 적용되기 전에 입력 잠재 샘플이 복사되므로 원래 입력 잠재 데이터는 수정되지 않습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 연산 적용 후 수정된 잠재 샘플입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/ko.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
