# YuE2 ABC 생성

이 노드는 YuE2 텍스트 및 가사 모델을 사용하여 스타일 설명과 가사를 기반으로 곡의 ABC 표기법을 생성합니다. 생성된 `abc` 출력은 YuE2 Generate Music 노드에 연결하여 오디오를 생성할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 스타일과 가사를 토큰화하고 ABC 표기법을 생성하는 데 사용되는 YuE2 모델입니다. | CLIP | 예 | - |
| `style` | 곡의 음악적 스타일을 설명하는 텍스트입니다. | STRING | 예 | - |
| `lyrics` | 곡의 가사를 포함하는 텍스트입니다. | STRING | 예 | - |
| `시드` | 생성에 사용되는 랜덤 시드입니다. 값을 변경하면 다른 결과가 생성됩니다. 기본값: 0. | INT | 예 | 0  ~  18446744073709551615 |
| `모드` | full: 멜로디와 코드를 생성합니다. melody: 멜로디만 생성하며, 커버에 권장됩니다. | COMBO | 예 | "full"<br>"melody" |
| `max_abc_tokens` | ABC 표기법에 대해 생성되는 최대 토큰 수입니다. 기본값: 8192. | INT | 예 | 1  ~  20000 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `abc` | 생성된 곡의 ABC 표기법이며, YuE2 Generate Music 노드에 연결할 수 있습니다. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/ko.md)

---
**Source fingerprint (SHA-256):** `3e06f980a53e90b750f4190a95199e0e5ed1bd8c54d4dbf8485602ff1af00102`
