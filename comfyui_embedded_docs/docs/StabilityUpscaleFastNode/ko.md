> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/ko.md)

이미지를 Stability API 호출을 통해 원본 크기의 4배로 빠르게 업스케일합니다. 이 노드는 저품질 또는 압축된 이미지를 Stability AI의 고속 업스케일링 서비스로 전송하여 업스케일링하기 위해 특별히 설계되었습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `이미지` | IMAGE | 예 | - | 업스케일할 입력 이미지 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | IMAGE | Stability AI API에서 반환된 업스케일된 이미지 |
