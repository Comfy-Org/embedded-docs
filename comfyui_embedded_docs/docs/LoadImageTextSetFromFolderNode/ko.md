> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/ko.md)

# LoadImageTextSetFromFolderNode

지정된 디렉토리에서 학습용 이미지 배치와 해당 이미지의 텍스트 캡션을 로드합니다. 이 노드는 자동으로 이미지 파일과 연결된 캡션 텍스트 파일을 검색하고, 지정된 크기 조정 설정에 따라 이미지를 처리한 후 제공된 CLIP 모델을 사용하여 캡션을 인코딩합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | 예 | - | 이미지를 로드할 폴더입니다. |
| `clip` | CLIP | 예 | - | 텍스트 인코딩에 사용되는 CLIP 모델입니다. |
| `resize_method` | COMBO | 아니요 | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | 이미지 크기 조정 방법입니다 (기본값: "None"). |
| `width` | INT | 아니요 | -1 ~ 10000 | 이미지 크기를 조정할 너비입니다. -1은 원본 너비를 사용함을 의미합니다 (기본값: -1). |
| `height` | INT | 아니요 | -1 ~ 10000 | 이미지 크기를 조정할 높이입니다. -1은 원본 높이를 사용함을 의미합니다 (기본값: -1). |

**참고:** CLIP 입력은 유효해야 하며 None일 수 없습니다. 체크포인트 로더 노드에서 CLIP 모델을 가져오는 경우, 체크포인트에 유효한 CLIP 또는 텍스트 인코더 모델이 포함되어 있는지 확인하십시오.

**폴더 구조 참고:** 이 노드는 kohya-ss/sd-scripts 폴더 구조를 지원합니다. 하위 폴더 이름이 숫자 뒤에 밑줄로 시작하는 경우(예: `5_myclass`), 해당 숫자는 반복 횟수로 사용되며 해당 하위 폴더 내의 이미지가 그 횟수만큼 로드됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 로드 및 처리된 이미지 배치입니다. |
| `CONDITIONING` | CONDITIONING | 텍스트 캡션에서 인코딩된 컨디셔닝 데이터입니다. |

---
**Source fingerprint (SHA-256):** `ffd6399783fc281a58bae811112d9ecacb51ab8ea3b512befa9b9fab2c6860de`
