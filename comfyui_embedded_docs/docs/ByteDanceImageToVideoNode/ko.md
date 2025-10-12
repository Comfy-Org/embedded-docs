> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/ko.md)

ByteDance Image to Video 노드는 입력 이미지와 텍스트 프롬프트를 기반으로 API를 통해 ByteDance 모델을 사용하여 비디오를 생성합니다. 시작 이미지 프레임을 가져와 제공된 설명을 따르는 비디오 시퀀스를 생성합니다. 이 노드는 비디오 해상도, 화면비, 지속 시간 및 기타 생성 매개변수에 대한 다양한 사용자 지정 옵션을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | COMBO | seedance_1_pro | Image2VideoModelName 옵션 | 모델 이름 |
| `prompt` | STRING | STRING | - | - | 비디오 생성에 사용되는 텍스트 프롬프트입니다. |
| `image` | IMAGE | IMAGE | - | - | 비디오에 사용될 첫 번째 프레임입니다. |
| `resolution` | STRING | COMBO | - | ["480p", "720p", "1080p"] | 출력 비디오의 해상도입니다. |
| `aspect_ratio` | STRING | COMBO | - | ["adaptive", "16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | 출력 비디오의 화면비입니다. |
| `duration` | INT | INT | 5 | 3-12 | 출력 비디오의 지속 시간(초 단위)입니다. |
| `seed` | INT | INT | 0 | 0-2147483647 | 생성에 사용할 시드 값입니다. |
| `camera_fixed` | BOOLEAN | BOOLEAN | False | - | 카메라를 고정할지 여부를 지정합니다. 플랫폼은 카메라를 고정하라는 지시를 프롬프트에 추가하지만, 실제 효과를 보장하지는 않습니다. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 비디오에 "AI 생성" 워터마크를 추가할지 여부입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 입력 이미지와 프롬프트 매개변수를 기반으로 생성된 비디오 파일입니다. |
