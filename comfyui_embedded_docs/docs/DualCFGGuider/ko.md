# 이중 CFG 가이드

DualCFGGuider 노드는 이중 classifier-free guidance 샘플링을 위한 가이던스 시스템을 생성합니다. 두 개의 긍정 조건화 입력과 하나의 부정 조건화 입력을 결합하고, 각 조건화 쌍에 서로 다른 가이던스 스케일을 적용하여 각 프롬프트가 생성된 출력에 미치는 영향을 제어합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 가이던스에 사용할 모델입니다. | MODEL | 예 | - |
| `cond1` | 첫 번째 긍정 조건화 입력입니다. | CONDITIONING | 예 | - |
| `cond2` | 중간 조건화로 처리되는 두 번째 긍정 조건화 입력입니다. | CONDITIONING | 예 | - |
| `negative` | 부정 조건화 입력입니다. | CONDITIONING | 예 | - |
| `cfg_conds` | `cond1`과 `cond2` 사이에 적용되는 가이던스 스케일입니다 (기본값: 8.0). | FLOAT | 예 | 0.0 - 100.0 |
| `cfg_cond2_negative` | `cond2`와 부정 조건화 사이에 적용되는 가이던스 스케일입니다 (기본값: 8.0). | FLOAT | 예 | 0.0 - 100.0 |
| `style` | 적용할 가이던스 스타일입니다 (기본값: "regular"). "regular"는 두 가이던스 스케일을 한 단계에서 결합하고, "nested"는 먼저 `cfg_conds`를 적용한 다음 결과를 부정 조건화에 대해 `cfg_cond2_negative`로 스케일링합니다. | COMBO | 예 | "regular"<br>"nested" |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `GUIDER` | 샘플링에 사용할 준비가 된 구성된 가이던스 시스템입니다. | GUIDER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/ko.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
