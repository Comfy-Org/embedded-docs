# 비디오 저장

SaveVideo 노드는 입력 비디오를 ComfyUI 출력 디렉터리에 저장합니다. 파일 이름 접두사, 비디오 형식, 코덱을 선택할 수 있으며, 카운터를 추가하여 고유한 파일 이름을 자동으로 생성합니다. 기본적으로 이 노드는 저장된 비디오에 워크플로우 메타데이터도 포함합니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `codec` | 비디오에 사용할 코덱입니다. `h264`를 선택하면 추가 인코딩 옵션이 표시됩니다(기본값: "auto"). | DYNAMIC_COMBO | 예 | "auto"<br>"h264" |
| `video` | 저장할 비디오입니다. | VIDEO | 예 | - |
| `filename_prefix` | 저장할 파일의 접두사입니다. `%date:yyyy-MM-dd%` 또는 `%Empty Latent Image.width%`와 같은 형식 정보를 포함하여 노드 값을 포함할 수 있습니다(기본값: "video/ComfyUI"). | STRING | 예 | - |
| `format` | 비디오를 저장할 형식입니다. 저장된 비디오의 파일 확장자를 결정합니다(기본값: "auto"). | COMBO | 예 | "auto"<br>"mp4"<br>"webm"<br>"mkv"<br>"gif" |

### h264 입력

이 입력은 `codec`이 `h264`로 설정된 경우 표시됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `encoding` | H.264 인코딩 모드입니다. 자동(auto)은 호환 가능한 H.264 스트림을 유지합니다. 다시 인코딩(re-encode)은 사용자 지정 CRF를 적용합니다(기본값: "auto"). | DYNAMIC_COMBO | 아니요 | "auto"<br>"re-encode" |
| `crf` | 값이 낮을수록 품질이 높아지고 파일 크기가 커집니다. `encoding`이 `re-encode`로 설정된 경우에만 사용할 수 있습니다(기본값: 23.0). | FLOAT | 예(`encoding`이 `re-encode`인 경우에만) | 0.0 ~ 51.0(단계: 1.0) |

참고: `filename_prefix`에 폴더가 포함된 경우(예: `video/ComfyUI`) 비디오는 출력 디렉터리의 해당 하위 폴더에 저장됩니다. 파일 이름은 접두사에 카운터가 추가되어 생성됩니다(예: `ComfyUI_00001_.mp4`). 따라서 기존 파일을 덮어쓰지 않습니다.

참고: 메타데이터가 활성화되면 노드는 저장된 비디오에 워크플로우 프롬프트와 추가 메타데이터를 포함합니다. `--disable-metadata` 인수로 ComfyUI를 시작하면 메타데이터를 비활성화할 수 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `video` | 입력에서 전달되어 저장된 비디오입니다. | VIDEO |
| `ui` | UI에 표시하기 위한 파일 경로 및 하위 폴더 정보를 포함한 저장된 비디오 파일의 미리보기입니다. | PREVIEW_VIDEO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/ko.md)

---
**Source fingerprint (SHA-256):** `c1fd5ac1043f0811951136b2d09cd59840b0c542079da9ed04c17cca7c02562b`
