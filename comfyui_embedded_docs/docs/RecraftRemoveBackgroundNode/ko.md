> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/ko.md)

이 노드는 Recraft API 서비스를 사용하여 이미지에서 배경을 제거합니다. 입력 배치의 각 이미지를 처리하고 투명한 배경이 적용된 처리된 이미지와 제거된 배경 영역을 나타내는 알파 마스크를 함께 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `이미지` | IMAGE | 예 | - | 배경 제거를 위해 처리할 입력 이미지 |
| `auth_token` | STRING | 아니오 | - | Recraft API 접근을 위한 인증 토큰 |
| `comfy_api_key` | STRING | 아니오 | - | Comfy.org 서비스 통합을 위한 API 키 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `이미지` | IMAGE | 투명한 배경이 적용된 처리된 이미지 |
| `mask` | MASK | 제거된 배경 영역을 나타내는 알파 채널 마스크 |
