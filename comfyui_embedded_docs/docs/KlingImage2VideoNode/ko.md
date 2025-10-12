> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/ko.md)

Kling Image to Video Node는 시작 이미지와 텍스트 프롬프트를 사용하여 비디오 콘텐츠를 생성합니다. 참조 이미지를 입력받아 제공된 긍정 및 부정 텍스트 설명을 기반으로 비디오 시퀀스를 생성하며, 모델 선택, 지속 시간, 화면 비율 등 다양한 구성 옵션을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 예 | - | 비디오 생성에 사용되는 참조 이미지입니다. |
| `prompt` | STRING | 예 | - | 긍정 텍스트 프롬프트입니다. |
| `negative_prompt` | STRING | 예 | - | 부정 텍스트 프롬프트입니다. |
| `model_name` | COMBO | 예 | 여러 옵션 사용 가능 | 비디오 생성을 위한 모델 선택 (기본값: "kling-v2-master"). |
| `cfg_scale` | FLOAT | 예 | 0.0-1.0 | 구성 스케일 매개변수 (기본값: 0.8). |
| `mode` | COMBO | 예 | 여러 옵션 사용 가능 | 비디오 생성 모드 선택 (기본값: std). |
| `aspect_ratio` | COMBO | 예 | 여러 옵션 사용 가능 | 생성된 비디오의 화면 비율 (기본값: field_16_9). |
| `duration` | COMBO | 예 | 여러 옵션 사용 가능 | 생성된 비디오의 지속 시간 (기본값: field_5). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 출력입니다. |
| `video_id` | STRING | 생성된 비디오의 고유 식별자입니다. |
| `duration` | STRING | 생성된 비디오의 지속 시간 정보입니다. |