> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/ko.md)

TripoRefineNode는 v1.4 Tripo 모델로 특별히 생성된 초안 3D 모델을 정제합니다. 모델 작업 ID를 받아 Tripo API를 통해 처리하여 개선된 버전의 모델을 생성합니다. 이 노드는 Tripo v1.4 모델에서 생성된 초안 모델과만 독점적으로 작동하도록 설계되었습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | 예 | - | v1.4 Tripo 모델이어야 합니다 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 아니오 | - | Comfy.org API 인증 토큰 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 아니오 | - | Comfy.org 서비스 API 키 |
| `unique_id` | UNIQUE_ID | 아니오 | - | 작업 고유 식별자 |

**참고:** 이 노드는 Tripo v1.4 모델로 생성된 초안 모델만 허용합니다. 다른 버전의 모델을 사용하면 오류가 발생할 수 있습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 정제된 모델의 파일 경로 또는 참조 |
| `model task_id` | MODEL_TASK_ID | 정제된 모델 작업의 작업 식별자 |
