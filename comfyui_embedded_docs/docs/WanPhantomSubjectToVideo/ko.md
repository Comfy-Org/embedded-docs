# WanPhantomSubjectToVideo

WanPhantomSubjectToVideo 노드는 컨디셔닝 입력과 선택적 참조 이미지를 처리하여 비디오 콘텐츠를 생성합니다. 이 노드는 비디오 생성을 위한 잠재 표현을 만들고, 입력 이미지가 제공될 경우 해당 이미지의 시각적 안내를 통합할 수 있습니다. 또한 Wan 비디오 모델에 필요한 시간 차원 연결을 포함하여 컨디셔닝 데이터를 준비하고, 수정된 컨디셔닝과 생성된 잠재 비디오 데이터를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 안내하는 긍정 컨디셔닝 입력 | CONDITIONING | 예 | - |
| `negative` | 특정 특성을 회피하기 위한 부정 컨디셔닝 입력 | CONDITIONING | 예 | - |
| `vae` | 이미지가 제공될 때 인코딩에 사용되는 VAE 모델 | VAE | 예 | - |
| `width` | 출력 비디오의 픽셀 너비 (기본값: 832, 16의 배수여야 함) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력 비디오의 픽셀 높이 (기본값: 480, 16의 배수여야 함) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 생성된 비디오의 프레임 수 (기본값: 81, 4의 배수여야 함) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 동시에 생성할 비디오 수 (기본값: 1) | INT | 예 | 1 to 4096 |
| `images` | 시간 차원 컨디셔닝을 위한 선택적 참조 이미지 | IMAGE | 아니요 | - |

**참고:** `images`가 제공되면 해당 이미지는 지정된 `width` 및 `height`에 맞게 자동으로 업스케일되며, 처음 `length`개의 프레임만 처리에 사용됩니다. 각 이미지는 VAE로 인코딩되기 전에 처음 3개의 색상 채널만 사용하도록 축소됩니다. `images`가 제공되지 않으면 컨디셔닝 입력은 변경 없이 그대로 전달됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 이미지가 제공될 때 시간 차원 연결이 적용된 수정된 긍정 컨디셔닝 | CONDITIONING |
| `negative_text` | 이미지가 제공될 때 시간 차원 연결이 적용된 수정된 부정 컨디셔닝 | CONDITIONING |
| `negative_img_text` | 이미지가 제공될 때 시간 차원 연결이 0으로 설정된 부정 컨디셔닝 | CONDITIONING |
| `latent` | 16개 채널, 시간 차원 ((length - 1) // 4) + 1, 공간 차원 height // 8 및 width // 8을 갖는 0으로 채워진 잠재 비디오 표현 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
