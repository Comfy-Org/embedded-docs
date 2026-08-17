# 광학 흐름 모델 불러오기

## 개요

`models/optical_flow/` 폴더에서 광학 흐름(optical flow) 모델을 불러옵니다. 현재는 torchvision의 RAFT-large 형식만 지원하며, 이는 VOIDWarpedNoise 노드에서 사용하는 모델입니다. ComfyUI는 광학 흐름 가중치를 자동으로 다운로드하지 않으므로, 체크포인트 파일을 `models/optical_flow/` 디렉터리에 직접 배치해야 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model_name` | 불러올 광학 흐름 모델입니다. 파일은 `optical_flow` 폴더에 있어야 합니다. 현재는 torchvision의 `raft_large.pth`만 지원합니다. | COMBO | 예 | `models/optical_flow/` 폴더의 파일 목록 |

선택한 파일은 torchvision RAFT-large 체크포인트여야 합니다. 노드는 파일에 예상되는 RAFT 키(`feature_encoder.*`, `context_encoder.*`, `update_block.*`)가 포함되어 있는지 확인하며, 형식이 인식되지 않으면 ValueError를 발생시킵니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `OPTICAL_FLOW` | 로드된 광학 흐름 모델로, 다른 노드에서 사용할 수 있도록 ModelPatcher로 감싼 형태입니다. | OPTICAL_FLOW |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/ko.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
