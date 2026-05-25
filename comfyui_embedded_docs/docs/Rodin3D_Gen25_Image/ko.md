> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/ko.md)

# 개요

이 노드는 Rodin Gen-2.5 API를 사용하여 1~5개의 참조 이미지로부터 3D 모델을 생성합니다. 생성 속도와 비용의 균형을 맞추기 위해 빠름(Fast), 보통(Regular), 초고화질(Extreme-High) 모드 중에서 선택할 수 있습니다.

# 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 예 | 1~5개 이미지 | 1~5개의 입력 이미지입니다. 여러 이미지가 제공될 경우 첫 번째 이미지가 재질에 사용됩니다. |
| `mode` | COMBO | 예 | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | 생성 품질 모드입니다. 더 높은 품질 모드는 더 나은 결과를 제공하지만 비용이 더 많이 듭니다. |
| `material` | COMBO | 예 | `"PBR"`<br>`"Matte"` | 생성된 3D 모델의 재질 유형입니다. |
| `geometry_file_format` | COMBO | 예 | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | 3D 모델 지오메트리의 출력 파일 형식입니다. |
| `texture_mode` | COMBO | 예 | `"Original"`<br>`"Clean"`<br>`"Style"` | 텍스처 생성 모드입니다. "Original"은 입력 텍스처를 유지하고, "Clean"은 제거하며, "Style"은 스타일화된 텍스처를 적용합니다. |
| `seed` | INT | 예 | 0 ~ 2147483647 | 재현 가능한 결과를 위한 무작위 시드입니다. 동일한 시드를 사용하면 동일한 출력을 얻을 수 있습니다. |
| `TAPose` | BOOLEAN | 예 | True / False | 생성된 모델에 T-포즈를 적용할지 여부입니다. |
| `hd_texture` | BOOLEAN | 예 | True / False | 고해상도 텍스처 맵을 생성할지 여부입니다. |
| `texture_delight` | BOOLEAN | 예 | True / False | 텍스처 생성 전에 입력 이미지에서 조명을 제거할지 여부입니다. |
| `use_original_alpha` | BOOLEAN | 예 | True / False | 입력 이미지의 원본 알파 채널을 사용할지 여부입니다. |
| `addon_highpack` | BOOLEAN | 예 | True / False | 표준 모델 외에 고폴리곤 버전의 모델을 추가로 생성할지 여부입니다. |
| `bbox_width` | INT | 예 | 1 ~ 1000 | 생성된 모델의 경계 상자 너비(센티미터)입니다. |
| `bbox_height` | INT | 예 | 1 ~ 1000 | 생성된 모델의 경계 상자 높이(센티미터)입니다. |
| `bbox_length` | INT | 예 | 1 ~ 1000 | 생성된 모델의 경계 상자 길이(센티미터)입니다. |
| `height_cm` | INT | 예 | 1 ~ 300 | 생성된 모델의 높이(센티미터)입니다. |

**이미지 개수 참고사항:** 이 노드는 1~5개의 이미지를 허용합니다. 이미지 배치(예: 4개 이미지 배치)를 제공하면 배치 내 각 이미지가 개별 입력 이미지로 처리됩니다. 5개를 초과하는 이미지를 제공하면 오류가 발생합니다.

# 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | FILE3D | 선택한 지오메트리 형식의 생성된 3D 모델 파일입니다. |

---
**Source fingerprint (SHA-256):** `65f755a2c3bd2317eb61c4681a406b51b06f960e36864d3602c3d03a44aa4878`
