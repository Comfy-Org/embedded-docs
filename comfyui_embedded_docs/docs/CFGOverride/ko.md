# CFG 오버라이드

CFG Override 노드를 사용하면 샘플링 프로세스의 특정 범위(전체 단계의 백분율로 정의됨)에 대해 고정된 CFG(Classifier-Free Guidance) 스케일 값을 설정할 수 있습니다. 여러 CFG Override 노드가 연결된 경우, 체인에서 샘플러에 가장 가까운 노드가 겹치는 범위에 대해 우선권을 가집니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | CFG 오버라이드를 적용할 모델 | MODEL | 예 | |
| `cfg` | 오버라이드 범위 동안 사용할 고정 CFG 스케일 값 (기본값: 1.0) | FLOAT | 예 | 0.0 to 100.0 |
| `start_percent` | 샘플링 프로세스의 백분율로 표시된 오버라이드 범위의 시작 지점 (기본값: 0.0) | FLOAT | 예 | 0.0 to 1.0 |
| `end_percent` | 샘플링 프로세스의 백분율로 표시된 오버라이드 범위의 종료 지점 (기본값: 1.0) | FLOAT | 예 | 0.0 to 1.0 |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `MODEL` | CFG 오버라이드 래퍼가 적용된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/ko.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
