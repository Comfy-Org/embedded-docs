> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/ko.md)

# Kling 이미지 생성 노드

Kling 이미지 생성 노드는 텍스트 프롬프트로부터 이미지를 생성하며, 참조 이미지를 사용하여 가이드할 수 있는 옵션을 제공합니다. 텍스트 설명과 참조 설정을 기반으로 하나 이상의 이미지를 생성한 후, 생성된 이미지를 출력으로 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 긍정 텍스트 프롬프트 |
| `negative_prompt` | STRING | 예 | - | 부정 텍스트 프롬프트 |
| `image_type` | COMBO | 예 | `"subject_reference"`<br>`"style_reference"` | 이미지 참조 유형 선택(고급). 참조 이미지가 제공될 때 필요합니다. |
| `image_fidelity` | FLOAT | 예 | 0.0 - 1.0 | 사용자 업로드 이미지의 참조 강도(기본값: 0.5, 고급) |
| `human_fidelity` | FLOAT | 예 | 0.0 - 1.0 | 피사체 참조 유사도(기본값: 0.45, 고급) |
| `model_name` | COMBO | 예 | `"kling-v3"`<br>`"kling-v2"`<br>`"kling-v1-5"` | 이미지 생성을 위한 모델 선택(기본값: "kling-v3") |
| `aspect_ratio` | COMBO | 예 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | 생성된 이미지의 화면 비율(기본값: "16:9") |
| `n` | INT | 예 | 1 - 9 | 생성할 이미지 수(기본값: 1) |
| `image` | IMAGE | 아니요 | - | 선택적 참조 이미지 |
| `seed` | INT | 아니요 | 0 - 2147483647 | 시드는 노드 재실행 여부를 제어합니다. 시드와 관계없이 결과는 비결정적입니다(기본값: 0) |

**매개변수 제약 조건:**

- `image` 매개변수는 선택 사항입니다. 참조 이미지가 제공될 경우 `image_type` 매개변수를 반드시 `"subject_reference"` 또는 `"style_reference"`로 설정해야 합니다.
- 참조 이미지가 제공되지 않을 경우 `image_type`, `image_fidelity`, `human_fidelity` 매개변수는 사용되지 않습니다.
- 프롬프트와 부정 프롬프트의 최대 길이는 `MAX_PROMPT_LENGTH_IMAGE_GEN`자입니다.
- `seed` 매개변수는 선택 사항이며 결정적 결과를 보장하지 않습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | IMAGE | 입력 매개변수를 기반으로 생성된 이미지 |

---
**Source fingerprint (SHA-256):** `f25164f4007b1f62285e76519238b5061b63597e1a06365acf93d4289063bd3a`
