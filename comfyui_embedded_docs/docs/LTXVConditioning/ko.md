# LTXV 조건 설정

LTXVConditioning 노드는 비디오 생성 모델을 위해 긍정 및 부정 컨디셔닝 입력에 프레임 속도 정보를 추가합니다. 기존 컨디셔닝 데이터를 가져와 지정된 프레임 속도 값을 두 컨디셔닝 세트에 모두 적용하여 비디오 모델 처리에 적합하게 만듭니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 프레임 속도 정보를 수신할 긍정 컨디셔닝 입력입니다 | CONDITIONING | 예 | - |
| `negative` | 프레임 속도 정보를 수신할 부정 컨디셔닝 입력입니다 | CONDITIONING | 예 | - |
| `frame_rate` | 두 컨디셔닝 세트에 적용할 프레임 속도 값입니다 (기본값: 25.0) | FLOAT | 예 | 0.0 - 1000.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 프레임 속도 정보가 적용된 긍정 컨디셔닝입니다 | CONDITIONING |
| `negative` | 프레임 속도 정보가 적용된 부정 컨디셔닝입니다 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/ko.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
