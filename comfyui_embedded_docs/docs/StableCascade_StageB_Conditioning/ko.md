# StableCascasde_StageB 조건 설정

StableCascade_StageB_Conditioning 노드는 기존 컨디셔닝 정보와 Stage C의 이전 잠재 표현을 결합하여 Stable Cascade Stage B 생성을 위한 컨디셔닝 데이터를 준비합니다. 각 컨디셔닝 항목에 Stage C의 잠재 샘플을 포함하도록 수정하여 생성 프로세스가 이전 정보를 활용해 더 일관된 출력을 생성할 수 있게 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `conditioning` | Stage C 이전 정보로 수정할 컨디셔닝 데이터 | CONDITIONING | 예 | - |
| `stage_c` | 컨디셔닝을 위한 이전 샘플이 포함된 Stage C의 잠재 표현 | LATENT | 예 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `CONDITIONING` | Stage C 이전 정보가 통합된 수정된 컨디셔닝 데이터 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/ko.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
