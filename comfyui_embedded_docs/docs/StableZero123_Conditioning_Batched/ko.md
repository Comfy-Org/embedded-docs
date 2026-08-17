# StableZero123 조건 설정 (배치)

StableZero123_Conditioning_Batched 노드는 Stable Zero123 모델로 객체의 3D 뷰를 생성하는 데 필요한 컨디셔닝 데이터를 준비합니다. 입력 이미지를 CLIP 비전 모델과 VAE로 인코딩하고, 배치의 각 항목에 대해 이미지 특징을 카메라 고도(elevation) 및 방위각(azimuth)과 결합한 다음, 포지티브 및 네거티브 컨디셔닝과 함께 빈 잠재 변수(latent)를 출력합니다. 배치 증분 입력은 배치의 각 연속 항목에 대해 카메라 각도를 높이거나 낮춥니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 입력 이미지를 이미지 임베딩으로 인코딩하는 데 사용되는 CLIP 비전 모델 | CLIP_VISION | 예 | - |
| `init_image` | 처리 및 인코딩될 초기 입력 이미지 | IMAGE | 예 | - |
| `vae` | 이미지 픽셀을 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 | VAE | 예 | - |
| `width` | 처리된 이미지의 목표 너비 (기본값: 256) | INT | 예 | 16 ~ MAX_RESOLUTION (단계 8) |
| `height` | 처리된 이미지의 목표 높이 (기본값: 256) | INT | 예 | 16 ~ MAX_RESOLUTION (단계 8) |
| `batch_size` | 배치에서 생성할 컨디셔닝 샘플 수 (기본값: 1) | INT | 예 | 1 ~ 4096 |
| `elevation` | 시작 카메라 고도 각도(도 단위) (기본값: 0.0) | FLOAT | 예 | -180.0 ~ 180.0 (단계 0.1) |
| `azimuth` | 시작 카메라 방위각 각도(도 단위) (기본값: 0.0) | FLOAT | 예 | -180.0 ~ 180.0 (단계 0.1) |
| `elevation_batch_increment` | 배치의 각 연속 항목에 대해 고도 각도에 추가되는 값 (기본값: 0.0, 고급 매개변수) | FLOAT | 예 | -180.0 ~ 180.0 (단계 0.1) |
| `azimuth_batch_increment` | 배치의 각 연속 항목에 대해 방위각 각도에 추가되는 값 (기본값: 0.0, 고급 매개변수) | FLOAT | 예 | -180.0 ~ 180.0 (단계 0.1) |

**참고:** `width` 및 `height` 값은 8의 배수여야 합니다(선택 단계가 8이므로 자동으로 적용됨). 노드가 이 값을 8로 나누어 잠재 변수 차원을 구성하기 때문입니다. 배치의 각 항목에 대해 `elevation` 및 `azimuth` 값은 `elevation_batch_increment` 및 `azimuth_batch_increment`만큼 증가하므로, 연속된 배치 항목에는 단계적으로 증가하는 카메라 각도가 적용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 이미지 임베딩, 카메라 임베딩, 그리고 생성 중 연결(concatenation)에 사용되는 인코딩된 입력 이미지를 결합한 포지티브 컨디셔닝 | CONDITIONING |
| `negative` | 0으로 초기화된 이미지 임베딩과 연결용 zero 잠재 변수를 사용하는 네거티브 컨디셔닝 | CONDITIONING |
| `latent` | (batch_size, 4, height/8, width/8) 차원과 배치 인덱스 정보를 포함한 빈 잠재 변수 텐서 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/ko.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
