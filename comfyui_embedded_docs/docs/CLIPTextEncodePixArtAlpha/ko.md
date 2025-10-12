> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/ko.md)

텍스트를 인코딩하고 PixArt Alpha의 해상도 조건을 설정합니다. 이 노드는 텍스트 입력을 처리하고 너비와 높이 정보를 추가하여 PixArt Alpha 모델에 특화된 조건 데이터를 생성합니다. PixArt Sigma 모델에는 적용되지 않습니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `width` | INT | 입력 | 1024 | 0 ~ MAX_RESOLUTION | 해상도 조건을 위한 너비 차원 |
| `height` | INT | 입력 | 1024 | 0 ~ MAX_RESOLUTION | 해상도 조건을 위한 높이 차원 |
| `text` | STRING | 입력 | - | - | 인코딩할 텍스트 입력, 다중 행 입력과 동적 프롬프트를 지원합니다 |
| `clip` | CLIP | 입력 | - | - | 토큰화와 인코딩에 사용되는 CLIP 모델 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 텍스트 토큰과 해상도 정보가 포함된 인코딩된 조건 데이터 |