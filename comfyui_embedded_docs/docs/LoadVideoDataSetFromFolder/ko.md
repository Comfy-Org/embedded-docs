# 비디오 불러오기 (폴더에서)

Loads all supported video files from a selected folder inside the ComfyUI input directory and returns them as a list of video references. This node returns lazy video references, so frames are decoded only when another node actually needs them. Supported formats: MP4, AVI, MOV, WEBM, MKV, and FLV.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `folder` | 비디오 파일이 포함된 폴더입니다. ComfyUI 입력 디렉터리 안의 사용 가능한 하위 폴더에서 선택합니다. | COMBO | 예 | ComfyUI 입력 디렉터리에서 사용 가능한 모든 하위 폴더 |

**참고:** 선택한 폴더에는 지원되는 비디오 파일이 하나 이상 포함되어 있어야 합니다. 지원되는 확장자는 MP4, AVI, MOV, WEBM, MKV 및 FLV입니다. 지원되는 비디오 파일이 없으면 노드에서 오류가 발생합니다. 폴더는 ComfyUI 입력 디렉터리 내부의 위치로 확인되어야 하며, 해당 디렉터리를 벗어나려는 폴더 이름(예: "..")은 오류와 함께 거부됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `videos` | 선택한 폴더의 각 비디오 파일에 대한 지연 비디오 참조 목록입니다. 프레임은 다른 노드에서 출력을 소비할 때만 디코딩됩니다. | VIDEO (list) |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/ko.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
