> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/ko.md)

FluxKontextMultiReferenceLatentMethod 노드는 특정 참조 잠재 변수 방법을 설정하여 조건부 데이터를 수정합니다. 이 노드는 선택된 방법을 조건부 입력에 추가하여, 이후 생성 단계에서 참조 잠재 변수가 처리되는 방식에 영향을 줍니다. 이 노드는 실험적으로 표시되며 Flux 조건부 시스템의 일부입니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 예 | - | 참조 잠재 변수 방법으로 수정될 조건부 데이터 |
| `reference_latents_method` | STRING | 예 | `"offset"`<br>`"index"`<br>`"uxo/uno"` | 참조 잠재 변수 처리에 사용할 방법. "uxo" 또는 "uso"가 선택되면 "uxo"로 변환됩니다 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 참조 잠재 변수 방법이 적용된 수정된 조건부 데이터 |