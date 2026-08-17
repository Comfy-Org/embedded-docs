# Kling 비디오 생성 (시작-끝 프레임)

이 노드는 제공한 시작 이미지와 종료 이미지 사이를 전환하는 비디오 시퀀스를 생성합니다. 첫 번째 프레임에서 마지막 프레임까지의 모든 중간 프레임을 생성하여 부드러운 변환을 만들어냅니다. 이 노드는 image-to-video API를 호출하지만 `image_tail` 요청 필드와 함께 작동하는 입력 옵션만 지원합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | 참조 이미지 - URL 또는 Base64 인코딩 문자열, 10MB를 초과할 수 없으며 해상도는 300*300px 이상이어야 합니다. 종횡비는 1:2.5 ~ 2.5:1 사이여야 합니다. Base64는 data:image 접두사를 포함하지 않아야 합니다. | IMAGE | 예 | - |
| `end_frame` | 참조 이미지 - 종료 프레임 제어. URL 또는 Base64 인코딩 문자열, 10MB를 초과할 수 없으며 해상도는 300*300px 이상이어야 합니다. Base64는 data:image 접두사를 포함하지 않아야 합니다. | IMAGE | 예 | - |
| `prompt` | 긍정 텍스트 프롬프트 | STRING | 예 | - |
| `negative_prompt` | 부정 텍스트 프롬프트 | STRING | 예 | - |
| `cfg_scale` | 프롬프트 가이던스의 강도를 제어합니다 (기본값: 0.5) | FLOAT | 아니요 | 0.0-1.0 |
| `aspect_ratio` | 생성된 비디오의 종횡비 (기본값: "16:9") | COMBO | 아니요 | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | 비디오 생성에 사용할 구성으로, 형식은 mode / duration / model_name입니다. (기본값: "pro mode / 5s duration / kling-v2-5-turbo"). 사용 가능한 모든 옵션은 kling-v2-5-turbo 모델과 함께 pro mode를 사용하며 비디오 길이만 다릅니다. | COMBO | 아니요 | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**이미지 제약 조건:**

- `start_frame`과 `end_frame`은 모두 제공되어야 하며 파일 크기가 10MB를 초과할 수 없습니다.
- 두 이미지 모두 최소 해상도는 300×300픽셀입니다.
- `start_frame`의 종횡비는 1:2.5 ~ 2.5:1 사이여야 합니다.
- Base64 인코딩 이미지는 "data:image" 접두사를 포함하지 않아야 합니다.

**프롬프트 제약 조건:**

- 긍정 프롬프트는 비어 있을 수 없습니다.
- 긍정 및 부정 프롬프트 모두 500자로 제한됩니다.
- `negative_prompt`를 비워 두면 요청에서 생략됩니다.

**가격:**

- "pro mode / 5s duration / kling-v2-5-turbo": 생성당 $0.35 USD
- "pro mode / 10s duration / kling-v2-5-turbo": 생성당 $0.70 USD

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `output` | 생성된 비디오 시퀀스 | VIDEO |
| `video_id` | 생성된 비디오의 고유 식별자 | STRING |
| `duration` | 생성된 비디오의 지속 시간 | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/ko.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
