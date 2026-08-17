# Cosmos 비디오 생성 (이미지 → 비디오)

CosmosImageToVideoLatent 노드는 이미지-투-비디오 생성을 위한 비디오 잠재 표현을 생성합니다. 빈 잠재 표현으로 시작하며, 선택적으로 시작 이미지 및/또는 종료 이미지를 비디오 시퀀스의 첫 번째 또는 마지막 프레임에 인코딩할 수 있습니다. 이미지가 제공되면 인코딩된 프레임을 생성 중에 고정으로 표시하는 노이즈 마스크도 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `vae` | 입력 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `width` | 출력 비디오의 픽셀 단위 너비입니다. (기본값: 1280) | INT | 예 | 16 to MAX_RESOLUTION (step 16) |
| `height` | 출력 비디오의 픽셀 단위 높이입니다. (기본값: 704) | INT | 예 | 16 to MAX_RESOLUTION (step 16) |
| `length` | 비디오 시퀀스의 프레임 수입니다. (기본값: 121) | INT | 예 | 1 to MAX_RESOLUTION (step 8) |
| `batch_size` | 출력 배치로 생성할 비디오 잠재 표현의 수입니다. (기본값: 1) | INT | 예 | 1 to 4096 |
| `start_image` | 비디오 시퀀스의 시작 부분에 인코딩할 선택적 이미지 또는 이미지 시퀀스입니다. | IMAGE | 아니오 | - |
| `end_image` | 비디오 시퀀스의 끝 부분에 인코딩할 선택적 이미지 또는 이미지 시퀀스입니다. | IMAGE | 아니오 | - |

**참고:** `start_image` 또는 `end_image`가 모두 제공되지 않으면 노드는 노이즈 마스크 없이 빈 잠재 표현을 반환합니다. 이미지가 하나 이상 제공되면 `noise_mask`가 포함됩니다. 제공된 이미지에서 인코딩된 잠재 프레임은 마스크 값 0(고정 유지)을 가지며, 나머지 프레임은 마스크 값 1(생성 대상)을 갖습니다. 이미지는 인코딩 전에 대상 `width` 및 `height`로 크기가 조정되며, 입력 이미지에서 가져오는 프레임 수는 해당 배치 차원과 같으며 최대 `length`입니다. 잠재 표현은 16개 채널, 공간 차원 `width / 8` 및 `height / 8`, 그리고 `((length - 1) // 8) + 1`개의 프레임을 갖습니다. 이미지가 제공되면 잠재 표현과 해당 노이즈 마스크는 출력 배치를 형성하기 위해 `batch_size` 번 반복됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `latent` | 비디오 잠재 표현 `samples`와 `start_image` 또는 `end_image`가 제공될 때 인코딩된 프레임을 고정으로 표시하는 `noise_mask`를 포함하는 LATENT입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/ko.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
