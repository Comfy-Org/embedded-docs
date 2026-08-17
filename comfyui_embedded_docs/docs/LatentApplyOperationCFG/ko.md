# 잠재 데이터 CFG 연산 (연산 적용)

LatentApplyOperationCFG 노드는 모델의 컨디셔닝 유도 과정을 수정하기 위해 잠재 연산을 적용합니다. 이 노드는 classifier-free guidance(CFG) 샘플링 과정에서 컨디셔닝 출력을 가로채고, 생성에 사용되기 전에 잠재 표현에 지정된 연산을 적용하는 방식으로 작동합니다.

모델이 두 개의 컨디셔닝 출력(예: 양성 및 음성 컨디셔닝)을 생성하는 경우, 연산은 두 출력 간의 차이에 적용된 후 두 번째 컨디셔닝이 다시 더해집니다. 컨디셔닝 출력이 하나뿐인 경우에는 해당 출력에 직접 연산이 적용됩니다. 이 노드는 실험적인 것으로 표시되어 있습니다.

## 입력

| 파라미터 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | CFG 연산이 적용될 모델 | MODEL | 예 | - |
| `operation` | CFG 샘플링 과정 중 적용할 잠재 연산 | LATENT_OPERATION | 예 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 샘플링 프로세스에 CFG 연산이 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/ko.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
