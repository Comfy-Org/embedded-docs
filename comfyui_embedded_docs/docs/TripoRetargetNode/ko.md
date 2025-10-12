> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/ko.md)

TripoRetargetNode는 사전 정의된 애니메이션을 3D 캐릭터 모델에 적용하기 위해 모션 데이터를 리타겟팅합니다. 이전에 처리된 3D 모델을 입력받아 여러 프리셋 애니메이션 중 하나를 적용하여 애니메이션이 적용된 3D 모델 파일을 생성합니다. 이 노드는 Tripo API와 통신하여 애니메이션 리타겟팅 작업을 처리합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | 예 | - | 애니메이션을 적용할 이전에 처리된 3D 모델의 작업 ID |
| `animation` | STRING | 예 | "preset:idle"<br>"preset:walk"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn" | 3D 모델에 적용할 애니메이션 프리셋 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 아니오 | - | Comfy.org API 접근을 위한 인증 토큰 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 아니오 | - | Comfy.org 서비스 접근을 위한 API 키 |
| `unique_id` | UNIQUE_ID | 아니오 | - | 작업 추적을 위한 고유 식별자 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 생성된 애니메이션 3D 모델 파일 |
| `retarget task_id` | RETARGET_TASK_ID | 리타겟팅 작업 추적을 위한 작업 ID |
