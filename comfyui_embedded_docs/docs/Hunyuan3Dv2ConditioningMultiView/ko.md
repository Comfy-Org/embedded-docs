# Hunyuan3Dv2ConditioningMultiView

Hunyuan3Dv2ConditioningMultiView 노드는 3D 비디오 생성을 위해 다중 뷰 CLIP 비전 임베딩을 처리합니다. 선택적으로 전면, 좌측, 후면 및 우측 뷰 임베딩을 입력받아 각 제공된 뷰에 위치 인코딩을 추가한 후 단일 컨디셔닝 시퀀스로 결합합니다. 이 노드는 결합된 임베딩에서 생성된 포지티브 컨디셔닝과 0 값으로 구성된 네거티브 컨디셔닝을 모두 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `front` | 전면 뷰에 대한 CLIP 비전 출력 | CLIP_VISION_OUTPUT | 아니오 | - |
| `left` | 좌측 뷰에 대한 CLIP 비전 출력 | CLIP_VISION_OUTPUT | 아니오 | - |
| `back` | 후면 뷰에 대한 CLIP 비전 출력 | CLIP_VISION_OUTPUT | 아니오 | - |
| `right` | 우측 뷰에 대한 CLIP 비전 출력 | CLIP_VISION_OUTPUT | 아니오 | - |

**참고:** 노드가 작동하려면 하나 이상의 뷰 입력이 제공되어야 합니다. 노드는 유효한 CLIP 비전 출력 데이터가 포함된 뷰만 처리합니다. 각 제공된 뷰는 해당 뷰 위치(전면, 좌측, 후면, 우측)에 따라 위치 인코딩을 받으며, 인코딩된 뷰는 동일한 순서로 연결됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 위치 인코딩이 포함된 결합된 다중 뷰 임베딩을 포함하는 포지티브 컨디셔닝 | CONDITIONING |
| `negative` | 포지티브 컨디셔닝과 동일한 형태의 0 값을 포함하는 네거티브 컨디셔닝 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/ko.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
