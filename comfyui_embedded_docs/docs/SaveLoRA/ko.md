# LoRA 가중치 저장

SaveLoRA 노드는 LoRA(Low-Rank Adaptation) 모델을 파일로 저장합니다. LoRA 모델을 출력 디렉터리에 `.safetensors` 파일로 기록하며, 파일 이름 접두사와 선택적 단계(step) 수를 지정할 수 있습니다. 단계 수를 제공하면 저장되는 파일 이름에 해당 단계 수가 포함됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `lora` | 저장할 LoRA 모델입니다. LoRA 레이어가 적용된 모델을 사용하지 마십시오. | LORA_MODEL | 예 | N/A |
| `prefix` | 저장될 LoRA 파일에 사용할 접두사입니다 (기본값: "loras/ComfyUI_trained_lora"). | STRING | 예 | N/A |
| `steps` | 선택 사항: LoRA가 학습된 단계 수입니다. 저장된 파일 이름을 지정하는 데 사용됩니다. | INT | 아니요 | N/A |

**참고:** `lora` 입력은 순수 LoRA 모델이어야 합니다. LoRA 레이어가 적용된 기본 모델을 제공하지 마십시오.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| *None* | 이 노드는 워크플로우에 데이터를 출력하지 않습니다. 파일을 디스크에 저장하는 출력 노드입니다. | N/A |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/ko.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
