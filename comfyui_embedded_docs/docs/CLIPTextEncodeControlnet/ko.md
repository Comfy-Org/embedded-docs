> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/ko.md)

CLIPTextEncodeControlnet 노드는 CLIP 모델을 사용하여 텍스트 입력을 처리하고 기존 조건화 데이터와 결합하여 controlnet 애플리케이션을 위한 향상된 조건화 출력을 생성합니다. 입력 텍스트를 토큰화하고 CLIP 모델을 통해 인코딩한 후, 결과 임베딩을 제공된 조건화 데이터에 cross-attention controlnet 매개변수로 추가합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | 필수 | - | - | 텍스트 토큰화 및 인코딩에 사용되는 CLIP 모델 |
| `조건` | CONDITIONING | 필수 | - | - | controlnet 매개변수로 향상시킬 기존 조건화 데이터 |
| `프롬프트 텍스트` | STRING | 멀티라인, 동적 프롬프트 | - | - | CLIP 모델에서 처리할 텍스트 입력 |

**참고:** 이 노드는 정상적으로 작동하기 위해 `clip`과 `conditioning` 입력이 모두 필요합니다. `text` 입력은 유연한 텍스트 처리를 위해 동적 프롬프트와 멀티라인 텍스트를 지원합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 추가된 controlnet cross-attention 매개변수가 포함된 향상된 조건화 데이터 |