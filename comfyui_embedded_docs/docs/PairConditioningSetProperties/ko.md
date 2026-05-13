> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/ko.md)

**PairConditioningSetProperties** 노드는 긍정 및 부정 컨디셔닝 쌍의 속성을 동시에 수정할 수 있도록 합니다. 두 컨디셔닝 입력에 강도 조정, 컨디셔닝 영역 설정, 선택적 마스킹 또는 타이밍 제어를 적용하여 수정된 긍정 및 부정 컨디셔닝 데이터를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive_NEW` | CONDITIONING | 예 | - | 수정할 긍정 컨디셔닝 입력 |
| `negative_NEW` | CONDITIONING | 예 | - | 수정할 부정 컨디셔닝 입력 |
| `strength` | FLOAT | 예 | 0.0 ~ 10.0 | 컨디셔닝에 적용되는 강도 승수 (기본값: 1.0) |
| `set_cond_area` | STRING | 예 | "default"<br>"mask bounds" | 컨디셔닝 영역 계산 방식을 결정합니다 (기본값: "default") |
| `mask` | MASK | 아니요 | - | 컨디셔닝 영역을 제한하는 선택적 마스크 |
| `hooks` | HOOKS | 아니요 | - | 고급 컨디셔닝 수정을 위한 선택적 후크 그룹 |
| `timesteps` | TIMESTEPS_RANGE | 아니요 | - | 컨디셔닝 적용 시점을 제한하는 선택적 타임스텝 범위 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 속성이 적용된 수정된 긍정 컨디셔닝 |
| `negative` | CONDITIONING | 속성이 적용된 수정된 부정 컨디셔닝 |

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
