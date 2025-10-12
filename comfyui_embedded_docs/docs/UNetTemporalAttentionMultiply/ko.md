> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/ko.md)

UNetTemporalAttentionMultiply 노드는 시간적 UNet 모델에서 다양한 유형의 어텐션 메커니즘에 곱셈 계수를 적용합니다. 이 노드는 자기 어텐션(self-attention)과 교차 어텐션(cross-attention) 레이어의 가중치를 조정하고, 구조적 요소와 시간적 요소를 구분하여 모델을 수정합니다. 이를 통해 각 어텐션 유형이 모델 출력에 미치는 영향력을 미세하게 조정할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 어텐션 승수로 수정할 입력 모델 |
| `self_structural` | FLOAT | 아니오 | 0.0 - 10.0 | 자기 어텐션 구조적 구성 요소에 대한 승수 (기본값: 1.0) |
| `self_temporal` | FLOAT | 아니오 | 0.0 - 10.0 | 자기 어텐션 시간적 구성 요소에 대한 승수 (기본값: 1.0) |
| `cross_structural` | FLOAT | 아니오 | 0.0 - 10.0 | 교차 어텐션 구조적 구성 요소에 대한 승수 (기본값: 1.0) |
| `cross_temporal` | FLOAT | 아니오 | 0.0 - 10.0 | 교차 어텐션 시간적 구성 요소에 대한 승수 (기본값: 1.0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 조정된 어텐션 가중치가 적용된 수정된 모델 |