# 비디오 삼각형 CFG 가이드

VideoTriangleCFGGuidance 노드는 비디오 모델에 삼각형 classifier-free guidance(CFG) 스케일링 패턴을 적용합니다. 최소 CFG 값과 원래 컨디셔닝 스케일 사이를 진동하는 삼각파 함수를 사용하여 시간에 따라 컨디셔닝 스케일을 수정합니다. 이는 동적 가이던스 패턴을 생성하여 비디오 생성의 일관성과 품질을 향상시키는 데 도움이 될 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 삼각형 CFG 가이던스를 적용할 비디오 모델 | MODEL | 예 | - |
| `min_cfg` | 삼각형 패턴의 최소 CFG 스케일 값 (기본값: 1.0) | FLOAT | 예 | 0.0 - 100.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 삼각형 CFG 가이던스가 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/ko.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
