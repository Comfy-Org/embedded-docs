# Google Gemini Decision (Choice)

연결한 텍스트, 이미지, 오디오 또는 비디오에 대해 직접 지정한 옵션 중 하나를 선택하고, 선택된 옵션과 그 위치, 신뢰도를 반환합니다. `choice`를 동일한 옵션 이름을 입력으로 갖는 Branch 노드에 연결하거나, Branch 노드를 사용할 수 없을 때는 `option_index`를 기준으로 라우팅하십시오.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 사용할 모델입니다(기본값: `"gemini-decision-1"`). | COMBO | 예 | `"gemini-decision-1"` |
| `question` | 옵션이 답하는 질문으로, 최대 5000자입니다(기본값: "What style is the image?"). | STRING | 예 | 1~5000자 |
| `options` | 한 줄에 하나의 옵션을 입력하며, 입력한 그대로 사용되고 각 옵션은 최대 128자입니다. 어느 옵션에도 해당하지 않는 입력을 위해 `other`와 같은 옵션을 추가하십시오(기본값: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | 예 | 2~255개 옵션 |
| `images` | 분류할 이미지로, 확장 가능한 슬롯(`image_1` ... `image_16`) 전체에서 최대 16개입니다. 배치로 묶인 이미지는 이미지당 한 번씩 계산됩니다. | IMAGE | 아니요 | 최대 16개 이미지 |
| `audio` | 분류할 오디오 클립입니다. | AUDIO | 아니요 | - |
| `video` | 분류할 비디오 클립입니다. | VIDEO | 아니요 | - |
| `text` | 질문의 대상이 되는 텍스트(예: 프롬프트 또는 LLM 응답)로, 최대 20000자입니다. | STRING | 아니요 | 최대 20000자 |

옵션은 최소 2개, 최대 255개를 지정하고 동일한 옵션을 두 번 나열하지 마십시오. 그렇지 않으면 노드에서 오류가 발생합니다. `text`, `images`, `audio`, `video` 중 하나 이상을 연결하고, 이미지를 여러 개 사용할 때는 질문 안에서 `image_1`, `image_2` 등으로 이름을 지정하십시오.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `choice` | 선택된 옵션으로, `options`에 작성된 그대로입니다. | STRING |
| `option_index` | `options`에서 선택된 옵션의 위치이며 0부터 시작합니다. | INT |
| `confidence` | 선택에 대한 신뢰도로, 0과 1 사이입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/ko.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
