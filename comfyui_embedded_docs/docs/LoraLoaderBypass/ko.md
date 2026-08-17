# LoRA 불러오기 (바이패스) (디버깅용)

LoraLoaderBypass 노드는 특별한 바이패스 모드에서 LoRA(저랭크 적응, Low-Rank Adaptation)를 확산 모델과 CLIP 모델에 적용합니다. 일반적인 LoRA 로더와 달리 기본 모델 가중치를 영구적으로 수정하지 않습니다. 대신 LoRA의 효과를 모델의 일반적인 정방향 패스에 추가하므로, 학습 중이거나 가중치가 오프로드된 모델을 작업할 때 유용합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | LoRA가 적용될 확산 모델입니다. | MODEL | 예 | N/A |
| `clip` | LoRA가 적용될 CLIP 모델입니다. | CLIP | 예 | N/A |
| `lora_name` | 적용할 LoRA 파일의 이름입니다. 옵션은 `loras` 폴더에서 불러옵니다. | COMBO | 예 | 사용 가능한 LoRA 파일 목록 |
| `strength_model` | 확산 모델을 수정하는 강도를 설정합니다. 이 값은 음수가 될 수 있습니다(기본값: 1.0). | FLOAT | 예 | -100.0 to 100.0 |
| `strength_clip` | CLIP 모델을 수정하는 강도를 설정합니다. 이 값은 음수가 될 수 있습니다(기본값: 1.0). | FLOAT | 예 | -100.0 to 100.0 |

**참고:** `strength_model`과 `strength_clip`이 모두 0으로 설정된 경우, 이 노드는 아무런 처리도 하지 않고 원본의 수정되지 않은 `model` 및 `clip` 입력을 반환합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `MODEL` | 바이패스 모드로 LoRA가 적용된 확산 모델입니다. | MODEL |
| `CLIP` | 바이패스 모드로 LoRA가 적용된 CLIP 모델입니다. | CLIP |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/ko.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
