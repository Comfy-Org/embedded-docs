> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/ko.md)

AudioEncoderLoader 노드는 사용 가능한 오디오 인코더 파일에서 오디오 인코더 모델을 불러옵니다. 오디오 인코더 파일 이름을 입력으로 받아, 워크플로우에서 오디오 처리 작업에 사용할 수 있는 불러온 오디오 인코더 모델을 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder_name` | STRING | COMBO | - | 사용 가능한 오디오 인코더 파일 | audio_encoders 폴더에서 불러올 오디오 인코더 모델 파일을 선택합니다 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `audio_encoder` | AUDIO_ENCODER | 오디오 처리 워크플로우에서 사용하기 위해 불러온 오디오 인코더 모델을 반환합니다 |