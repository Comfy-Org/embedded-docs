# 배경 제거 모델 불러오기

파일에서 배경 제거 모델을 로드하여 다른 노드가 이미지에서 배경을 제거할 때 사용할 수 있도록 준비합니다. 모델 파일은 배경 제거 폴더의 사용 가능한 파일 중에서 선택됩니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | 이미지에서 배경을 제거하는 데 사용되는 모델입니다. | COMBO | 예 | 사용 가능한 모델 파일 목록 (background_removal 폴더에 있는 파일의 정렬된 목록) |

**참고:** 선택한 파일에 유효한 배경 제거 모델이 포함되어 있지 않으면 노드에서 오류가 발생합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `bg_model` | 로드된 배경 제거 모델로, 다른 노드가 이미지를 처리할 때 사용할 수 있습니다. | BACKGROUND_REMOVAL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/ko.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
