# 잠재 데이터 연산 (톤맵 레인하르트)

LatentOperationTonemapReinhard는 잠재 벡터에 Reinhard 톤매핑을 적용합니다. 이 기법은 잠재 벡터를 정규화하고, 크기의 평균과 표준 편차를 기반으로 하는 통계적 접근 방식을 통해 크기를 조정합니다. 강도는 `multiplier` 매개변수로 제어됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `multiplier` | 톤매핑 효과의 강도를 제어합니다 (기본값: 1.0) | FLOAT | 예 | 0.0 to 100.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `operation` | 잠재 벡터에 적용할 수 있는 톤매핑 연산을 반환합니다 | LATENT_OPERATION |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/ko.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
