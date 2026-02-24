> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon%20Scaling/ko.md)

이 노드는 연구 논문 "Elucidating the Exposure Bias in Diffusion Models"의 Epsilon Scaling 방법을 구현합니다. 샘플링 과정에서 예측된 노이즈를 스케일링하여 노출 편향(Exposure Bias)을 줄이는 데 도움을 주며, 이로 인해 생성된 이미지의 품질 향상에 기여할 수 있습니다. 이 구현체는 논문에서 권장하는 "균일 스케줄(uniform schedule)"을 사용합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 엡실론 스케일링 패치가 적용될 모델입니다. |
| `scaling_factor` | FLOAT | 아니요 | 0.5 - 1.5 | 예측된 노이즈를 스케일링할 인자입니다. 1.0보다 큰 값은 노이즈를 감소시키고, 1.0보다 작은 값은 노이즈를 증가시킵니다 (기본값: 1.005). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 샘플링 과정에 엡실론 스케일링 기능이 적용된 입력 모델의 패치 버전입니다. |
