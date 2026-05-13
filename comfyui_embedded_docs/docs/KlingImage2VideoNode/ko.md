> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/ko.md)

# Kling 이미지-투-비디오 노드

Kling 이미지-투-비디오 노드는 시작 참조 이미지와 텍스트 프롬프트를 사용하여 비디오를 생성합니다. 이미지를 첫 번째 프레임으로 사용하고, 긍정 및 부정 텍스트 설명을 기반으로 비디오 시퀀스를 생성하며, 모델, 지속 시간, 화면 비율 및 생성 모드에 대한 구성 가능한 옵션을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 예 | - | 비디오 생성에 사용되는 참조 이미지입니다. |
| `prompt` | STRING | 예 | - | 긍정 텍스트 프롬프트입니다. |
| `negative_prompt` | STRING | 예 | - | 부정 텍스트 프롬프트입니다. |
| `model_name` | COMBO | 예 | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` | 비디오 생성에 사용되는 모델입니다(기본값: `"kling-v2-master"`). |
| `cfg_scale` | FLOAT | 예 | 0.0 ~ 1.0 | 비디오가 프롬프트를 얼마나 밀접하게 따르는지 제어합니다. 값이 높을수록 더 강하게 따릅니다(기본값: 0.8). |
| `mode` | COMBO | 예 | `"std"`<br>`"pro"` | 생성 모드입니다. `"std"`는 표준 품질, `"pro"`는 더 높은 품질입니다(기본값: `"std"`). |
| `aspect_ratio` | COMBO | 예 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 생성된 비디오의 화면 비율입니다(기본값: `"16:9"`). |
| `duration` | COMBO | 예 | `"5"`<br>`"10"` | 생성된 비디오의 지속 시간(초)입니다(기본값: `"5"`). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 출력입니다. |
| `video_id` | STRING | 생성된 비디오의 고유 식별자입니다. |
| `duration` | STRING | 생성된 비디오의 지속 시간 정보입니다. |

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`
