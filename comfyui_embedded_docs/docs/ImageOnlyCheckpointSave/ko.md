> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/ko.md)

# ImageOnlyCheckpointSave 노드

ImageOnlyCheckpointSave 노드는 모델, CLIP 비전 인코더 및 VAE가 포함된 체크포인트 파일을 저장합니다. 지정된 파일명 접두사를 사용하여 safetensors 파일을 생성하고 출력 디렉토리에 저장합니다. 이 노드는 이미지 관련 모델 구성 요소를 단일 체크포인트 파일로 함께 저장하도록 특별히 설계되었습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 체크포인트에 저장할 모델 |
| `clip_vision` | CLIP_VISION | 예 | - | 체크포인트에 저장할 CLIP 비전 인코더 |
| `vae` | VAE | 예 | - | 체크포인트에 저장할 VAE(변이형 오토인코더) |
| `filename_prefix` | STRING | 예 | - | 출력 파일명 접두사 (기본값: "checkpoints/ComfyUI") |
| `prompt` | PROMPT | 아니요 | - | 워크플로우 프롬프트 데이터를 위한 숨김 매개변수 |
| `extra_pnginfo` | EXTRA_PNGINFO | 아니요 | - | 추가 PNG 메타데이터를 위한 숨김 매개변수 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| - | - | 이 노드는 출력을 반환하지 않습니다 |

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
