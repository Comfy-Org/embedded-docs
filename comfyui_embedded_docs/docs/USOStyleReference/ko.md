# USO 스타일 참조

USOStyleReference 노드는 참조 이미지의 스타일 정보를 Flux 모델에 적용합니다. CLIP 비전 출력에서 스타일 임베딩을 구축한 다음 모델의 복제본을 패치하여, 생성 중에 텍스트 프롬프트 컨디셔닝 앞에 스타일 임베딩이 삽입되도록 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 스타일 참조 패치를 적용할 기본 모델 | MODEL | Yes | - |
| `model_patch` | 스타일 참조 정보를 포함하는 모델 패치 | MODEL_PATCH | Yes | - |
| `clip_vision_output` | CLIP 비전 처리에서 추출한 인코딩된 시각적 특징입니다. 이 노드는 -20 및 -11 레이어의 은닉 상태를 마지막에서 두 번째 은닉 상태와 결합하여 스타일 임베딩을 구축합니다. | CLIP_VISION_OUTPUT | Yes | - |

참고: 세 입력 모두 필수입니다. 이 노드는 실험 단계로 표시되어 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 스타일 참조 패치가 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/ko.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
