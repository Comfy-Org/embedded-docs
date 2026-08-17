# 곡선 편집기

Curve Editor 노드는 곡선을 조정하고 미세 조정하기 위한 시각적 인터페이스를 제공합니다. 입력 곡선의 모양을 수정하고 선택적으로 히스토그램으로 분포를 시각화할 수 있습니다. 이 노드는 수정된 곡선을 출력하여 워크플로우의 다른 부분에서 사용할 수 있게 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `curve` | 편집할 입력 곡선입니다. | CURVE | 예 | N/A |
| `histogram` | 시각적 참조를 위해 곡선과 함께 표시할 선택적 히스토그램입니다. | HISTOGRAM | 아니오 | N/A |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `curve` | 노드 인터페이스에서 조정을 수행한 후의 편집된 곡선입니다. | CURVE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/ko.md)

---
**Source fingerprint (SHA-256):** `6c4459998b1a3dd3a53f84cb1c231c448c64aa55b96444bc4ac7470556a3b915`
