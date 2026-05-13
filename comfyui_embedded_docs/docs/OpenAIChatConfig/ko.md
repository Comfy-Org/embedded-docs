> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/ko.md)

OpenAIChatConfig 노드는 OpenAI Chat 노드에 대한 추가 구성 옵션을 설정할 수 있도록 합니다. 이 노드는 모델이 응답을 생성하는 방식을 제어하는 고급 설정(잘라내기 동작, 출력 길이 제한 및 사용자 지정 지침 포함)을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `truncation` | COMBO | 예 | `"auto"`<br>`"disabled"` | 모델 응답에 사용할 잘라내기 전략입니다. auto: 현재 응답과 이전 응답의 컨텍스트가 모델의 컨텍스트 창 크기를 초과하면, 모델은 대화 중간의 입력 항목을 삭제하여 응답을 컨텍스트 창에 맞게 잘라냅니다. disabled: 모델 응답이 컨텍스트 창 크기를 초과하면 요청이 실패하고 400 오류가 반환됩니다(기본값: "auto") |
| `max_output_tokens` | INT | 아니요 | 16 ~ 16384 | 응답에 대해 생성될 수 있는 토큰 수의 상한선입니다. 표시되는 출력 토큰을 포함합니다(기본값: 4096) |
| `instructions` | STRING | 아니요 | - | 모델이 응답을 생성하는 방법에 대한 지침입니다(여러 줄 입력 지원). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | OpenAI Chat 노드와 함께 사용하기 위해 지정된 설정을 포함하는 구성 객체입니다. |

---
**Source fingerprint (SHA-256):** `6d956aa1bc7f822c18ddaa55cd2345dad947fd93833de25a957f49878484af97`
