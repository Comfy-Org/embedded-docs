> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/ko.md)

TripoConversionNode는 Tripo API를 사용하여 3D 모델을 다양한 파일 형식 간에 변환합니다. 이전 Tripo 작업에서 얻은 작업 ID를 사용하여 결과 모델을 원하는 형식으로 다양한 내보내기 옵션과 함께 변환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | 예 | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | 이전 Tripo 작업(모델 생성, 리깅 또는 리타겟팅)에서 얻은 작업 ID |
| `format` | COMBO | 예 | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | 변환할 3D 모델의 대상 파일 형식 |
| `quad` | BOOLEAN | 아니오 | True/False | 삼각형을 사각형으로 변환할지 여부 (기본값: False) |
| `face_limit` | INT | 아니오 | -1 ~ 500000 | 출력 모델의 최대 면 수, 제한 없음을 원할 경우 -1 사용 (기본값: -1) |
| `texture_size` | INT | 아니오 | 128 ~ 4096 | 출력 텍스처의 크기(픽셀 단위) (기본값: 4096) |
| `texture_format` | COMBO | 아니오 | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | 내보낼 텍스처의 형식 (기본값: JPEG) |

**참고:** `original_model_task_id`는 이전 Tripo 작업(모델 생성, 리깅 또는 리타겟팅)의 유효한 작업 ID여야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| *명명된 출력 없음* | - | 이 노드는 변환을 비동기적으로 처리하며 결과는 Tripo API 시스템을 통해 반환됩니다 |
