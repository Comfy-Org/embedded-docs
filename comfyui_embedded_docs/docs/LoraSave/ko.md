> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/ko.md)

LoraSave 노드는 모델 간 차이에서 LoRA(Low-Rank Adaptation) 파일을 추출하고 저장합니다. 이 노드는 디퓨전 모델 차이, 텍스트 인코더 차이, 또는 둘 모두를 처리하여 지정된 랭크와 유형으로 LoRA 형식으로 변환할 수 있습니다. 결과 LoRA 파일은 나중에 사용할 수 있도록 출력 디렉토리에 저장됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `filename_prefix` | STRING | 예 | - | 출력 파일 이름의 접두사 (기본값: "loras/ComfyUI_extracted_lora") |
| `rank` | INT | 예 | 1-4096 | LoRA의 랭크 값으로, 크기와 복잡도를 제어합니다 (기본값: 8) |
| `lora_type` | COMBO | 예 | 여러 옵션 사용 가능 | 생성할 LoRA의 유형으로, 다양한 옵션을 사용할 수 있습니다 |
| `bias_diff` | BOOLEAN | 예 | - | LoRA 계산에 바이어스 차이를 포함할지 여부 (기본값: True) |
| `model_diff` | MODEL | 아니오 | - | LoRA로 변환할 ModelSubtract 출력 |
| `text_encoder_diff` | CLIP | 아니오 | - | LoRA로 변환할 CLIPSubtract 출력 |

**참고:** 노드가 기능하려면 `model_diff` 또는 `text_encoder_diff` 중 적어도 하나가 제공되어야 합니다. 둘 다 생략하면 노드는 출력을 생성하지 않습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| - | - | 이 노드는 LoRA 파일을 출력 디렉토리에 저장하지만 워크플로우를 통해 데이터를 반환하지는 않습니다 |