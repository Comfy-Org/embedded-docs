# HunyuanRefinerLatent

HunyuanRefinerLatent 노드는 정제 작업을 위해 conditioning 및 latent 입력을 처리합니다. latent 이미지 데이터를 통합하면서 positive 및 negative conditioning 모두에 노이즈 증강을 적용하고, 추가 처리를 위해 특정 차원을 가진 새 latent 출력을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 처리할 positive conditioning 입력 | CONDITIONING | 예 | - |
| `negative` | 처리할 negative conditioning 입력 | CONDITIONING | 예 | - |
| `latent` | latent 표현 입력 | LATENT | 예 | - |
| `noise_augmentation` | 적용할 노이즈 증강 양 (기본값: 0.10, 단계: 0.01, 고급 매개변수) | FLOAT | 예 | 0.0 - 1.0 |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `positive` | 노이즈 증강 및 latent 이미지 연결이 적용된 처리된 positive conditioning | CONDITIONING |
| `negative` | 노이즈 증강 및 latent 이미지 연결이 적용된 처리된 negative conditioning | CONDITIONING |
| `latent` | 입력 `latent`와 동일한 배치 크기와 동일한 마지막 3개 차원 크기를 가지지만, 32개 채널을 가진 0으로 채워진 새 latent | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/ko.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
