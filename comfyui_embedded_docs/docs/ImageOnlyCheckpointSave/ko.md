# 이미지 전용 체크포인트 저장

ImageOnlyCheckpointSave 노드는 모델, CLIP 비전 인코더 및 VAE를 포함하는 체크포인트 파일을 저장합니다. 지정된 파일 이름 접두사를 사용하여 safetensors 파일을 생성하고 출력 디렉토리에 저장합니다. 이 노드는 이미지 관련 모델 구성 요소를 단일 체크포인트 파일에 함께 저장하도록 특별히 설계되었습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 체크포인트에 저장될 모델 | MODEL | 예 | - |
| `clip_vision` | 체크포인트에 저장될 CLIP 비전 인코더 | CLIP_VISION | 예 | - |
| `vae` | 체크포인트에 저장될 VAE(변분 오토인코더) | VAE | 예 | - |
| `filename_prefix` | 출력 파일 이름의 접두사(기본값: "checkpoints/ComfyUI") | STRING | 예 | - |
| `prompt` | 워크플로우 프롬프트 데이터를 위한 숨김 매개변수 | PROMPT | 아니요 | - |
| `extra_pnginfo` | 추가 PNG 메타데이터를 위한 숨김 매개변수 | EXTRA_PNGINFO | 아니요 | - |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| - | 이 노드는 출력을 반환하지 않습니다 | - |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/ko.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
