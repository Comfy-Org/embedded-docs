# SD_4X 확대 조건 설정

SD_4XUpscale_Conditioning 노드는 확산 모델을 사용하여 이미지 업스케일링을 위한 컨디셔닝 데이터를 준비합니다. 입력 이미지와 컨디셔닝 데이터를 받아 스케일링과 노이즈 증강을 적용하여 업스케일링 과정을 안내하는 수정된 컨디셔닝을 생성합니다. 이 노드는 업스케일링된 차원에 대한 포지티브 및 네거티브 컨디셔닝과 함께 잠재 표현을 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `images` | 업스케일링할 입력 이미지 | IMAGE | 예 | - |
| `positive` | 원하는 콘텐츠로 생성 과정을 안내하는 포지티브 컨디셔닝 데이터 | CONDITIONING | 예 | - |
| `negative` | 원치 않는 콘텐츠에서 생성 과정을 멀어지게 하는 네거티브 컨디셔닝 데이터 | CONDITIONING | 예 | - |
| `scale_ratio` | 입력 이미지에 적용되는 스케일링 비율 (기본값: 4.0) | FLOAT | 예 | 0.0 - 10.0 |
| `noise_augmentation` | 업스케일링 과정에서 추가할 노이즈의 양 (기본값: 0.0) | FLOAT | 예 | 0.0 - 1.0 |

대상 업스케일링 차원은 입력 이미지의 차원에 `scale_ratio`를 곱하여 계산됩니다. 컨디셔닝에 포함된 이미지와 출력 잠재 표현은 모두 해당 대상 차원의 1/4 크기로 생성됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 업스케일링 정보가 적용된 수정된 포지티브 컨디셔닝 | CONDITIONING |
| `negative` | 업스케일링 정보가 적용된 수정된 네거티브 컨디셔닝 | CONDITIONING |
| `latent` | 업스케일링된 차원에 해당하는 빈 잠재 표현 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/ko.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
