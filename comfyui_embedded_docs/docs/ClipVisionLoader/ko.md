이 노드는 `ComfyUI/models/clip_vision` 폴더에 있는 모델을 감지하며, 또한 extra_model_paths.yaml 파일에 구성된 추가 경로의 모델도 읽습니다.
때때로 **ComfyUI 인터페이스를 새로 고침**해야 해당 폴더의 모델 파일을 읽을 수 있습니다.

CLIPVisionLoader 노드는 지정된 경로에서 CLIP Vision 모델을 로드하도록 설계되었습니다. CLIP Vision 모델의 위치 지정 및 초기화의 복잡성을 추상화하여, 추가 처리나 추론 작업에 쉽게 사용할 수 있도록 합니다.

## 입력

| 필드        | 데이터 유형   | 설명                                                                                                        |
| ----------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
| `clip_name` | COMBO[STRING] | 로드할 CLIP Vision 모델의 이름을 지정하며, 미리 정의된 디렉토리 구조 내에서 모델 파일을 찾는 데 사용됩니다. |

## 출력

| 필드          | Comfy dtype   | 설명                                                                                            |
| ------------- | ------------- | ----------------------------------------------------------------------------------------------- |
| `clip_vision` | `CLIP_VISION` | 로드된 CLIP Vision 모델로, 이미지 인코딩이나 기타 비전 관련 작업에 사용할 준비가 되어 있습니다. |
