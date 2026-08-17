# 이미지 저장

SaveImage 노드는 수신한 이미지를 사용자의 `ComfyUI/output` 디렉토리에 저장합니다. 각 이미지를 PNG 파일로 저장하며, 프롬프트와 같은 워크플로우 메타데이터를 추후 참조할 수 있도록 저장된 파일에 포함할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `images` | 저장할 이미지입니다. | IMAGE | 예 | - |
| `filename_prefix` | 저장할 파일의 접두사입니다. 노드의 값을 포함하기 위해 `%date:yyyy-MM-dd%` 또는 `%Empty Latent Image.width%`와 같은 형식 정보를 포함할 수 있습니다 (기본값: "ComfyUI"). | STRING | 예 | - |
| `prompt` | 숨겨진 입력으로, ComfyUI가 자동으로 제공합니다. 저장된 PNG 파일에 메타데이터로 포함되는 프롬프트 데이터입니다. | PROMPT | 아니요 | - |
| `extra_pnginfo` | 숨겨진 입력으로, ComfyUI가 자동으로 제공합니다. 저장된 PNG 파일에 메타데이터로 포함되는 추가 워크플로우 정보입니다. | EXTRA_PNGINFO | 아니요 | - |

각 이미지는 PNG 파일로 저장됩니다. 저장된 파일 이름에서 접두사의 `%batch_num%`은 이미지의 배치 번호로 대체되며, 0으로 채워진 카운터가 추가됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `images` | 저장된 것과 동일한 이미지로, 다른 노드에서 사용할 수 있도록 전달됩니다. | IMAGE |
| `ui` | ComfyUI 인터페이스에 표시되는, 파일 이름, 하위 폴더 및 유형이 있는 저장된 이미지 목록을 포함하는 UI 결과입니다. | UI_RESULT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/ko.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
