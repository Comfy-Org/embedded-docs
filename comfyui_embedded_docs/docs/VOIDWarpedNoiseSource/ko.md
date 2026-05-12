> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/ko.md)

## 개요

이 노드는 LATENT(VOIDWarpedNoise 노드의 출력 등)를 NOISE 소스로 변환합니다. 이를 통해 왜곡된 노이즈를 SamplerCustomAdvanced 노드와 함께 사용하여 보다 제어된 이미지 생성을 수행할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `warped_noise` | LATENT | 예 | 해당 없음 | VOIDWarpedNoise에서 생성된 왜곡된 노이즈 잠재값 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `NOISE` | NOISE | SamplerCustomAdvanced와 함께 사용할 수 있는 노이즈 소스 |