> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/ko.md)

ElevenLabs Voice Selector 노드를 사용하면 ElevenLabs 텍스트 음성 변환 사전 정의 음성 목록에서 특정 음성을 선택할 수 있습니다. 음성 이름을 입력으로 받아 음성 생성에 필요한 해당 음식 식별자를 출력합니다. 이 노드는 다른 ElevenLabs 오디오 노드와 함께 사용할 호환 음성을 선택하는 과정을 단순화합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `voice` | STRING | 예 | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | 사전 정의된 ElevenLabs 음성 목록에서 음성을 선택합니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `voice` | STRING | 선택한 ElevenLabs 음성의 고유 식별자로, 텍스트 음성 변환 생성을 위해 다른 노드로 전달할 수 있습니다. |