> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/ko.md)

ImageOnlyCheckpointSave 노드는 모델, CLIP 비전 인코더, VAE를 포함하는 체크포인트 파일을 저장합니다. 지정된 파일명 접두사를 사용하여 safetensors 파일을 생성하고 출력 디렉토리에 저장합니다. 이 노드는 이미지 관련 모델 구성 요소들을 단일 체크포인트 파일에 함께 저장하도록 특별히 설계되었습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 체크포인트에 저장될 모델 |
| `clip_vision` | CLIP_VISION | 예 | - | 체크포인트에 저장될 CLIP 비전 인코더 |
| `vae` | VAE | 예 | - | 체크포인트에 저장될 VAE(변분 자동인코더) |
| `filename_prefix` | STRING | 예 | - | 출력 파일명의 접두사 (기본값: "checkpoints/ComfyUI") |
| `prompt` | PROMPT | 아니오 | - | 워크플로우 프롬프트 데이터를 위한 숨겨진 매개변수 |
| `extra_pnginfo` | EXTRA_PNGINFO | 아니오 | - | 추가 PNG 메타데이터를 위한 숨겨진 매개변수 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| - | - | 이 노드는 어떠한 출력도 반환하지 않습니다 |