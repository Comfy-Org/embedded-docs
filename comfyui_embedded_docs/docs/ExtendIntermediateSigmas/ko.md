# 시그마 배열 중간 구간 확장

The ExtendIntermediateSigmas 노드는 기존의 sigma 값 시퀀스를 가져와 그 사이에 추가 중간 sigma 값을 삽입합니다. 이 노드를 사용하면 추가할 단계 수, 보간을 위한 간격 방법, 그리고 sigma 시퀀스 내에서 확장이 발생할 위치를 제어하는 선택적 시작 및 종료 sigma 경계를 지정할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `sigmas` | 중간 값으로 확장할 입력 sigma 시퀀스 | SIGMAS | 예 | - |
| `steps` | 기존 sigma 사이에 삽입할 중간 단계 수입니다. N 단계를 지정하면 각 적격 쌍 사이에 N-1개의 중간 sigma 값이 삽입됩니다 (기본값: 2) | INT | 예 | 1 to 100 |
| `start_at_sigma` | 확장을 위한 상한 sigma 경계입니다. 이 값보다 작은 sigma만 확장합니다 (기본값: -1.0, 이는 무한대를 의미합니다) | FLOAT | 예 | -1.0 to 20000.0 |
| `end_at_sigma` | 확장을 위한 하한 sigma 경계입니다. 이 값보다 큰 sigma만 확장합니다 (기본값: 12.0) | FLOAT | 예 | 0.0 to 20000.0 |
| `spacing` | 중간 sigma 값의 간격을 결정하는 보간 방법입니다. "linear"는 값을 균등하게 분포시키고, "cosine"과 "sine"은 곡선형 간격을 적용합니다 (기본값: "linear") | COMBO | 예 | `"linear"`<br>`"cosine"`<br>`"sine"` |

**참고:** 이 노드는 현재 sigma가 `start_at_sigma` 이하이고 `end_at_sigma` 이상인 기존 sigma 쌍 사이에만 중간 sigma를 삽입합니다. `start_at_sigma`가 -1.0으로 설정된 경우 무한대로 처리되므로 `end_at_sigma` 하한 경계만 적용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sigmas` | 추가 중간 값이 삽입된 확장된 sigma 시퀀스 | SIGMAS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/ko.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
