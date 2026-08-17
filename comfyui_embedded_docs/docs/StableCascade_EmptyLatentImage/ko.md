# StableCascade 빈 잠재 이미지

StableCascade_EmptyLatentImage 노드는 Stable Cascade 모델용 빈 잠재 텐서를 생성합니다. 이 노드는 입력 해상도와 압축 설정에 따라 적절한 차원을 가진 두 개의 개별 잠재 표현(스테이지 C용 및 스테이지 B용)을 생성합니다. 이 노드는 Stable Cascade 생성 파이프라인의 시작점을 제공합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `width` | 출력 이미지의 픽셀 단위 너비입니다 (기본값: 1024, 간격: 8) | INT | 예 | 256 to MAX_RESOLUTION |
| `height` | 출력 이미지의 픽셀 단위 높이입니다 (기본값: 1024, 간격: 8) | INT | 예 | 256 to MAX_RESOLUTION |
| `compression` | 스테이지 C의 잠재 차원을 결정하는 압축 계수입니다 (기본값: 42, 간격: 1). 고급 매개변수입니다. | INT | 예 | 4 to 128 |
| `batch_size` | 배치에서 생성할 잠재 샘플 수입니다 (기본값: 1) | INT | 아니요 | 1 to 4096 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `stage_c` | 차원이 [batch_size, 16, height//compression, width//compression]인 스테이지 C 잠재 텐서입니다. | LATENT |
| `stage_b` | 차원이 [batch_size, 4, height//4, width//4]인 스테이지 B 잠재 텐서입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/ko.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
