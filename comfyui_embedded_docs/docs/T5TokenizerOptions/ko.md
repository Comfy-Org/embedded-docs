# T5 토큰생성기 옵션

T5TokenizerOptions 노드는 다양한 T5 모델 유형에 대한 토크나이저 설정을 구성할 수 있게 해 줍니다. 이 노드는 t5xxl, pile_t5xl, t5base, mt5xl 및 umt5xxl을 포함한 여러 T5 모델 변형에 대해 최소 패딩 및 최소 길이 매개변수를 설정합니다. CLIP 입력을 받아 지정된 토크나이저 옵션이 적용된 수정된 CLIP을 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip` | 토크나이저 옵션을 구성할 CLIP 모델 | CLIP | 예 | - |
| `min_padding` | 모든 T5 모델 유형에 설정할 최소 패딩 값 (기본값: 0) | INT | 아니요 | 0 to 10000 |
| `min_length` | 모든 T5 모델 유형에 설정할 최소 길이 값 (기본값: 0) | INT | 아니요 | 0 to 10000 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 모든 T5 변형에 업데이트된 토크나이저 옵션이 적용된 수정된 CLIP 모델 | CLIP |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/ko.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
