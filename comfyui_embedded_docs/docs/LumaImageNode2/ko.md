# Luma UNI-1 이미지

## 개요

이 노드는 Luma UNI-1 모델을 사용하여 텍스트 설명에서 이미지를 생성합니다. 텍스트 프롬프트와 화면 비율, 스타일 등의 선택적 설정을 입력한 다음 Luma API에 요청을 보내 이미지를 만듭니다. 사용 가능한 모델 변형은 `uni-1`과 `uni-1-max` 두 가지입니다.

## 입력

### 공통 입력

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | 생성에 사용할 모델입니다. 모델을 선택하면 해당 모델에 대한 추가 설정이 표시됩니다. | DYNAMIC_COMBO | 예 | `"uni-1"`<br>`"uni-1-max"` |
| `prompt` | 원하는 이미지에 대한 텍스트 설명입니다. 1~6000자. | STRING | 예 | 1~6000자 |
| `seed` | 시드는 노드 재실행 여부를 제어합니다. 결과는 시드와 관계없이 비결정적입니다. (기본값: 0) | INT | 예 | 0 to 2147483647 |

### uni-1 및 uni-1-max 입력

`uni-1` 및 `uni-1-max` 모델 옵션에서 공유됩니다. 이 설정은 두 모델 중 하나를 선택하면 표시됩니다.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | 출력 이미지의 화면 비율입니다. `"auto"`는 프롬프트에 따라 모델이 선택하도록 합니다. (기본값: `"auto"`) | COMBO | 예 | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | 스타일 프리셋입니다. `"auto"`는 프롬프트에 따라 선택하며, `"manga"`는 만화/애니메이션 미학을 적용하고 세로형 화면 비율(2:3, 9:16, 1:2, 1:3)이 필요합니다. (기본값: `"auto"`) | COMBO | 예 | `"auto"`<br>`"manga"` |
| `web_search` | 생성 전에 웹에서 시각적 참조를 검색합니다. (기본값: False) | BOOLEAN | 예 | True / False |

### 참조 입력

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `image_ref` | 확장 가능한 슬롯: 1~9개 항목(예: `image_1`~`image_9`)을 연결할 수 있습니다. 스타일/콘텐츠 안내에 사용할 참조 이미지를 최대 9개까지 지원합니다. | IMAGE | 아니요 | 최대 9개 이미지 |

**참고:** `style`을 `"manga"`로 설정한 경우 `aspect_ratio`는 `"auto"` 또는 세로형 비율 `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"` 중 하나여야 합니다. `"manga"` 스타일에 다른 비율을 사용하면 오류가 발생합니다. 참조 이미지 최대 개수는 `uni-1` 및 `uni-1-max` 모두 9개입니다.

## 출력

| Output Name | Description | Data Type |
| --- | --- | --- |
| `image` | 생성된 이미지 텐서입니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/ko.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`
