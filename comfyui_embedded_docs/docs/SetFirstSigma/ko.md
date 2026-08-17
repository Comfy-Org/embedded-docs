# SetFirstSigma

SetFirstSigma 노드는 시그마 값 시퀀스에서 첫 번째 시그마 값을 사용자 지정 값으로 대체하여 시퀀스를 수정합니다. 기존 시그마 시퀀스와 새 시그마 값을 입력으로 받아, 첫 번째 요소만 변경되고 나머지 시그마 값은 모두 유지된 새 시그마 시퀀스를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `sigmas` | 수정할 시그마 값의 입력 시퀀스 | SIGMAS | 예 | - |
| `sigma` | 시퀀스의 첫 번째 요소로 설정할 새 시그마 값 (기본값: 136.0) | FLOAT | 예 | 0.0 ~ 20000.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sigmas` | 첫 번째 요소가 사용자 지정 시그마 값으로 대체된 수정된 시그마 시퀀스 | SIGMAS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/ko.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
