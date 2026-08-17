# 모델 저장

ModelSave 노드는 학습되거나 수정된 모델을 컴퓨터 저장소에 저장합니다. 이 노드는 모델을 입력으로 받아 지정한 파일 이름 접두사를 사용하여 출력 폴더에 safetensors 체크포인트 파일로 작성합니다. 사용 가능한 경우 워크플로 프롬프트와 메타데이터 정보가 저장된 파일에 포함됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 디스크에 저장할 모델입니다 | MODEL | 예 | - |
| `filename_prefix` | 저장된 모델 파일의 파일 이름 및 경로 접두사(기본값: "diffusion_models/ComfyUI"). 저장 시 이름에 카운터가 추가됩니다(예: `ComfyUI_00000_.safetensors`). | STRING | 예 | - |
| `prompt` | 워크플로 프롬프트 정보(자동으로 제공됨) | PROMPT | 아니요 | - |
| `extra_pnginfo` | 추가 워크플로 메타데이터(자동으로 제공됨) | EXTRA_PNGINFO | 아니요 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| *None* | 이 노드는 출력 값을 반환하지 않습니다 | - |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/ko.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
