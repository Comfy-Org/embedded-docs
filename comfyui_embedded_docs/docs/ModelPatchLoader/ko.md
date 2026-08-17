# 모델 패치 로더

ModelPatchLoader 노드는 model_patches 폴더에서 특수 모델 패치를 로드합니다. 패치 파일의 유형을 자동으로 감지하여 적절한 모델 아키텍처를 로드한 다음, 워크플로우에서 사용할 수 있도록 ModelPatcher로 래핑합니다. 이 노드는 controlnet 블록, feature embedder 모델 및 기타 특수 아키텍처를 포함한 다양한 패치 유형을 지원합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `name` | model_patches 디렉토리에서 로드할 모델 패치의 파일 이름입니다 | STRING | 예 | model_patches 폴더의 모든 사용 가능한 모델 패치 파일 |

참고: 이 노드는 ComfyUI에서 실험 단계로 표시되어 있습니다. 패치 유형은 파일 내용에서 자동으로 감지되므로 단일 노드로 여러 종류의 패치를 처리할 수 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `MODEL_PATCH` | 워크플로우에서 사용할 수 있도록 ModelPatcher로 래핑된 로드된 모델 패치입니다 | MODEL_PATCH |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/ko.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
