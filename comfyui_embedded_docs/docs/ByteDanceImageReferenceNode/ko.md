> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/ko.md)

ByteDance Image Reference Node는 텍스트 프롬프트와 1개에서 4개의 참조 이미지를 사용하여 비디오를 생성합니다. 이 노드는 이미지와 프롬프트를 외부 API 서비스로 전송하여 사용자의 설명과 일치하는 비디오를 생성하면서 참조 이미지의 시각적 스타일과 콘텐츠를 통합합니다. 이 노드는 비디오 해상도, 화면비, 지속 시간 및 기타 생성 매개변수에 대한 다양한 제어 기능을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedance_1_lite | seedance_1_lite | 모델 이름 |
| `prompt` | STRING | STRING | - | - | 비디오 생성에 사용되는 텍스트 프롬프트입니다. |
| `images` | IMAGE | IMAGE | - | - | 1개에서 4개의 이미지입니다. |
| `resolution` | STRING | COMBO | - | 480p, 720p | 출력 비디오의 해상도입니다. |
| `aspect_ratio` | STRING | COMBO | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | 출력 비디오의 화면비입니다. |
| `duration` | INT | INT | 5 | 3-12 | 출력 비디오의 지속 시간(초 단위)입니다. |
| `seed` | INT | INT | 0 | 0-2147483647 | 생성에 사용할 시드 값입니다. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 비디오에 "AI 생성" 워터마크를 추가할지 여부입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 입력 프롬프트와 참조 이미지를 기반으로 생성된 비디오 파일입니다. |
