> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/ko.md)

HunyuanRefinerLatent 노드는 정제 작업을 위한 조건화와 잠재 입력을 처리합니다. 잠재 이미지 데이터를 통합하면서 양수 및 음수 조건화에 노이즈 증강을 적용하고, 추가 처리를 위한 특정 차원의 새로운 잠재 출력을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 처리할 양수 조건화 입력 |
| `negative` | CONDITIONING | 예 | - | 처리할 음수 조건화 입력 |
| `latent` | LATENT | 예 | - | 잠재 표현 입력 |
| `noise_augmentation` | FLOAT | 예 | 0.0 - 1.0 | 적용할 노이즈 증강량 (기본값: 0.10) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 노이즈 증강과 잠재 이미지 연결이 적용된 처리된 양수 조건화 |
| `negative` | CONDITIONING | 노이즈 증강과 잠재 이미지 연결이 적용된 처리된 음수 조건화 |
| `latent` | LATENT | [batch_size, 32, height, width, channels] 차원을 가진 새로운 잠재 출력 |