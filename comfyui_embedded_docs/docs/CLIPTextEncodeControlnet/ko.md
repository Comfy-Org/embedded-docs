# CLIP 텍스트 인코딩 (컨트롤넷)

CLIPTextEncodeControlnet 노드는 CLIP 모델을 사용하여 텍스트 입력을 처리하고, 기존 컨디셔닝 데이터와 결합하여 컨트롤넷 애플리케이션용 향상된 컨디셔닝 출력을 생성합니다. 입력 텍스트를 토큰화하고 CLIP 모델을 통해 인코딩한 다음, 생성된 임베딩을 제공된 컨디셔닝 데이터에 크로스 어텐션 컨트롤넷 매개변수로 추가합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip` | 텍스트 토큰화 및 인코딩에 사용되는 CLIP 모델 | CLIP | 예 | - |
| `conditioning` | 컨트롤넷 매개변수로 향상시킬 기존 컨디셔닝 데이터 | CONDITIONING | 예 | - |
| `text` | CLIP 모델로 처리할 텍스트 입력. 여러 줄 텍스트 및 동적 프롬프트를 지원합니다 | STRING | 예 | - |

**참고:** 이 노드는 세 가지 입력(`clip`, `conditioning`, `text`)이 모두 있어야 정상적으로 작동합니다. `text` 입력은 동적 프롬프트와 여러 줄 텍스트를 지원하여 유연한 텍스트 처리를 가능하게 합니다. 이 노드는 실험적 단계로 표시되어 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `CONDITIONING` | CLIP 텍스트 인코딩에서 파생된 컨트롤넷 크로스 어텐션 매개변수(`cross_attn_controlnet` 및 `pooled_output_controlnet`)가 추가된 향상된 컨디셔닝 데이터 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/ko.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
