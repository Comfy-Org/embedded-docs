> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/ko.md)

Kling Text to Video 노드는 텍스트 설명을 비디오 콘텐츠로 변환합니다. 텍스트 프롬프트를 입력받아 지정된 구성 설정을 기반으로 해당하는 비디오 시퀀스를 생성합니다. 이 노드는 다양한 화면비와 생성 모드를 지원하여 다양한 길이와 품질의 비디오를 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 긍정적 텍스트 프롬프트 (기본값: 없음) |
| `negative_prompt` | STRING | 예 | - | 부정적 텍스트 프롬프트 (기본값: 없음) |
| `cfg_scale` | FLOAT | 아니오 | 0.0-1.0 | 구성 스케일 값 (기본값: 1.0) |
| `aspect_ratio` | COMBO | 아니오 | KlingVideoGenAspectRatio의 옵션들 | 비디오 화면비 설정 (기본값: "16:9") |
| `mode` | COMBO | 아니오 | 여러 옵션 사용 가능 | 비디오 생성에 사용할 구성으로, 형식: 모드/지속시간/모델_이름을 따릅니다. (기본값: modes[4]) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 출력 |
| `video_id` | STRING | 생성된 비디오의 고유 식별자 |
| `duration` | STRING | 생성된 비디오의 지속 시간 정보 |