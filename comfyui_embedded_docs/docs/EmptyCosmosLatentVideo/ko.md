# 빈 잠재 비디오 (Cosmos)

EmptyCosmosLatentVideo 노드는 지정된 차원으로 빈 잠재 비디오 텐서를 생성합니다. 이 노드는 너비, 높이, 길이 및 배치 크기 매개변수를 구성할 수 있으며, 비디오 생성 워크플로우의 시작점으로 사용할 수 있는 0으로 채워진 잠재 표현을 생성합니다. 잠재 표현의 공간 차원은 8분의 1로 다운샘플링됩니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `width` | 잠재 비디오의 픽셀 단위 너비 (기본값: 1280, 16의 배수여야 함) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 잠재 비디오의 픽셀 단위 높이 (기본값: 704, 16의 배수여야 함) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 잠재 비디오의 프레임 수 (기본값: 121, 8의 배수여야 함) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 배치로 생성할 잠재 비디오의 수 (기본값: 1) | INT | 예 | 1 to 4096 |

잠재 텐서는 16개의 채널을 사용합니다. 공간 차원은 픽셀 차원에 비해 8로 나누어지며 (height // 8, width // 8), 프레임 수는 ((length - 1) // 8) + 1개의 잠재 프레임으로 압축됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `samples` | 0으로 채워진 빈 잠재 비디오 텐서입니다. 형태: (batch_size, 16, ((length - 1) // 8) + 1, height // 8, width // 8) | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/ko.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
