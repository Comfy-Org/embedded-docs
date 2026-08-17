# LoRA 모델 로드

LoraModelLoader 노드는 학습된 LoRA(Low-Rank Adaptation) 가중치를 확산 모델에 적용합니다. 학습된 LoRA 모델에서 LoRA 가중치를 로드하고 영향 강도를 조정하여 기본 모델을 수정합니다. 이를 통해 확산 모델을 처음부터 다시 학습시키지 않고도 동작을 사용자 지정할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | LoRA가 적용될 확산 모델입니다. | MODEL | 예 | - |
| `lora` | 확산 모델에 적용할 LoRA 모델입니다. | LORA_MODEL | 예 | - |
| `strength_model` | 확산 모델을 수정하는 강도입니다. 이 값은 음수일 수 있습니다(기본값: 1.0). | FLOAT | 예 | -100.0 to 100.0 |
| `bypass` | 활성화하면 기본 모델 가중치를 수정하지 않고 LoRA를 바이패스 모드로 적용합니다. 학습 중이거나 모델 가중치를 오프로드한 경우에 유용합니다(기본값: False). | BOOLEAN | 예 | True or False |

**참고:** `strength_model`이 0으로 설정된 경우, 노드는 LoRA 수정을 적용하지 않고 원래 모델을 반환합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model` | 수정된 확산 모델입니다. | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/ko.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
