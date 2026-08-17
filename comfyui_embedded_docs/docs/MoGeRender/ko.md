# MoGe 렌더

## 개요

이 노드는 MoGe 깊이/법선 추정 노드에서 생성된 `MOGE_GEOMETRY` 패킷을 받아 표준 이미지 형식으로 렌더링합니다. 깊이 맵, 컬러 깊이 맵, 법선 맵 또는 마스크를 출력하도록 선택할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | MoGe 추정 노드에서 생성된 지오메트리 데이터 패킷입니다. | MOGE_GEOMETRY | 예 | 해당 없음 |
| `output` | 지오메트리 데이터에서 렌더링할 이미지 유형입니다. DirectX와 OpenGL은 법선 맵의 녹색 채널 규칙을 제어합니다. DirectX: 녹색 = -Y 아래쪽(Unreal). OpenGL: 녹색 = +Y 위쪽(Blender, Substance, Unity, glTF). (기본값: `"depth"`) | COMBO | 예 | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**참고:** 선택한 `output` 모드에 따라 `moge_geometry`에 포함되어야 하는 데이터가 결정됩니다.
- `depth` 및 `depth_colored`는 깊이 데이터가 필요합니다. 깊이는 0.1/99.9 백분위수 클리핑을 사용하여 정규화된 시차(1/깊이) 맵으로 변환됩니다.
- `normal_opengl` 및 `normal_directx`는 법선 데이터 또는 법선을 파생할 수 있는 점 데이터가 필요합니다. 둘 다 없으면 노드는 오류를 발생시킵니다.
- `mask`는 마스크 데이터가 필요합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `IMAGE` | `output` 모드에 따라 렌더링된 이미지로, RGB 텐서 배치입니다. 내용은 그레이스케일 깊이 맵, 컬러 깊이 맵, 법선 맵 또는 마스크 중 하나입니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/ko.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
