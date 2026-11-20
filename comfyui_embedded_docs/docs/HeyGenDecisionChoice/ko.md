# HeyGen Decision (Choice)

연결한 텍스트, 이미지, 오디오 또는 비디오에 대해 직접 지정한 옵션 중 하나를 선택하고, 선택된 옵션과 그 위치, 신뢰도를 돌려받습니다. `choice`를 동일한 옵션 이름을 입력으로 받는 Branch 노드에 연결하거나, `option_index`를 기준으로 분기하세요.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 사용할 모델입니다. `heygen-decision-1-turbo`는 `heygen-decision-1`보다 빠르고 비용이 적게 듭니다 (기본값: `"heygen-decision-1"`). | COMBO | 예 | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | 옵션이 답해야 할 질문으로, 최대 5000자입니다 (기본값: "What style is the image?"). | STRING | 예 | 1~5000자 |
| `options` | 한 줄에 옵션 하나씩 입력하며, 입력한 그대로 사용되고 각 옵션은 최대 128자입니다. 어느 옵션에도 해당하지 않는 입력을 위해 `other`와 같은 옵션을 추가하세요 (기본값: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | 예 | 2~255개 옵션 |
| `images` | 분류할 이미지로, 배치의 모든 프레임을 포함해 총 최대 4개입니다. 소켓 순서대로 `image_1`부터 `image_4`까지 번호가 매겨집니다. | IMAGE | 아니요 | 최대 4개 이미지 |
| `audio_1` | 분류할 오디오로, 최대 30분입니다. | AUDIO | 아니요 | 최대 30분 |
| `video_1` | 분류할 비디오로, 최대 60초입니다. | VIDEO | 아니요 | 최대 60초 |
| `text` | 질문의 대상이 되는 텍스트로, 프롬프트나 LLM 응답 등이며 최대 20000자입니다. | STRING | 아니요 | 최대 20000자 |

옵션은 2~255개로 지정해야 하며, 중복되는 옵션이나 대소문자만 다른 옵션이 있으면 노드에서 오류가 발생합니다. 분류할 입력을 최소 하나 이상 연결하고, 질문 안에서 소켓 이름으로 지칭하세요. 예: "Which season is shown in image_1?".

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `choice` | 선택된 옵션으로, `options`에 작성된 그대로입니다. | STRING |
| `option_index` | `options`에서 선택된 옵션의 위치이며 0부터 시작합니다. | INT |
| `confidence` | 선택에 대한 신뢰도로, 0에서 1 사이의 값입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/ko.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
