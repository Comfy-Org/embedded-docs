# Empty Flux 2 Latent

EmptyFlux2LatentImage 노드는 비어 있는 빈 잠재 표현을 생성합니다. 이 노드는 0으로 채워진 텐서를 생성하며, 이는 Flux 모델의 노이즈 제거(denoising) 프로세스의 시작점으로 사용됩니다. 잠재 표현의 차원은 입력 `width`와 `height`에 의해 결정되며, 16배 축소됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `width` | 생성할 최종 이미지의 너비입니다. 잠재 너비는 이 값을 16으로 나눈 값입니다. 기본값은 1024입니다. | INT | 예 | 16 to 16384 |
| `height` | 생성할 최종 이미지의 높이입니다. 잠재 높이는 이 값을 16으로 나눈 값입니다. 기본값은 1024입니다. | INT | 예 | 16 to 16384 |
| `batch_size` | 단일 배치에서 생성할 잠재 샘플의 수입니다. 기본값은 1입니다. | INT | 아니요 | 1 to 4096 |

**참고:** `width` 및 `height` 입력은 16으로 나누어 떨어져야 합니다. 노드가 내부적으로 이 값을 16으로 나누어 잠재 차원을 생성하기 때문입니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `samples` | 0으로 채워진 잠재 텐서입니다. 형태는 `[batch_size, 128, height // 16, width // 16]`입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/ko.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
