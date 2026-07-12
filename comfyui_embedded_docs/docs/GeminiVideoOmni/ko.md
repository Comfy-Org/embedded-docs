# Google Gemini Omni (Video)

Google의 Gemini Omni Flash 모델을 사용하여 텍스트 프롬프트로 오디오가 포함된 영상을 생성합니다. 결과를 안내하거나 편집하기 위해 참조 이미지 및/또는 영상을 선택적으로 제공할 수 있습니다. 원하는 길이(3~10초)와 화면 비율(16:9 또는 9:16)을 프롬프트에 직접 작성하세요.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 영상 생성을 위해 사용되는 Gemini video 모델입니다. | MODEL | Yes | "Omni Flash" |
| `seed` | seed는 노드가 다시 실행될지 여부를 제어합니다. seed와 관계없이 결과는 비결정적입니다. | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/ko.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
