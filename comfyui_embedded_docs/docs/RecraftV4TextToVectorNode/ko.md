# Recraft V4 텍스트-벡터

Recraft V4 Text to Vector 노드는 텍스트 설명에서 SVG(Scalable Vector Graphics) 이미지를 생성합니다. Recraft V4 및 V4.1 모델을 사용하여 이미지를 생성하기 위해 외부 API에 연결합니다. 이 노드는 프롬프트를 기반으로 하나 이상의 SVG 이미지를 출력합니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 생성에 사용할 모델입니다. 모델을 선택하면 사용 가능한 `size` 옵션이 변경됩니다. | DYNAMIC_COMBO | 예 | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 이미지 생성을 위한 프롬프트입니다. 최대 10,000자입니다. | STRING | 예 | N/A |
| `negative_prompt` | 이 입력은 무시됩니다. Recraft V4 및 V4.1 모델은 네거티브 프롬프트를 지원하지 않습니다. | STRING | 예 | N/A |
| `n` | 생성할 이미지 수입니다(기본값: 1). | INT | 예 | 1 to 6 |
| `seed` | 노드 재실행 여부를 결정하는 시드입니다. 실제 결과는 시드와 관계없이 비결정적입니다(기본값: 0). | INT | 예 | 0 to 18446744073709551615 |
| `recraft_controls` | Recraft Controls 노드를 통한 생성에 대한 선택적 추가 제어입니다. | CUSTOM | 아니요 | N/A |

### recraftv4_1_vector, recraftv4_1_utility_vector 및 recraftv4 입력

이 세 모델은 동일한 `size` 옵션을 공유합니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `size` | 생성된 이미지의 크기입니다(기본값: `"1024x1024"`). | COMBO | 예 | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector 및 recraftv4_pro 입력

이 세 모델은 동일한 `size` 옵션을 공유합니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `size` | 생성된 이미지의 크기입니다(기본값: `"2048x2048"`). | COMBO | 예 | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**참고:** `size` 매개변수는 선택한 `model`에 따라 사용 가능한 옵션이 변경되는 동적 입력입니다. `seed` 값은 외부 API에서 재현 가능한 결과를 보장하지 않습니다. Recraft V4 및 V4.1 모델은 네거티브 프롬프트를 지원하지 않으므로 `negative_prompt` 입력은 무시됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `output` | 생성된 SVG(Scalable Vector Graphics) 이미지입니다. | SVG |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/ko.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
