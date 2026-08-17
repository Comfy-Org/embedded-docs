# 손실 그래프 그리기

LossGraphNode는 시간에 따른 학습 손실 값의 시각적 그래프를 생성하고 이를 미리 보기 이미지로 표시합니다. 학습 과정의 손실 데이터를 입력받아 학습 단계별 손실 변화를 보여주는 선 그래프를 생성합니다. 생성된 그래프에는 축 레이블과 최소/최대 손실 값이 포함됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `loss` | 학습 노드에서 제공하는 손실 맵입니다. 그래프를 그리는 데 사용되는 손실 값 목록이 포함된 `loss` 키를 포함해야 합니다. | LOSS_MAP | 예 | - |
| `filename_prefix` | 저장된 손실 그래프 이미지의 접두사입니다. (기본값: "loss_graph") | STRING | 예 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `ui.images` | 미리 보기로 표시되는 생성된 손실 그래프 이미지입니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/ko.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
