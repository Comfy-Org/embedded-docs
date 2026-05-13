> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/ko.md)

다음은 제공된 영어 문서를 번역 규칙에 따라 한국어로 번역한 결과입니다.

> 본 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/en.md)

텍스트 프롬프트와 원본 이미지의 종횡비를 기반으로 이미지를 동기식으로 수정합니다. 이 노드는 입력 이미지를 받아 제공된 프롬프트에 따라 변환하며, 구성 가능한 이미지 가중치를 사용하여 원본 이미지가 변경되는 정도를 제어합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 수정할 입력 이미지 |
| `prompt` | STRING | 예 | - | 이미지 생성을 위한 프롬프트 (기본값: "") |
| `image_weight` | FLOAT | 아니요 | 0.0-0.98 | 이미지 가중치입니다. 1.0에 가까울수록 이미지가 덜 수정됩니다 (기본값: 0.1). 내부적으로 이 값은 반전(1.0 - image_weight)되어 0.0에서 0.98 사이로 제한됩니다. |
| `model` | STRING | 예 | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` | 이미지 수정에 사용할 Luma 모델입니다. 모델에 따라 비용이 다릅니다. |
| `seed` | INT | 아니요 | 0-18446744073709551615 | 노드 재실행 여부를 결정하는 시드입니다. 시드와 관계없이 실제 결과는 비결정적입니다 (기본값: 0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | Luma 모델에 의해 생성된 수정된 이미지 |

---
**Source fingerprint (SHA-256):** `078542bdba19945037c95fefa30d1b403ebf58e29270c8067dcb8ff21a99b7e0`
