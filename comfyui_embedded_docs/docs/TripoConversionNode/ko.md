> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/ko.md)

# Tripo 변환 노드

TripoConversionNode는 Tripo API를 사용하여 3D 모델을 다양한 파일 형식 간에 변환합니다. 이 노드는 이전 Tripo 작업(모델 생성, 리깅 또는 리타겟팅)의 작업 ID를 받아 결과 모델을 다양한 내보내기 옵션과 함께 원하는 형식으로 변환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | 예 | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | 이전 Tripo 작업(모델 생성, 리깅 또는 리타겟팅)의 작업 ID |
| `format` | COMBO | 예 | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | 변환된 3D 모델의 대상 파일 형식 |
| `quad` | BOOLEAN | 아니요 | True/False | 삼각형을 사각형으로 변환할지 여부 (기본값: False) |
| `face_limit` | INT | 아니요 | -1 ~ 2000000 | 출력 모델의 최대 면 수, 제한 없음은 -1 사용 (기본값: -1) |
| `texture_size` | INT | 아니요 | 128 ~ 4096 | 출력 텍스처의 픽셀 크기 (기본값: 4096) |
| `texture_format` | COMBO | 아니요 | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | 내보내는 텍스처의 형식 (기본값: JPEG) |
| `force_symmetry` | BOOLEAN | 아니요 | True/False | 모델에 대칭을 강제 적용할지 여부 (기본값: False) |
| `flatten_bottom` | BOOLEAN | 아니요 | True/False | 모델의 바닥을 평평하게 할지 여부 (기본값: False) |
| `flatten_bottom_threshold` | FLOAT | 아니요 | 0.0 ~ 1.0 | 바닥 평탄화 임계값 (기본값: 0.0) |
| `pivot_to_center_bottom` | BOOLEAN | 아니요 | True/False | 피벗 지점을 모델의 중앙 하단으로 이동할지 여부 (기본값: False) |
| `scale_factor` | FLOAT | 아니요 | 0.0 이상 | 모델에 적용할 배율 (기본값: 1.0) |
| `with_animation` | BOOLEAN | 아니요 | True/False | 내보내기에 애니메이션 데이터를 포함할지 여부 (기본값: False) |
| `pack_uv` | BOOLEAN | 아니요 | True/False | UV 좌표를 패킹할지 여부 (기본값: False) |
| `bake` | BOOLEAN | 아니요 | True/False | 텍스처를 베이크할지 여부 (기본값: False) |
| `part_names` | STRING | 아니요 | 쉼표로 구분된 목록 | 내보내기에 포함할 부품 이름의 쉼표로 구분된 목록 (기본값: "") |
| `fbx_preset` | COMBO | 아니요 | blender<br>mixamo<br>3dsmax | 사용할 FBX 내보내기 프리셋 (기본값: blender) |
| `export_vertex_colors` | BOOLEAN | 아니요 | True/False | 정점 색상을 내보낼지 여부 (기본값: False) |
| `export_orientation` | COMBO | 아니요 | align_image<br>default | 내보내기 방향 모드 (기본값: default) |
| `animate_in_place` | BOOLEAN | 아니요 | True/False | 모델을 제자리에서 애니메이션할지 여부 (기본값: False) |

**참고:** `original_model_task_id`는 이전 Tripo 작업(모델 생성, 리깅 또는 리타겟팅)의 유효한 작업 ID여야 합니다. "고급"으로 표시된 매개변수는 선택 사항이며 특정 내보내기 요구 사항이 있을 때만 구성하면 됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| *명명된 출력 없음* | - | 이 노드는 변환을 비동기적으로 처리하며 Tripo API 시스템을 통해 결과를 반환합니다 |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
