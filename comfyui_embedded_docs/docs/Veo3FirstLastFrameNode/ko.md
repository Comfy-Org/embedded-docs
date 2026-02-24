> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/ko.md)

Veo3FirstLastFrameNode는 Google의 Veo 3 모델을 사용하여 비디오를 생성합니다. 텍스트 프롬프트를 기반으로 비디오를 만들며, 제공된 첫 번째 프레임과 마지막 프레임을 사용하여 시퀀스의 시작과 끝을 안내합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | 해당 없음 | 비디오에 대한 텍스트 설명 (기본값: 빈 문자열). |
| `negative_prompt` | STRING | 아니요 | 해당 없음 | 비디오에서 피해야 할 내용을 안내하는 부정적 텍스트 프롬프트 (기본값: 빈 문자열). |
| `resolution` | COMBO | 예 | `"720p"`<br>`"1080p"` | 출력 비디오의 해상도. |
| `aspect_ratio` | COMBO | 아니요 | `"16:9"`<br>`"9:16"` | 출력 비디오의 화면비 (기본값: "16:9"). |
| `duration` | INT | 아니요 | 4 ~ 8 | 출력 비디오의 지속 시간(초) (기본값: 8). |
| `seed` | INT | 아니요 | 0 ~ 4294967295 | 비디오 생성을 위한 시드 값 (기본값: 0). |
| `first_frame` | IMAGE | 예 | 해당 없음 | 비디오의 시작 프레임. |
| `last_frame` | IMAGE | 예 | 해당 없음 | 비디오의 끝 프레임. |
| `model` | COMBO | 아니요 | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"` | 생성에 사용할 특정 Veo 3 모델 (기본값: "veo-3.1-fast-generate"). |
| `generate_audio` | BOOLEAN | 아니요 | 해당 없음 | 비디오에 대한 오디오 생성 여부 (기본값: True). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 파일. |
