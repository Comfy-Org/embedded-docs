# Pixal3DConditioning

이 노드는 Trellis2 3D 생성 파이프라인을 위한 이미지 컨디셔닝을 준비합니다. 입력 이미지에서 DINOv3 비전 모델을 사용하여 두 가지 해상도로 시각적 특징을 추출하고, 이를 단계별 특징 맵으로 구성한 다음(선택적으로 NAF 모델로 강화), 수평 시야각에서 파생된 카메라 데이터와 결합합니다. 긍정 및 부정 컨디셔닝 쌍을 출력하며, 부정 컨디셔닝은 분류기 없는 유도를 위해 0으로 설정된 특징을 사용합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision 모델입니다. | CLIP_VISION | 예 | — |
| `image` | ImageCropToMask에서 전처리된 이미지입니다(Pixal3D의 경우 pad_factor=1.1). | IMAGE | 예 | — |
| `camera_angle_x` | 수평 시야각(도 단위)입니다(표시 이름: fov). 이미지별 FoV를 얻으려면 MoGeGeometryToFOV(axis='horizontal', unit='degrees')를 연결하십시오(업스트림 기본값과 일치). 기본값: 49.13. | FLOAT | 예 | 1.0 – 170.0 |

참고: `camera_angle_x` 값은 내부적으로 라디안으로 변환되며 투영 변환 행렬의 카메라 거리를 계산하는 데 사용됩니다. 제공된 비전 모델에 NAF 구성 요소가 포함된 경우, 이 노드는 모양 및 텍스처 단계를 위한 고해상도 특징 맵을 추가로 생성합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `positive` | 이미지에서 파생된 특징 맵과 Trellis2 생성을 위한 투영 데이터를 포함하는 긍정 컨디셔닝입니다. | CONDITIONING |
| `negative` | 분류기 없는 유도를 위해 0으로 설정된 특징 텐서를 포함하는 부정 컨디셔닝입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/ko.md)

---
**Source fingerprint (SHA-256):** `3eba711620f6c56a21bbf7df89f8d406ce6f90908298b1a295a1dbbddd042472`
