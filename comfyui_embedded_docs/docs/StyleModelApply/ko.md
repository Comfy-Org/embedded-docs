
이 노드는 주어진 컨디셔닝에 스타일 모델을 적용하여 CLIP 비전 모델의 출력에 기반해 스타일을 향상시키거나 변경하도록 설계되었습니다. 스타일 모델의 컨디셔닝을 기존 컨디셔닝에 통합하여 생성 과정에서 스타일이 매끄럽게 혼합되도록 합니다.

## 입력

### 필수

| 매개변수             | Comfy dtype          | 설명 |
|-----------------------|-----------------------|-------------|
| `conditioning`        | `CONDITIONING`       | 스타일 모델의 컨디셔닝이 적용될 원래의 컨디셔닝 데이터입니다. 이는 향상되거나 변경될 기본 컨텍스트나 스타일을 정의하는 데 중요합니다. |
| `style_model`         | `STYLE_MODEL`        | CLIP 비전 모델의 출력에 기반하여 새로운 컨디셔닝을 생성하는 데 사용되는 스타일 모델입니다. 적용될 새로운 스타일을 정의하는 데 중요한 역할을 합니다. |
| `clip_vision_output`  | `CLIP_VISION_OUTPUT` | 스타일 모델이 새로운 컨디셔닝을 생성하는 데 사용하는 CLIP 비전 모델의 출력입니다. 스타일 적용에 필요한 시각적 컨텍스트를 제공합니다. |

## 출력

| 매개변수            | Comfy dtype           | 설명 |
|----------------------|-----------------------|-------------|
| `conditioning`       | `CONDITIONING`        | 스타일 모델의 출력을 통합하여 향상되거나 변경된 컨디셔닝입니다. 추가 처리나 생성을 위해 준비된 최종 스타일 컨디셔닝을 나타냅니다. |
