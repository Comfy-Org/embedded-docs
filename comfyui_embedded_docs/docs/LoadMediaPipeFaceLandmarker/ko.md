# MediaPipe 얼굴 랜드마커 불러오기

이 노드는 이미지에서 얼굴과 얼굴 랜드마크(눈, 코, 입 등)를 감지할 수 있는 MediaPipe Face Landmarker v2 모델을 로드합니다. 로드된 모델에는 두 가지 감지 변형(short 및 full)과 함께 얼굴 분석을 위한 공유 메시 데이터, 블렌드셰이프, 표준 기하 구조가 포함되어 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 형식 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | `models/detection/` 디렉토리의 얼굴 감지 모델입니다. | COMBO | 예 | `models/detection/` 디렉토리에서 사용 가능한 모델 목록 |

## 출력

| 출력 이름 | 설명 | 데이터 형식 |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | 두 가지 감지 변형(short/full), 공유 메시 및 블렌드셰이프 데이터, 표준 기하 구조, 얼굴 토폴로지 연결 집합, GPU 관리를 위한 모델 패처를 포함하는 로드된 MediaPipe Face Landmarker 모델 객체입니다. | FACE_DETECTION_MODEL |

**참고:** 출력은 얼굴 감지 및 랜드마크 추출 작업을 위해 다른 노드에서 사용할 수 있는 복잡한 객체입니다. 여기에는 근거리 감지용 "short" 변형과 전체 범위 감지용 "full" 변형의 두 가지 감지 변형이 포함되어 있습니다.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/ko.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
