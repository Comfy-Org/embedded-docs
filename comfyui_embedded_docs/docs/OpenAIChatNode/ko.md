> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/ko.md)

이 노드는 OpenAI 모델로부터 텍스트 응답을 생성합니다. 텍스트 프롬프트를 전송하고 생성된 응답을 수신하여 AI 모델과 대화를 나눌 수 있습니다. 이 노드는 이전 컨텍스트를 기억할 수 있는 다중 턴 대화를 지원하며, 모델에 대한 추가 컨텍스트로 이미지와 파일을 처리할 수도 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 모델에 대한 텍스트 입력으로, 응답을 생성하는 데 사용됩니다 (기본값: 비어 있음) |
| `persist_context` | BOOLEAN | 예 | - | 다중 턴 대화를 위해 호출 간 채팅 컨텍스트를 유지합니다 (기본값: True) |
| `model` | COMBO | 예 | 사용 가능한 여러 OpenAI 모델 | 응답 생성에 사용할 OpenAI 모델 |
| `images` | IMAGE | 아니오 | - | 모델에 대한 컨텍스트로 사용할 선택적 이미지입니다. 여러 이미지를 포함하려면 Batch Images 노드를 사용할 수 있습니다 (기본값: None) |
| `files` | OPENAI_INPUT_FILES | 아니오 | - | 모델에 대한 컨텍스트로 사용할 선택적 파일입니다. OpenAI Chat Input Files 노드의 입력을 허용합니다 (기본값: None) |
| `advanced_options` | OPENAI_CHAT_CONFIG | 아니오 | - | 모델에 대한 선택적 구성입니다. OpenAI Chat Advanced Options 노드의 입력을 허용합니다 (기본값: None) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output_text` | STRING | OpenAI 모델에 의해 생성된 텍스트 응답 |