# 이미지 데이터셋을 폴더에 저장

이 노드는 ComfyUI의 출력 디렉터리 내부에 지정된 폴더에 이미지 목록을 PNG 파일로 저장합니다. 이 노드는 더 이상 사용되지 않습니다(deprecated). 이 노드는 중복되며, 대상 폴더를 파일 이름 접두사에 지정할 수 있는 기존 Save Image 노드로 대체되었습니다. 이 노드는 수신된 각 이미지를 사용자 지정 파일 이름 접두사를 사용하여 디스크에 저장하며, 기존 파일을 덮어쓰거나 덮어쓰기를 방지하기 위해 파일 이름을 증가시켜 저장할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `images` | 저장할 이미지 목록입니다. | IMAGE | 예 | N/A |
| `folder_name` | 이미지를 저장할 폴더의 이름입니다(출력 디렉터리 내부). 기본값은 "dataset"입니다. | STRING | 아니요 | N/A |
| `filename_prefix` | 저장되는 이미지 파일 이름의 접두사입니다. 기본값은 "image"입니다. | STRING | 아니요 | N/A |
| `mode` | 기존 파일을 덮어쓸지, 아니면 덮어쓰기를 방지하기 위해 파일 이름을 증가시킬지 여부입니다. 기본값은 "overwrite"입니다. | COMBO | 아니요 | "overwrite"<br>"increment" |

**참고:** `images` 입력은 목록이므로 한 번에 여러 이미지를 수신하여 처리할 수 있습니다. 모든 입력은 목록으로 수신됩니다. `folder_name`, `filename_prefix`, `mode`의 경우 연결된 목록의 첫 번째 값만 사용됩니다. `folder_name`은 ComfyUI의 출력 디렉터리 내부에 있는 폴더를 가리켜야 합니다. 출력 디렉터리를 벗어나는 폴더 이름(예: "..", 절대 경로, 드라이브 문자를 사용하는 경우)은 오류와 함께 거부됩니다. 이미지는 항상 PNG 형식으로 저장됩니다. `filename_prefix` 매개변수는 고급 옵션입니다.

## 출력

이 노드에는 데이터 출력이 없습니다. 파일 시스템에 저장 작업을 수행하는 출력 노드입니다.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/ko.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
