# CosmosPredict2ImageToVideoLatent

`CosmosPredict2ImageToVideoLatent` 노드는 이미지로부터 비디오 생성을 위한 비디오 잠재 표현을 생성합니다. 빈 비디오 잠재 표현을 생성하거나 시작 및 종료 이미지를 통합하여 지정된 크기와 길이를 가진 비디오 시퀀스를 생성할 수 있습니다. 이 노드는 비디오 처리를 위해 이미지를 적절한 잠재 공간 형식으로 인코딩하는 작업을 처리합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `vae` | 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `width` | 출력 비디오의 가로 크기(픽셀 단위, 기본값: 848, 16으로 나누어져야 함)입니다. | INT | 예 | 16 ~ MAX_RESOLUTION (16 단계) |
| `height` | 출력 비디오의 세로 크기(픽셀 단위, 기본값: 480, 16으로 나누어져야 함)입니다. | INT | 예 | 16 ~ MAX_RESOLUTION (16 단계) |
| `length` | 비디오 시퀀스의 프레임 수입니다 (기본값: 93) | INT | 예 | 1 ~ MAX_RESOLUTION (4 단계) |
| `batch_size` | 생성할 비디오 시퀀스의 수입니다 (기본값: 1) | INT | 예 | 1 ~ 4096 |
| `start_image` | 비디오 시퀀스의 선택적 시작 이미지입니다. | IMAGE | 아니요 | - |
| `end_image` | 비디오 시퀀스의 선택적 종료 이미지입니다. | IMAGE | 아니요 | - |

**참고:** `start_image`와 `end_image`가 모두 제공되지 않으면 노드는 빈 비디오 잠재 표현을 생성합니다. 이미지가 제공되면 해당 이미지가 인코딩되어 적절한 마스킹과 함께 비디오 시퀀스의 시작 및/또는 끝에 배치됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `samples` | 인코딩된 비디오 시퀀스를 포함하는 생성된 비디오 잠재 표현입니다. | LATENT |
| `noise_mask` | 생성 중 잠재 공간의 어떤 부분을 보존해야 하는지 나타내는 마스크입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/ko.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
