> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/en.md)

TripoRefineNode는 특히 v1.4 Tripo 모델이 생성한 초안 3D 모델을 정제합니다. 모델 작업 ID를 받아 Tripo API를 통해 처리하여 개선된 버전의 모델을 생성합니다. 이 노드는 Tripo v1.4 모델이 생성한 초안 모델에만 작동하도록 설계되었습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | 예 | - | v1.4 Tripo 모델이어야 함 |

**참고:** 이 노드는 Tripo v1.4 모델이 생성한 초안 모델만 허용합니다. 다른 버전의 모델을 사용하면 오류가 발생할 수 있습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 정제된 모델의 파일 경로 또는 참조(하위 호환성 전용) |
| `model task_id` | MODEL_TASK_ID | 정제된 모델 작업의 식별자 |
| `GLB` | FILE3DGLB | GLB 형식의 정제된 3D 모델 |

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
