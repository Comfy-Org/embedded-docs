> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/ko.md)

VOIDInpaintConditioning 노드는 CogVideoX 모델을 사용한 인페인팅에 필요한 컨디셔닝 데이터를 준비합니다. 소스 비디오와 전처리된 쿼드마스크를 입력받아 VAE로 인코딩한 후, 모델이 마스킹된 영역을 채우는 데 사용하는 32채널 컨디셔닝 신호로 결합합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 인페인팅 잠재 정보로 보강할 포지티브 컨디셔닝 |
| `negative` | CONDITIONING | 예 | - | 인페인팅 잠재 정보로 보강할 네거티브 컨디셔닝 |
| `vae` | VAE | 예 | - | 마스크와 마스킹된 비디오를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 |
| `video` | IMAGE | 예 | - | [T, H, W, 3] 형식의 소스 비디오 프레임 |
| `quadmask` | MASK | 예 | - | VOIDQuadmaskPreprocess에서 전처리된 [T, H, W] 형식의 쿼드마스크 |
| `width` | INT | 예 | 16 ~ MAX_RESOLUTION (단위: 8) | 비디오와 마스크를 리사이즈할 너비 (기본값: 672) |
| `height` | INT | 예 | 16 ~ MAX_RESOLUTION (단위: 8) | 비디오와 마스크를 리사이즈할 높이 (기본값: 384) |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION (단위: 1) | 처리할 픽셀 프레임 수. CogVideoX-Fun-V1.5(patch_size_t=2)의 경우 latent_t가 짝수여야 하므로, 홀수 latent_t를 생성하는 길이는 내림 처리됩니다(예: 49 → 45) (기본값: 45) |
| `batch_size` | INT | 예 | 1 ~ 64 | 출력 노이즈 잠재의 배치 크기 (기본값: 1) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 인페인팅 잠재 정보가 추가된 포지티브 컨디셔닝 |
| `negative` | CONDITIONING | 인페인팅 잠재 정보가 추가된 네거티브 컨디셔닝 |
| `latent` | LATENT | [batch_size, 16, latent_t, latent_h, latent_w] 형태의 0으로 채워진 노이즈 잠재 텐서 |