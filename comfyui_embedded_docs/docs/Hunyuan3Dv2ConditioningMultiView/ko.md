> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/ko.md)

Hunyuan3Dv2ConditioningMultiView 노드는 3D 비디오 생성을 위한 다중 뷰 CLIP 비전 임베딩을 처리합니다. 선택적인 전면, 좌측, 후면, 우측 뷰 임베딩을 입력받아 위치 인코딩과 결합하여 비디오 모델용 조건화 데이터를 생성합니다. 이 노드는 결합된 임베딩에서 생성된 긍정 조건화와 제로 값으로 구성된 부정 조건화를 모두 출력합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `앞` | CLIP_VISION_OUTPUT | 아니오 | - | 전면 뷰에 대한 CLIP 비전 출력 |
| `왼쪽` | CLIP_VISION_OUTPUT | 아니오 | - | 좌측 뷰에 대한 CLIP 비전 출력 |
| `뒤` | CLIP_VISION_OUTPUT | 아니오 | - | 후면 뷰에 대한 CLIP 비전 출력 |
| `오른쪽` | CLIP_VISION_OUTPUT | 아니오 | - | 우측 뷰에 대한 CLIP 비전 출력 |

**참고:** 노드가 기능하려면 최소한 하나의 뷰 입력이 제공되어야 합니다. 노드는 유효한 CLIP 비전 출력 데이터를 포함하는 뷰만 처리합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `부정 조건` | CONDITIONING | 위치 인코딩과 결합된 다중 뷰 임베딩을 포함하는 긍정 조건화 |
| `negative` | CONDITIONING | 대조 학습을 위한 제로 값으로 구성된 부정 조건화 |
