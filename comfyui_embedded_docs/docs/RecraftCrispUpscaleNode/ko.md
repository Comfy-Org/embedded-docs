> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/ko.md)

이미지를 동기적으로 업스케일합니다. '선명한 업스케일' 도구를 사용하여 주어진 래스터 이미지를 향상시키고, 이미지 해상도를 높이며 이미지를 더 선명하고 깨끗하게 만듭니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `이미지` | IMAGE | 예 | - | 업스케일할 입력 이미지 |
| `auth_token` | STRING | 아니오 | - | Recraft API 인증 토큰 |
| `comfy_api_key` | STRING | 아니오 | - | Comfy.org 서비스 API 키 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `이미지` | IMAGE | 향상된 해상도와 선명도를 가진 업스케일된 이미지 |
