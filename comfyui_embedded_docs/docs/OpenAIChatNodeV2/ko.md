# OpenAI ChatGPT

이 노드는 OpenAI의 GPT 모델로 텍스트 응답을 생성합니다. 텍스트 프롬프트를 전송하고, 선택적으로 이미지나 파일을 컨텍스트로 함께 전송한 뒤, 답변을 문자열로 반환합니다. 모든 설정은 `model` 선택기 안에 있습니다. 모델을 선택하면 해당 모델의 `reasoning_effort` 수준, 토큰 제한, 시드 및 시스템 프롬프트가 표시되므로 별도의 구성 노드가 필요하지 않습니다. 이 노드는 이전 OpenAI ChatGPT 노드를 대체하며, 소스 코드에서는 이제 해당 노드를 더 이상 사용되지 않는 것으로 표시합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 응답을 생성하는 데 사용할 모델입니다. 각 모델은 지원하는 `reasoning_effort` 수준을 표시합니다(기본값: `"gpt-6.2-sol"`). | DYNAMIC_COMBO | 예 | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | 모델에 전달할 텍스트 입력입니다(기본값: 빈 문자열). | STRING | 예 | - |
| `images` | 확장 가능한 슬롯: 1~16개 항목(`image_1`, `image_2`, ...)을 연결합니다. 모델의 컨텍스트로 사용할 선택적 이미지입니다. | IMAGE | 아니요 | 0~16개 이미지 |
| `files` | 모델의 컨텍스트로 사용할 선택적 파일입니다. OpenAI ChatGPT Input Files 노드의 입력을 받습니다. | OPENAI_INPUT_FILES | 아니요 | - |
| `reasoning_effort` | 모델이 답변하기 전에 얼마나 추론할지 결정합니다. 수준이 높을수록 더 많은 토큰을 사용하고 시간이 더 오래 걸립니다. 제공되는 수준은 선택한 모델에 따라 다릅니다(기본값: `"medium"`, `gpt-5.5-pro`의 경우 `"high"`). | COMBO | 예 | 아래 모델별 목록 참조 |
| `max_output_tokens` | 생성할 최대 토큰 수이며 추론 토큰을 포함합니다. 값이 낮고 `reasoning_effort`가 높으면 답변을 위한 공간이 남지 않을 수 있습니다(기본값: 32768). | INT | 예 | 16 ~ 128000 |
| `seed` | 시드는 노드를 다시 실행할지 여부를 제어합니다. 시드에 관계없이 결과는 비결정적입니다(기본값: 42). | INT | 예 | 0 ~ 2147483647 |
| `system_prompt` | 모델의 동작을 규정하는 기본 지침입니다(기본값: 빈 문자열). | STRING | 아니요 | - |

### 모델별 추론 강도 수준

- `gpt-6.2-sol`, `gpt-6.2-astra`, `gpt-6-astra`, `gpt-6.1-sol`: `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, 기본값 `"medium"`.
- `gpt-6.1-terra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, 기본값 `"medium"`.
- `gpt-5.5-pro`: `"medium"`, `"high"`, `"xhigh"`, 기본값 `"high"`.
- `gpt-5.5`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, 기본값 `"medium"`.

### 동작 관련 참고 사항

- 답변 텍스트만 반환됩니다. 모델이 사고 과정에서 논평 단계에 출력하는 메시지는 건너뜁니다.
- 답변이 작성되기 전에 토큰 예산이 소진되면, 노드는 `max_output_tokens`를 늘리라는 오류를 발생시킵니다.
- 이미지는 API의 자동 세부 수준과 함께 원래 해상도로 전송되므로, 큰 이미지는 더 많은 토큰을 사용합니다.
- 모든 요청은 OpenAI 측에 저장되며, 반환되는 텍스트는 답변 부분들을 줄바꿈으로 연결합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `output` | OpenAI 모델이 생성한 텍스트 응답입니다. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/ko.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
