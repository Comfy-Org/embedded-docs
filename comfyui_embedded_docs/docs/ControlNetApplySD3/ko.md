> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/ko.md)

이 노드는 Stable Diffusion 3 조건화에 ControlNet 지도를 적용합니다. 긍정적 및 부정적 조건화 입력과 함께 ControlNet 모델 및 이미지를 받은 다음, 조정 가능한 강도 및 타이밍 매개변수를 사용하여 생성 과정에 영향을 미치는 제어 지도를 적용합니다.

**참고:** 이 노드는 더 이상 사용되지 않는 것으로 표시되었으며 향후 버전에서 제거될 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | ControlNet 지도를 적용할 긍정적 조건화 |
| `negative` | CONDITIONING | 예 | - | ControlNet 지도를 적용할 부정적 조건화 |
| `control_net` | CONTROL_NET | 예 | - | 지도에 사용할 ControlNet 모델 |
| `vae` | VAE | 예 | - | 과정에서 사용되는 VAE 모델 |
| `image` | IMAGE | 예 | - | ControlNet이 지도로 사용할 입력 이미지 |
| `strength` | FLOAT | 예 | 0.0 - 10.0 | ControlNet 효과의 강도 (기본값: 1.0) |
| `start_percent` | FLOAT | 예 | 0.0 - 1.0 | ControlNet 적용이 시작되는 생성 과정의 지점 (기본값: 0.0) |
| `end_percent` | FLOAT | 예 | 0.0 - 1.0 | ControlNet 적용이 중단되는 생성 과정의 지점 (기본값: 1.0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | ControlNet 지도가 적용된 수정된 긍정적 조건화 |
| `negative` | CONDITIONING | ControlNet 지도가 적용된 수정된 부정적 조건화 |