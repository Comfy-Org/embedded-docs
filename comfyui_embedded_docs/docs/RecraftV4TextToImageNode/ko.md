# Recraft V4 텍스트-이미지

이 노드는 Recraft V4 및 V4.1 AI 모델을 사용하여 텍스트 설명으로부터 이미지를 생성합니다. 프롬프트와 생성 설정을 Recraft 이미지 생성 서비스로 전송하고, 생성된 이미지 또는 이미지들을 반환합니다. 모델, 이미지 크기, 생성할 이미지 수를 선택할 수 있습니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 생성에 사용할 모델입니다. 모델을 선택하면 사용 가능한 `size` 옵션이 결정됩니다. | DYNAMIC_COMBO | 예 | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 이미지 생성을 위한 프롬프트입니다. 최대 10,000자까지 입력할 수 있습니다. | STRING | 예 | 1~10000자 |
| `negative_prompt` | 이 입력은 무시됩니다. Recraft V4 및 V4.1 모델은 네거티브 프롬프트를 지원하지 않습니다. | STRING | 예 | N/A |
| `n` | 생성할 이미지 수입니다(기본값: 1). | INT | 예 | 1~6 |
| `seed` | 노드 재실행 여부를 결정하는 시드입니다. 시드와 관계없이 실제 결과는 비결정적입니다(기본값: 0). | INT | 예 | 0~18446744073709551615 |
| `recraft_controls` | Recraft Controls 노드를 통해 생성에 대한 추가 제어를 제공하는 선택적 입력입니다. | CUSTOM | 아니요 | N/A |

### recraftv4_1, recraftv4_1_utility 및 recraftv4 입력

`recraftv4_1`, `recraftv4_1_utility` 및 `recraftv4` 모델이 공통으로 사용하는 입력입니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `size` | 생성된 이미지의 크기입니다(기본값: 1024x1024). | COMBO | 예 | 여러 옵션 사용 가능(표준 Recraft V4 크기) |

### recraftv4_1_pro, recraftv4_1_utility_pro 및 recraftv4_pro 입력

`recraftv4_1_pro`, `recraftv4_1_utility_pro` 및 `recraftv4_pro` 모델이 공통으로 사용하는 입력입니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `size` | 생성된 이미지의 크기입니다(기본값: 2048x2048). | COMBO | 예 | 여러 옵션 사용 가능(Pro Recraft V4 크기) |

**참고 사항:**

- `size` 입력은 모델을 선택하면 나타나며, 사용 가능한 옵션은 모델에 따라 달라집니다. 표준 모델(`recraftv4_1`, `recraftv4_1_utility`, `recraftv4`)은 동일한 크기 세트를 공유하는 반면, Pro 모델(`recraftv4_1_pro`, `recraftv4_1_utility_pro`, `recraftv4_pro`)은 다른 크기 세트를 공유합니다.
- `negative_prompt` 입력은 UI에 표시되지만 모델로 전송되지는 않습니다. Recraft V4 및 V4.1 모델은 네거티브 프롬프트를 지원하지 않습니다.
- `seed` 값은 값이 변경될 때 노드가 재실행되는지 여부만 결정합니다. 실제 이미지 결과는 시드와 관계없이 비결정적입니다.
- Recraft Controls 입력을 통해 Infinite Style Library의 스타일 ID를 사용하는 경우, Vector 아트 스타일이 아닌지 확인하세요. Vector 아트 스타일의 경우 이미지 대신 SVG 데이터가 반환될 수 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `output` | 생성된 이미지 또는 이미지 배치입니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/ko.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
