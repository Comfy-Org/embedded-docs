# LMS 샘플러

SamplerLMS 노드는 확산 모델에서 사용하기 위한 최소 평균 제곱(LMS) 샘플러를 생성합니다. 이 노드는 샘플링 과정에서 사용할 수 있는 샘플러 객체를 생성하며, LMS 알고리즘의 차수를 제어하여 수치적 안정성과 정확성을 확보할 수 있게 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `order` | LMS 샘플러 알고리즘의 차수 매개변수로, 수치적 방법의 정확성과 안정성을 제어합니다 (기본값: 4; 고급 매개변수) | INT | 예 | 1~100 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sampler` | 샘플링 파이프라인에서 사용할 수 있는 구성된 LMS 샘플러 객체 | SAMPLER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/ko.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
