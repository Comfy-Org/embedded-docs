# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent 노드는 Wan 2.2 비디오 생성에 사용되는 잠재(latent) 입력을 준비합니다. 지정된 너비, 높이 및 프레임 수로 빈 비디오 잠재를 생성하며, 시작 이미지가 제공되면 해당 이미지를 잠재의 첫 번째 프레임에 인코딩합니다. 또한 이미지로 이미 채워진 프레임과 아직 생성해야 하는 프레임을 표시하는 노이즈 마스크를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `vae` | 시작 이미지를 잠재 공간에 인코딩하는 데 사용되는 VAE 모델 | VAE | 예 | - |
| `width` | 출력 비디오의 픽셀 단위 너비 (기본값: 1280, 단계: 32) | INT | 예 | 32 ~ MAX_RESOLUTION |
| `height` | 출력 비디오의 픽셀 단위 높이 (기본값: 704, 단계: 32) | INT | 예 | 32 ~ MAX_RESOLUTION |
| `length` | 비디오의 프레임 수 (기본값: 49, 단계: 4) | INT | 예 | 1 ~ MAX_RESOLUTION |
| `batch_size` | 병렬로 생성할 비디오 잠재의 수 (기본값: 1) | INT | 예 | 1 ~ 4096 |
| `start_image` | 비디오 잠재의 첫 번째 프레임에 배치되는 선택적 이미지 또는 이미지 시퀀스. 처음 `length` 프레임만 사용됩니다. 이미지는 VAE로 인코딩되기 전에 이중 선형 리샘플링 및 중앙 크롭을 사용하여 `width` x `height` 크기로 조정됩니다. | IMAGE | 아니요 | - |

**참고:** 잠재의 공간 차원은 `width / 16` 및 `height / 16`이므로 `width`와 `height`는 16으로 나누어 떨어져야 합니다. 잠재의 시간 차원은 `((length - 1) // 4) + 1`로 계산되며 48개의 채널을 가집니다. `start_image`가 제공되면 인코딩된 이미지가 잠재의 첫 번째 프레임을 채우고 `noise_mask`는 해당 프레임에 대해 0으로, 나머지 프레임에 대해 1로 설정되며, 이는 샘플러가 이미지 프레임은 변경하지 않고 나머지를 생성하도록 지시합니다. `start_image`가 제공되지 않으면 잠재는 0으로 채워지고 노이즈 마스크는 포함되지 않습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `LATENT` | 생성된 비디오 잠재로, `batch_size`만큼 반복됩니다. `start_image`가 제공되면 이미지로 인코딩된 프레임(0)과 생성할 프레임(1)을 표시하는 `noise_mask`도 포함합니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/ko.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
