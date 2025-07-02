이 노드는 `ComfyUI/models/clip_vision` 폴더에 있는 모델을 자동으로 감지하며, `extra_model_paths.yaml` 파일에 구성된 추가 경로의 모델도 읽습니다. ComfyUI를 시작한 후에 모델을 추가했다면, **ComfyUI 인터페이스를 새로 고침**하여 최신 모델 파일 목록을 확인하세요.

## 입력

| 필드         | 데이터 유형     | 설명 |
|--------------|----------------|------|
| CLIP 파일명  | COMBO[STRING]  | `ComfyUI/models/clip_vision` 폴더 내의 모든 지원되는 모델 파일을 나열합니다. |

## 출력

| 필드         | 데이터 유형   | 설명 |
|--------------|--------------|------|
| clip_vision  | CLIP_VISION  | 이미지 인코딩이나 기타 비전 관련 작업에 사용할 수 있는 로드된 CLIP Vision 모델입니다. |
