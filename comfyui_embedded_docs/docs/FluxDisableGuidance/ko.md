# 가이드 비활성화 (FLUX)

이 노드는 Flux 및 Flux 계열 모델에 대한 guidance embed 기능을 완전히 비활성화합니다. 입력으로 conditioning 데이터를 받아 guidance 구성 요소를 `None`으로 설정하여 제거하고, 수정된 conditioning 데이터를 반환함으로써 생성 과정에서 guidance 기반 조건화를 효과적으로 끕니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `conditioning` | guidance를 제거하기 위해 처리할 conditioning 데이터 | CONDITIONING | 예 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `conditioning` | guidance가 비활성화된 수정된 conditioning 데이터 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/ko.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
