# 프레임 보간

Frame Interpolate 노드는 이미지 시퀀스의 기존 프레임 사이에 새 프레임을 생성하여 프레임 속도를 효과적으로 높입니다. AI 모델을 사용하여 중간 프레임이 어떻게 보일지 예측하며, 이를 통해 부드러운 슬로우 모션 효과를 만들거나 비디오의 부드러움을 높일 수 있습니다. 연속된 각 프레임 쌍에 대해 노드는 `multiplier - 1`개의 새 프레임을 생성하여 원본 프레임 사이에 삽입합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `interp_model` | 중간 프레임 생성에 사용할 프레임 보간 모델 (예: RIFE 또는 FILM 모델) | INTERP_MODEL | 예 | - |
| `images` | 보간할 연속 이미지(프레임) 배치. 최소 2개 이미지가 필요하며, 더 적게 제공되면 노드는 입력 이미지를 변경하지 않고 반환합니다. | IMAGE | 예 | - |
| `multiplier` | 프레임 수를 곱할 배수. 예를 들어 배수가 2이면 프레임 수가 두 배가 됩니다. (기본값: 2) | INT | 예 | 2~16 |

참고: 보간은 연속된 프레임 쌍 사이에서 이루어지므로 입력 이미지 배치에는 최소 2개의 프레임이 포함되어야 합니다. 출력의 총 프레임 수는 `(number of input frames - 1) * multiplier + 1`입니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `IMAGE` | 원본 프레임 사이에 보간된 프레임이 삽입된 새 이미지 배치로, 더 부드러운 시퀀스를 생성합니다. 출력 프레임의 총 수는 `(number of input frames - 1) * multiplier + 1`입니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/ko.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
