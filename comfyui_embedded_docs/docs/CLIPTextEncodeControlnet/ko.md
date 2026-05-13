> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/ko.md)

CLIPTextEncodeControlnet 노드는 CLIP 모델을 사용하여 텍스트 입력을 처리하고, 이를 기존 컨디셔닝 데이터와 결합하여 컨트롤넷 애플리케이션을 위한 향상된 컨디셔닝 출력을 생성합니다. 입력 텍스트를 토큰화하고 CLIP 모델을 통해 인코딩한 후, 결과 임베딩을 제공된 컨디셔닝 데이터에 크로스 어텐션 컨트롤넷 매개변수로 추가합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 예 | - | 텍스트 토큰화 및 인코딩에 사용되는 CLIP 모델 |
| `조건` | CONDITIONING | 예 | - | 컨트롤넷 매개변수로 보강할 기존 컨디셔닝 데이터 |
| `프롬프트 텍스트` | STRING | 예 | - | CLIP 모델로 처리할 텍스트 입력. 여러 줄 텍스트 및 동적 프롬프트 지원 |

**참고:** 이 노드는 세 가지 입력(`clip`, `conditioning`, `text`)이 모두 있어야 올바르게 작동합니다. `text` 입력은 유연한 텍스트 처리를 위해 동적 프롬프트와 여러 줄 텍스트를 지원합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | CLIP 텍스트 인코딩에서 파생된 컨트롤넷 크로스 어텐션 매개변수(`cross_attn_controlnet` 및 `pooled_output_controlnet`)가 추가된 향상된 컨디셔닝 데이터 |

---
**Source fingerprint (SHA-256):** `dd6f68d822cc38e27c826b634c938d62e07b075e18a0f46f80b462aecca0b70b`
