# DPMPP_3M_SDE 샘플러

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `eta` | 샘플링 과정의 무작위성을 제어합니다 (기본값: 1.0) | FLOAT | 예 | 0.0 - 100.0 |
| `s_noise` | 샘플링 중 추가되는 노이즈의 양을 제어합니다 (기본값: 1.0) | FLOAT | 예 | 0.0 - 100.0 |
| `noise_device` | 노이즈 계산 장치를 선택합니다. GPU 또는 CPU 중에서 선택합니다 (기본값: "gpu") | COMBO | 예 | "gpu"<br>"cpu" |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sampler` | 샘플링 워크플로우에서 사용할 구성된 샘플러 객체를 반환합니다. | SAMPLER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/ko.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
