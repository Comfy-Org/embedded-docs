> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/ko.md)

HunyuanVideo15SuperResolution 노드는 비디오 초해상도 처리를 위한 조건화 데이터를 준비합니다. 비디오의 잠재 표현과 선택적으로 시작 이미지를 입력받아, 노이즈 증강 및 CLIP 비전 데이터와 함께 패키징하여 모델이 더 높은 해상도의 출력을 생성하는 데 사용할 수 있는 형식으로 변환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | 해당 없음 | 잠재 데이터와 증강 데이터로 수정될 긍정적 조건화 입력입니다. |
| `negative` | CONDITIONING | 예 | 해당 없음 | 잠재 데이터와 증강 데이터로 수정될 부정적 조건화 입력입니다. |
| `vae` | VAE | 아니요 | 해당 없음 | 선택적 `start_image`를 인코딩하는 데 사용되는 VAE입니다. `start_image`가 제공된 경우 필수입니다. |
| `start_image` | IMAGE | 아니요 | 해당 없음 | 초해상도 과정을 안내하기 위한 선택적 시작 이미지입니다. 제공된 경우 업스케일되어 조건화 잠재 표현으로 인코딩됩니다. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 아니요 | 해당 없음 | 조건화에 추가할 선택적 CLIP 비전 임베딩입니다. |
| `latent` | LATENT | 예 | 해당 없음 | 조건화에 통합될 입력 비디오 잠재 표현입니다. |
| `noise_augmentation` | FLOAT | 아니요 | 0.0 - 1.0 | 조건화에 적용할 노이즈 증강의 강도입니다 (기본값: 0.70). |

**참고:** `start_image`를 제공하는 경우, 인코딩을 위해 반드시 `vae`도 연결해야 합니다. `start_image`는 입력 `latent`가 의미하는 차원과 일치하도록 자동으로 업스케일됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 연결된 잠재 데이터, 노이즈 증강 및 선택적 CLIP 비전 데이터를 포함하도록 수정된 긍정적 조건화입니다. |
| `negative` | CONDITIONING | 연결된 잠재 데이터, 노이즈 증강 및 선택적 CLIP 비전 데이터를 포함하도록 수정된 부정적 조건화입니다. |
| `latent` | LATENT | 입력된 잠재 표현이 변경 없이 통과됩니다. |
