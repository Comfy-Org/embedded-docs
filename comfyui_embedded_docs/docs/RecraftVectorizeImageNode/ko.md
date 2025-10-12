> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/ko.md)

입력 이미지에서 SVG를 동기적으로 생성합니다. 이 노드는 래스터 이미지를 벡터 그래픽 형식으로 변환하며, 입력 배치의 각 이미지를 처리하고 결과를 단일 SVG 출력으로 결합합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `이미지` | IMAGE | 예 | - | SVG 형식으로 변환할 입력 이미지 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 아니오 | - | API 접근을 위한 인증 토큰 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 아니오 | - | Comfy.org 서비스를 위한 API 키 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `SVG` | SVG | 처리된 모든 이미지를 결합한 생성된 벡터 그래픽 출력 |