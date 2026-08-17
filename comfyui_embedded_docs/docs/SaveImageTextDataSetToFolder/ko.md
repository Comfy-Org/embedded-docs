# 이미지 및 텍스트 데이터셋을 폴더에 저장

Save Image-Text (to Folder)는 이미지와 텍스트 캡션의 쌍으로 구성된 데이터셋을 ComfyUI의 출력 디렉터리 안에 있는 폴더에 저장하는 출력 노드입니다. 각 이미지는 PNG 파일로 저장되며, 캡션이 제공되면 각 이미지에 대해 동일한 기본 이름을 가진 대응하는 TXT 파일이 생성됩니다. 이는 생성된 이미지와 해당 설명의 체계적인 데이터셋을 구축하는 데 유용합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `images` | 저장할 이미지 목록입니다. | IMAGE | 예 | - |
| `texts` | 저장할 텍스트 캡션 목록입니다. 이 입력은 선택 사항입니다. | STRING | 아니요 | - |
| `folder_name` | 이미지를 저장할 폴더 이름입니다(출력 디렉터리 내). (기본값: "dataset") | STRING | 예 | - |
| `filename_prefix` | 저장되는 이미지 파일 이름의 접두사입니다. (기본값: "image") | STRING | 예 | - |
| `mode` | 기존 파일을 덮어쓸지, 아니면 덮어쓰기를 피하기 위해 파일 이름을 증가시킬지 결정합니다. (기본값: "overwrite") | COMBO | 예 | "overwrite"<br>"increment" |

**참고:** `images` 입력은 목록입니다. `texts` 입력은 선택 사항이며, 제공할 경우 텍스트 캡션 목록이어야 합니다. 캡션은 이미지와 순서대로 짝지어지며, 각 캡션은 해당 이미지와 같은 기본 이름을 가진 UTF-8 `.txt` 파일로 저장됩니다(예: `image_00000.png`에 대한 `image_00000.txt`). 캡션 수가 이미지 수보다 적으면 나머지 이미지는 캡션 없이 저장되고, 초과되는 캡션은 무시됩니다.

기본값이 있는 입력(`folder_name`, `filename_prefix`, `mode`)은 연결할 필요가 없으며, 기본값이 자동으로 사용됩니다.

`mode`가 `overwrite`(기본값)로 설정되면 이미지는 `image_00000.png`와 같은 이름으로 저장되며, 같은 이름의 기존 파일을 덮어씁니다. `mode`가 `increment`로 설정되면 자동으로 증가하는 카운터가 파일 이름에 추가되어 기존 파일을 덮어쓰지 않습니다.

`folder_name` 값은 ComfyUI 출력 디렉터리 내부의 위치로 확인되어야 합니다. 출력 디렉터리를 벗어나려는 폴더 이름(예: `..` 사용)은 거부됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| - | 이 노드에는 출력이 없습니다. 파일을 파일 시스템에 직접 저장합니다. | - |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/ko.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
