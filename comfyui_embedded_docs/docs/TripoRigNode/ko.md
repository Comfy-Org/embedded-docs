> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/ko.md)

TripoRigNode는 원본 모델 작업 ID에서 리깅된 3D 모델을 생성합니다. Tripo API에 요청을 보내 Tripo 사양을 사용하여 GLB 형식의 애니메이션 리그를 생성한 후, 리그 생성 작업이 완료될 때까지 API를 폴링합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | 예 | - | 리깅할 원본 3D 모델의 작업 ID |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 아니오 | - | Comfy.org API 접근을 위한 인증 토큰 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 아니오 | - | Comfy.org 서비스 인증을 위한 API 키 |
| `unique_id` | UNIQUE_ID | 아니오 | - | 작업 추적을 위한 고유 식별자 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 생성된 리깅된 3D 모델 파일 |
| `rig task_id` | RIG_TASK_ID | 리그 생성 과정 추적을 위한 작업 ID |