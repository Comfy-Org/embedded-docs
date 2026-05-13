> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/ko.md)

# ConditioningStableAudio 노드

ConditioningStableAudio 노드는 오디오 생성을 위해 긍정 및 부정 조건 입력에 타이밍 정보를 추가합니다. 이 노드는 시작 시간과 전체 지속 시간 매개변수를 설정하여 오디오 콘텐츠가 생성되어야 하는 시점과 지속 시간을 제어합니다. 오디오 특화 타이밍 메타데이터를 추가하여 기존 조건 데이터를 수정합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 오디오 타이밍 정보로 수정될 긍정 조건 입력 |
| `negative` | CONDITIONING | 예 | - | 오디오 타이밍 정보로 수정될 부정 조건 입력 |
| `seconds_start` | FLOAT | 예 | 0.0 ~ 1000.0 | 오디오 생성을 위한 시작 시간(초) (기본값: 0.0) |
| `seconds_total` | FLOAT | 예 | 0.0 ~ 1000.0 | 오디오 생성을 위한 전체 지속 시간(초) (기본값: 47.0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 오디오 타이밍 정보가 적용된 수정된 긍정 조건 |
| `negative` | CONDITIONING | 오디오 타이밍 정보가 적용된 수정된 부정 조건 |

---
**Source fingerprint (SHA-256):** `ad4fdb2ac536e4f9cc23c044a7a63333e3f3530cc782937eaedc1565cc7c5d0e`
