> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/ko.md)

# 개요

이 노드는 Tripo P1 API를 사용하여 단일 2D 이미지를 3D 모델로 변환합니다. 저폴리곤, 게임에 바로 사용할 수 있는 메시를 생성하도록 최적화되어 있습니다.

# 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 3D 모델로 변환할 입력 이미지입니다. |
| `output_mode` | DICT | 예 | 설명 참조 | 출력 모드와 품질 설정을 지정하는 딕셔너리입니다. 이 매개변수는 생성되는 모델의 유형과 텍스처 품질을 제어합니다. 사용 가능한 옵션은 `_build_p1_output_mode` 헬퍼 함수에 의해 정의되며, `texture_quality`(예: "standard", "high", "ultra") 및 `image_alignment` 설정을 포함합니다. |
| `enable_image_autofix` | BOOLEAN | 아니요 | True<br>False | 더 나은 생성 품질을 위해 입력 이미지를 전처리합니다. (기본값: False) |
| `face_limit` | INT | 아니요 | - | 생성된 메시의 면 수를 제한합니다. 값이 -1이면 제한이 없음을 의미합니다. (기본값: -1) |
| `model_seed` | INT | 아니요 | - | 재현 가능한 모델 생성을 위한 시드 값입니다. 제공되지 않으면 무작위 시드가 사용됩니다. (기본값: None) |
| `auto_size` | BOOLEAN | 아니요 | True<br>False | 생성된 모델의 최적 크기를 자동으로 결정합니다. (기본값: False) |
| `export_uv` | BOOLEAN | 아니요 | True<br>False | 모델과 함께 UV 좌표를 내보냅니다. (기본값: True) |
| `compress_geometry` | BOOLEAN | 아니요 | True<br>False | 파일 크기를 줄이기 위해 지오메트리 데이터를 압축합니다. (기본값: False) |

# 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 생성된 3D 모델의 파일 경로입니다. 이 출력은 이전 버전과의 호환성을 위해서만 제공됩니다. |
| `model task_id` | MODEL_TASK_ID | 모델 생성 요청에 대한 고유 작업 ID입니다. |
| `GLB` | FILE3DGLB | GLB 형식으로 생성된 3D 모델입니다. |

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
