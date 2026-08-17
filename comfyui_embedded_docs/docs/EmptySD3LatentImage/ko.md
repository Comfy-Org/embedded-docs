# 빈 잠재 이미지 (SD3)

EmptySD3LatentImage 노드는 Stable Diffusion 3 모델용으로 특별히 포맷된 빈 잠재 이미지 텐서를 생성합니다. 이 노드는 SD3 파이프라인에서 기대하는 올바른 차원과 구조를 가진 0으로 채워진 텐서를 생성합니다. 일반적으로 이미지 생성 워크플로우의 시작점으로 사용됩니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `width` | 출력 잠재 이미지의 가로 크기(픽셀)입니다 (기본값: 1024) | INT | 예 | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 출력 잠재 이미지의 세로 크기(픽셀)입니다 (기본값: 1024) | INT | 예 | 16 to MAX_RESOLUTION (step: 16) |
| `batch_size` | 배치에서 생성할 잠재 이미지의 수입니다 (기본값: 1) | INT | 예 | 1 to 4096 |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `LATENT` | SD3 호환 차원을 가진 빈 샘플을 포함하는 잠재 텐서입니다. 텐서는 16개 채널을 가지며, 입력 너비와 높이에 비해 공간적으로 8배 축소됩니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/ko.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
