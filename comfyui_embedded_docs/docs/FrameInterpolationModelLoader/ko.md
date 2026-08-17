# 프레임 보간 모델 불러오기

## 개요

이 노드는 파일에서 프레임 보간 모델을 로드하여 워크플로우에서 사용할 수 있도록 준비합니다. 모델 유형(FILM 또는 RIFE)을 자동으로 감지하고 하드웨어에서 최적의 성능을 위해 모델을 구성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `model_name` | 로드할 프레임 보간 모델을 선택합니다. 모델은 'frame_interpolation' 폴더에 있어야 합니다. | COMBO | 필수 | `frame_interpolation` 폴더에 있는 모델 파일 목록 |

참고: 선택한 파일이 인식 가능한 FILM 또는 RIFE 프레임 보간 모델이 아닌 경우, 노드는 오류를 발생시킵니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | 로드되어 구성된 프레임 보간 모델로, 다른 노드에서 사용할 준비가 된 상태입니다. | INTERP_MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/ko.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
