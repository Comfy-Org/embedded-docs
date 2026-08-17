# Kandinsky5ImageToVideo

Kandinsky5ImageToVideo 노드는 Kandinsky 모델을 사용하여 비디오 생성을 위한 conditioning 및 잠재 공간 데이터를 준비합니다. 이 노드는 빈 비디오 잠재 텐서를 생성하고, 선택적으로 시작 이미지를 인코딩하여 생성된 비디오의 초기 프레임을 안내할 수 있으며, 이에 따라 긍정 및 부정 conditioning을 수정합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 안내하는 긍정 conditioning 프롬프트입니다. | CONDITIONING | 예 | 해당 없음 |
| `negative` | 비디오 생성이 특정 개념에서 멀어지도록 유도하는 부정 conditioning 프롬프트입니다. | CONDITIONING | 예 | 해당 없음 |
| `vae` | 선택적 시작 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | 해당 없음 |
| `width` | 출력 비디오의 가로 크기(픽셀 단위)입니다 (기본값: 768). | INT | 예 | 16 ~ 8192 (16 단계) |
| `height` | 출력 비디오의 세로 크기(픽셀 단위)입니다 (기본값: 512). | INT | 예 | 16 ~ 8192 (16 단계) |
| `length` | 비디오의 프레임 수입니다 (기본값: 121). | INT | 예 | 1 ~ 8192 (4 단계) |
| `batch_size` | 동시에 생성할 비디오 시퀀스 수입니다 (기본값: 1). | INT | 예 | 1 ~ 4096 |
| `start_image` | 선택적 시작 이미지입니다. 제공되면 인코딩되어 모델 출력 잠재의 노이즈 시작 부분을 대체하는 데 사용됩니다. | IMAGE | 아니요 | 해당 없음 |

**참고:** `start_image`가 제공되면 쌍선형 보간을 사용하여 지정된 `width` 및 `height`에 맞게 크기가 조정됩니다. 이미지의 첫 `length` 프레임만 인코딩에 사용됩니다. 그런 다음 인코딩된 잠재는 시작 프레임을 표시하는 마스크와 함께 `positive` 및 `negative` conditioning 모두에 주입되어, 깨끗하게 인코딩된 이미지가 생성된 비디오의 노이즈 시작 부분을 대체합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 인코딩된 시작 이미지 데이터로 업데이트되었을 수 있는 수정된 긍정 conditioning입니다. | CONDITIONING |
| `negative` | 인코딩된 시작 이미지 데이터로 업데이트되었을 수 있는 수정된 부정 conditioning입니다. | CONDITIONING |
| `latent` | 지정된 `batch_size`, `length`, `height` 및 `width`에 따라 0으로 채워진 빈 비디오 잠재 텐서입니다. | LATENT |
| `cond_latent` | 제공된 시작 이미지의 깨끗하고 인코딩된 잠재 표현입니다. 모델 출력 잠재의 노이즈 시작 부분을 대체하는 데 사용됩니다. `start_image`가 제공되지 않으면 비어 있습니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
