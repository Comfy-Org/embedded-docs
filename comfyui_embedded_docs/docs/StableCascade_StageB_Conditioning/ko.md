> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/ko.md)

StableCascade_StageB_Conditioning 노드는 Stage C의 사전 잠재 표현과 기존 조건 정보를 결합하여 Stable Cascade Stage B 생성을 위한 조건 데이터를 준비합니다. 이 노드는 Stage C의 잠재 샘플을 포함하도록 조건 데이터를 수정하여, 보다 일관된 출력을 위해 사전 정보를 활용할 수 있도록 생성 프로세스를 가능하게 합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 예 | - | Stage C 사전 정보로 수정될 조건 데이터 |
| `stage_c` | LATENT | 예 | - | 조건 설정을 위한 사전 샘플을 포함하는 Stage C의 잠재 표현 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Stage C 사전 정보가 통합된 수정된 조건 데이터 |