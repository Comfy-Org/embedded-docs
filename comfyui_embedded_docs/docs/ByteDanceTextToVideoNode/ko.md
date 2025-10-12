> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/ko.md)

ByteDance Text to Video 노드는 텍스트 프롬프트를 기반으로 API를 통해 ByteDance 모델을 사용하여 동영상을 생성합니다. 텍스트 설명과 다양한 동영상 설정을 입력으로 받아 제공된 사양과 일치하는 동영상을 생성합니다. 이 노드는 API 통신을 처리하고 생성된 동영상을 출력으로 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | 콤보 | seedance_1_pro | Text2VideoModelName 옵션 | 모델 이름 |
| `prompt` | STRING | 문자열 | - | - | 동영상 생성에 사용되는 텍스트 프롬프트입니다. |
| `resolution` | STRING | 콤보 | - | ["480p", "720p", "1080p"] | 출력 동영상의 해상도입니다. |
| `aspect_ratio` | STRING | 콤보 | - | ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | 출력 동영상의 종횡비입니다. |
| `duration` | INT | 정수 | 5 | 3-12 | 출력 동영상의 길이(초 단위)입니다. |
| `seed` | INT | 정수 | 0 | 0-2147483647 | 생성에 사용할 시드 값입니다. (선택 사항) |
| `camera_fixed` | BOOLEAN | 불린 | False | - | 카메라를 고정할지 여부를 지정합니다. 플랫폼이 카메라 고정 지시사항을 프롬프트에 추가하지만, 실제 효과를 보장하지는 않습니다. (선택 사항) |
| `watermark` | BOOLEAN | 불린 | True | - | 동영상에 "AI 생성" 워터마크를 추가할지 여부입니다. (선택 사항) |

**매개변수 제약 조건:**

- `prompt` 매개변수는 공백 제거 후 최소 1자 이상을 포함해야 합니다.
- `prompt` 매개변수는 다음 텍스트 매개변수를 포함할 수 없습니다: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark"
- `duration` 매개변수는 3초에서 12초 사이의 값으로 제한됩니다.
- `seed` 매개변수는 0부터 2,147,483,647까지의 값을 허용합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 동영상 파일 |
