# Flux Kontext 다중 참조 잠재 방법

FluxKontextMultiReferenceLatentMethod 노드는 특정 참조 잠재 변수(reference latents) 방식을 설정하여 컨디셔닝 데이터를 수정합니다. 선택된 방식을 컨디셔닝 입력에 추가하며, 이는 후속 생성 단계에서 참조 잠재 변수가 처리되는 방식에 영향을 줍니다. 이 노드는 실험적 기능으로 표시되어 있으며 Flux 컨디셔닝 시스템의 일부입니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `conditioning` | 참조 잠재 변수 방식으로 수정할 컨디셔닝 데이터 | CONDITIONING | 예 | - |
| `reference_latents_method` | 참조 잠재 변수 처리에 사용할 방식입니다. "uxo" 또는 "uso"를 선택하면 "uxo"로 변환됩니다. 이 매개변수는 고급 매개변수로 표시되어 있습니다. | COMBO | 예 | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `conditioning` | 참조 잠재 변수 방식이 적용된 수정된 컨디셔닝 데이터 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/ko.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
