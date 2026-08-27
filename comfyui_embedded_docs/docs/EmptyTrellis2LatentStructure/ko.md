# EmptyTrellis2LatentStructure

이 노드는 Trellis2 모델을 위한 빈 latent 구조를 생성하며, 모든 값은 0으로 설정됩니다. 배치에서 지정된 항목 수에 맞는 크기로 32개 채널과 16×16×16 해상도를 가진 빈 3D latent 텐서를 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `batch_size` | 배치에서 latent 이미지의 수입니다 (기본값: 1). | INT | 예 | 1 to 4096 |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `LATENT` | 빈 Trellis2 latent 구조입니다. samples는 (batch_size, 32, 16, 16, 16) 형태의 0으로 채워진 텐서이며, latent 유형은 "trellis2"로 설정됩니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/ko.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
