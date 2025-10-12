> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/ko.md)

TrainLoraNode는 제공된 잠재 데이터와 조건화 데이터를 사용하여 확산 모델에 대한 LoRA(Low-Rank Adaptation) 모델을 생성하고 학습시킵니다. 사용자 정의 학습 매개변수, 옵티마이저 및 손실 함수를 사용하여 모델을 미세 조정할 수 있습니다. 이 노드는 LoRA가 적용된 학습된 모델, LoRA 가중치, 학습 손실 메트릭, 그리고 완료된 총 학습 단계를 출력합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | LoRA를 학습시킬 모델입니다. |
| `latents` | LATENT | 예 | - | 학습에 사용할 잠재 데이터로, 모델의 데이터셋/입력 역할을 합니다. |
| `positive` | CONDITIONING | 예 | - | 학습에 사용할 긍정 조건화 데이터입니다. |
| `batch_size` | INT | 예 | 1-10000 | 학습에 사용할 배치 크기입니다 (기본값: 1). |
| `grad_accumulation_steps` | INT | 예 | 1-1024 | 학습에 사용할 경사 누적 단계 수입니다 (기본값: 1). |
| `steps` | INT | 예 | 1-100000 | LoRA를 학습시킬 단계 수입니다 (기본값: 16). |
| `learning_rate` | FLOAT | 예 | 0.0000001-1.0 | 학습에 사용할 학습률입니다 (기본값: 0.0005). |
| `rank` | INT | 예 | 1-128 | LoRA 계층의 랭크입니다 (기본값: 8). |
| `optimizer` | COMBO | 예 | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | 학습에 사용할 옵티마이저입니다 (기본값: "AdamW"). |
| `loss_function` | COMBO | 예 | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | 학습에 사용할 손실 함수입니다 (기본값: "MSE"). |
| `seed` | INT | 예 | 0-18446744073709551615 | 학습에 사용할 시드 값입니다 (LoRA 가중치 초기화 및 노이즈 샘플링용 생성기에 사용됨) (기본값: 0). |
| `training_dtype` | COMBO | 예 | "bf16"<br>"fp32" | 학습에 사용할 데이터 타입입니다 (기본값: "bf16"). |
| `lora_dtype` | COMBO | 예 | "bf16"<br>"fp32" | LoRA에 사용할 데이터 타입입니다 (기본값: "bf16"). |
| `algorithm` | COMBO | 예 | 여러 옵션 사용 가능 | 학습에 사용할 알고리즘입니다. |
| `gradient_checkpointing` | BOOLEAN | 예 | - | 학습에 그래디언트 체크포인팅 사용 여부 (기본값: True). |
| `existing_lora` | COMBO | 예 | 여러 옵션 사용 가능 | 추가할 기존 LoRA입니다. 새 LoRA의 경우 None으로 설정합니다 (기본값: "[None]"). |

**참고:** 긍정 조건화 입력의 수는 잠재 이미지의 수와 일치해야 합니다. 여러 이미지에 대해 하나의 긍정 조건화만 제공된 경우, 모든 이미지에 대해 자동으로 반복됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_with_lora` | MODEL | 학습된 LoRA가 적용된 원본 모델입니다. |
| `lora` | LORA_MODEL | 저장하거나 다른 모델에 적용할 수 있는 학습된 LoRA 가중치입니다. |
| `loss` | LOSS_MAP | 시간에 따른 학습 손실 값을 포함하는 딕셔너리입니다. |
| `steps` | INT | 완료된 총 학습 단계 수입니다 (기존 LoRA의 이전 단계 포함). |