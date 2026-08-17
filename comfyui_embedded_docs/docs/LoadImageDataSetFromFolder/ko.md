# 폴더에서 이미지 데이터셋 불러오기

이 노드는 선택한 폴더에서 이미지 데이터셋을 로드하여 목록으로 반환합니다. 폴더는 ComfyUI의 기본 입력 디렉토리 내부에 있는 하위 폴더여야 합니다. 지원되는 이미지 형식은 PNG, JPG, JPEG, WEBP입니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `folder` | 이미지를 로드할 폴더입니다. 사용 가능한 옵션은 ComfyUI의 기본 입력 디렉토리에 존재하는 하위 폴더들입니다. 이 디렉토리 밖으로 경로가 벗어나는 값(예: ".." 사용)은 거부됩니다. | COMBO | 예 | *사용 가능한 여러 옵션* — ComfyUI 입력 디렉토리에 있는 하위 폴더들 |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `images` | 로드된 이미지 목록입니다. 이 노드는 선택한 폴더에서 발견된 모든 유효한 이미지 파일(PNG, JPG, JPEG, WEBP)을 로드하여 목록으로 반환합니다. 폴더에 지원되는 이미지 파일이 없으면 오류가 발생합니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/ko.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
