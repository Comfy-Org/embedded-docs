> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/ko.md)

ModelMergeCosmos14B 노드는 Cosmos 14B 모델 아키텍처에 특화된 블록 기반 접근 방식을 사용하여 두 개의 AI 모델을 병합합니다. 각 모델 블록과 임베딩 레이어에 대해 0.0에서 1.0 사이의 가중치 값을 조정하여 모델의 다양한 구성 요소를 혼합할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `모델1` | MODEL | 예 | - | 병합할 첫 번째 모델 |
| `모델2` | MODEL | 예 | - | 병합할 두 번째 모델 |
| `pos_embedder.` | FLOAT | 예 | 0.0 - 1.0 | 위치 임베더 가중치 (기본값: 1.0) |
| `extra_pos_embedder.` | FLOAT | 예 | 0.0 - 1.0 | 추가 위치 임베더 가중치 (기본값: 1.0) |
| `x_embedder.` | FLOAT | 예 | 0.0 - 1.0 | X 임베더 가중치 (기본값: 1.0) |
| `t_embedder.` | FLOAT | 예 | 0.0 - 1.0 | T 임베더 가중치 (기본값: 1.0) |
| `affline_norm.` | FLOAT | 예 | 0.0 - 1.0 | 아핀 정규화 가중치 (기본값: 1.0) |
| `blocks.block0.` | FLOAT | 예 | 0.0 - 1.0 | 블록 0 가중치 (기본값: 1.0) |
| `blocks.block1.` | FLOAT | 예 | 0.0 - 1.0 | 블록 1 가중치 (기본값: 1.0) |
| `blocks.block2.` | FLOAT | 예 | 0.0 - 1.0 | 블록 2 가중치 (기본값: 1.0) |
| `blocks.block3.` | FLOAT | 예 | 0.0 - 1.0 | 블록 3 가중치 (기본값: 1.0) |
| `blocks.block4.` | FLOAT | 예 | 0.0 - 1.0 | 블록 4 가중치 (기본값: 1.0) |
| `blocks.block5.` | FLOAT | 예 | 0.0 - 1.0 | 블록 5 가중치 (기본값: 1.0) |
| `blocks.block6.` | FLOAT | 예 | 0.0 - 1.0 | 블록 6 가중치 (기본값: 1.0) |
| `blocks.block7.` | FLOAT | 예 | 0.0 - 1.0 | 블록 7 가중치 (기본값: 1.0) |
| `blocks.block8.` | FLOAT | 예 | 0.0 - 1.0 | 블록 8 가중치 (기본값: 1.0) |
| `blocks.block9.` | FLOAT | 예 | 0.0 - 1.0 | 블록 9 가중치 (기본값: 1.0) |
| `blocks.block10.` | FLOAT | 예 | 0.0 - 1.0 | 블록 10 가중치 (기본값: 1.0) |
| `blocks.block11.` | FLOAT | 예 | 0.0 - 1.0 | 블록 11 가중치 (기본값: 1.0) |
| `blocks.block12.` | FLOAT | 예 | 0.0 - 1.0 | 블록 12 가중치 (기본값: 1.0) |
| `blocks.block13.` | FLOAT | 예 | 0.0 - 1.0 | 블록 13 가중치 (기본값: 1.0) |
| `blocks.block14.` | FLOAT | 예 | 0.0 - 1.0 | 블록 14 가중치 (기본값: 1.0) |
| `blocks.block15.` | FLOAT | 예 | 0.0 - 1.0 | 블록 15 가중치 (기본값: 1.0) |
| `blocks.block16.` | FLOAT | 예 | 0.0 - 1.0 | 블록 16 가중치 (기본값: 1.0) |
| `blocks.block17.` | FLOAT | 예 | 0.0 - 1.0 | 블록 17 가중치 (기본값: 1.0) |
| `blocks.block18.` | FLOAT | 예 | 0.0 - 1.0 | 블록 18 가중치 (기본값: 1.0) |
| `blocks.block19.` | FLOAT | 예 | 0.0 - 1.0 | 블록 19 가중치 (기본값: 1.0) |
| `blocks.block20.` | FLOAT | 예 | 0.0 - 1.0 | 블록 20 가중치 (기본값: 1.0) |
| `blocks.block21.` | FLOAT | 예 | 0.0 - 1.0 | 블록 21 가중치 (기본값: 1.0) |
| `blocks.block22.` | FLOAT | 예 | 0.0 - 1.0 | 블록 22 가중치 (기본값: 1.0) |
| `blocks.block23.` | FLOAT | 예 | 0.0 - 1.0 | 블록 23 가중치 (기본값: 1.0) |
| `blocks.block24.` | FLOAT | 예 | 0.0 - 1.0 | 블록 24 가중치 (기본값: 1.0) |
| `blocks.block25.` | FLOAT | 예 | 0.0 - 1.0 | 블록 25 가중치 (기본값: 1.0) |
| `blocks.block26.` | FLOAT | 예 | 0.0 - 1.0 | 블록 26 가중치 (기본값: 1.0) |
| `blocks.block27.` | FLOAT | 예 | 0.0 - 1.0 | 블록 27 가중치 (기본값: 1.0) |
| `blocks.block28.` | FLOAT | 예 | 0.0 - 1.0 | 블록 28 가중치 (기본값: 1.0) |
| `blocks.block29.` | FLOAT | 예 | 0.0 - 1.0 | 블록 29 가중치 (기본값: 1.0) |
| `blocks.block30.` | FLOAT | 예 | 0.0 - 1.0 | 블록 30 가중치 (기본값: 1.0) |
| `blocks.block31.` | FLOAT | 예 | 0.0 - 1.0 | 블록 31 가중치 (기본값: 1.0) |
| `blocks.block32.` | FLOAT | 예 | 0.0 - 1.0 | 블록 32 가중치 (기본값: 1.0) |
| `blocks.block33.` | FLOAT | 예 | 0.0 - 1.0 | 블록 33 가중치 (기본값: 1.0) |
| `blocks.block34.` | FLOAT | 예 | 0.0 - 1.0 | 블록 34 가중치 (기본값: 1.0) |
| `blocks.block35.` | FLOAT | 예 | 0.0 - 1.0 | 블록 35 가중치 (기본값: 1.0) |
| `final_layer.` | FLOAT | 예 | 0.0 - 1.0 | 최종 레이어 가중치 (기본값: 1.0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 두 입력 모델의 특징을 결합한 병합된 모델 |
