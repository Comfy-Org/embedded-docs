# ModelMergeQwenImage

ModelMergeQwenImage 노드는 조정 가능한 가중치를 사용하여 두 AI 모델의 구성 요소를 결합함으로써 모델을 병합합니다. 이를 통해 트랜스포머 블록, 위치 임베딩 및 텍스트 처리 구성 요소를 포함한 Qwen 이미지 모델의 특정 부분을 혼합할 수 있습니다. 병합 결과의 각 부분에 대해 각 모델이 얼마나 많은 영향을 미칠지 제어할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model1` | 병합할 첫 번째 모델 (기본값: 없음) | MODEL | 예 | - |
| `model2` | 병합할 두 번째 모델 (기본값: 없음) | MODEL | 예 | - |
| `pos_embeds.` | 위치 임베딩 혼합 가중치 (기본값: 1.0) | FLOAT | 예 | 0.0 ~ 1.0 |
| `img_in.` | 이미지 입력 처리 혼합 가중치 (기본값: 1.0) | FLOAT | 예 | 0.0 ~ 1.0 |
| `txt_norm.` | 텍스트 정규화 혼합 가중치 (기본값: 1.0) | FLOAT | 예 | 0.0 ~ 1.0 |
| `txt_in.` | 텍스트 입력 처리 혼합 가중치 (기본값: 1.0) | FLOAT | 예 | 0.0 ~ 1.0 |
| `time_text_embed.` | 시간 및 텍스트 임베딩 혼합 가중치 (기본값: 1.0) | FLOAT | 예 | 0.0 ~ 1.0 |
| `transformer_blocks.0.` to `transformer_blocks.59.` | 각 트랜스포머 블록 혼합 가중치 (기본값: 1.0) | FLOAT | 예 | 0.0 ~ 1.0 |
| `proj_out.` | 출력 프로젝션 혼합 가중치 (기본값: 1.0) | FLOAT | 예 | 0.0 ~ 1.0 |

참고: 트랜스포머 블록 가중치 입력은 총 60개이며(`transformer_blocks.0.`부터 `transformer_blocks.59.`까지), 모델의 각 트랜스포머 블록에 하나씩 해당합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 지정된 가중치로 두 입력 모델의 구성 요소를 결합한 병합 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/ko.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
