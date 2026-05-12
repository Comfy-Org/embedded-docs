> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/ko.md)

## 개요

`models/optical_flow/` 폴더에서 광학 흐름 모델을 불러옵니다. 현재는 VOIDWarpedNoise 노드에서 사용하는 torchvision의 RAFT-large 형식만 지원됩니다. ComfyUI는 광학 흐름 가중치를 자동으로 다운로드하지 않으므로, 체크포인트 파일을 `models/optical_flow/` 디렉터리에 직접 배치해야 합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | 예 | `models/optical_flow/` 폴더 내 파일 목록 | 불러올 광학 흐름 모델입니다. 파일은 `optical_flow` 폴더에 배치되어야 합니다. 현재는 torchvision의 `raft_large.pth`만 지원됩니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `OPTICAL_FLOW` | MODEL | 불러온 광학 흐름 모델로, 다른 노드에서 사용할 수 있도록 ModelPatcher로 래핑된 상태입니다. |