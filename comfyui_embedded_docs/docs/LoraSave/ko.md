> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/ko.md)

LoraSave 노드는 모델 차이에서 LoRA(Low-Rank Adaptation) 파일을 추출하여 저장합니다. 확산 모델 차이, 텍스트 인코더 차이 또는 둘 다를 처리하여 지정된 순위와 유형의 LoRA 형식으로 변환할 수 있습니다. 생성된 LoRA 파일은 나중에 사용할 수 있도록 출력 디렉터리에 저장됩니다.

## 입력

| 매개변수 | 데이터 유형 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `파일명 접두사` | STRING | 예 | - | 출력 파일 이름의 접두사 (기본값: "loras/ComfyUI_extracted_lora") |
| `순위` | INT | 예 | 1-4096 | LoRA의 순위 값으로, 크기와 복잡성을 제어합니다 (기본값: 8) |
| `LoRA 유형` | COMBO | 예 | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` | 생성할 LoRA 유형 (기본값: "standard") |
| `차이 편향` | BOOLEAN | 예 | - | LoRA 계산에 편향 차이를 포함할지 여부 (기본값: True) |
| `모델 차이` | MODEL | 아니요 | - | LoRA로 변환할 ModelSubtract 출력 |
| `텍스트 인코더 차이` | CLIP | 아니요 | - | LoRA로 변환할 CLIPSubtract 출력 |

**참고:** 노드가 작동하려면 `model_diff` 또는 `text_encoder_diff` 중 하나 이상을 제공해야 합니다. 둘 다 생략하면 노드는 출력을 생성하지 않습니다.

## 출력

| 출력 이름 | 데이터 유형 | 설명 |
|-------------|-----------|-------------|
| - | - | 이 노드는 LoRA 파일을 출력 디렉터리에 저장하지만 워크플로를 통해 데이터를 반환하지는 않습니다 |

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`
