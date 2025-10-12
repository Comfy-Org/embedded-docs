> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/ko.md)

LoraModelLoader 노드는 학습된 LoRA(Low-Rank Adaptation) 가중치를 디퓨전 모델에 적용합니다. 이 노드는 학습된 LoRA 모델에서 LoRA 가중치를 로드하고 그 영향력을 조정하여 기본 모델을 수정합니다. 이를 통해 디퓨전 모델의 동작을 처음부터 재학습하지 않고도 사용자 정의할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | LoRA를 적용할 디퓨전 모델입니다. |
| `lora` | LORA_MODEL | 예 | - | 디퓨전 모델에 적용할 LoRA 모델입니다. |
| `strength_model` | FLOAT | 예 | -100.0 ~ 100.0 | 디퓨전 모델을 수정할 강도입니다. 이 값은 음수일 수 있습니다 (기본값: 1.0). |

**참고:** `strength_model`이 0으로 설정되면, 노드는 LoRA 수정을 적용하지 않고 원본 모델을 반환합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | LoRA 가중치가 적용된 수정된 디퓨전 모델입니다. |
