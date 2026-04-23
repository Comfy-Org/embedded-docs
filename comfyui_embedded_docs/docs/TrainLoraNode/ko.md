> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/ko.md)

# TrainLoraNode

TrainLoraNode는 제공된 잠재 표현(latents)과 컨디셔닝 데이터를 사용하여 확산 모델에 대한 LoRA(Low-Rank Adaptation) 모델을 생성하고 학습합니다. 사용자 정의 학습 매개변수, 최적화기 및 손실 함수를 사용하여 모델을 미세 조정할 수 있습니다. 이 노드는 학습된 LoRA 가중치, 손실 기록 맵 및 완료된 총 학습 단계 수를 출력합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | LoRA를 학습할 모델입니다. |
| `latents` | LATENT | 예 | - | 학습에 사용할 잠재 표현으로, 모델의 데이터셋/입력 역할을 합니다. |
| `positive` | CONDITIONING | 예 | - | 학습에 사용할 긍정 컨디셔닝입니다. |
| `batch_size` | INT | 예 | 1-10000 | 학습에 사용할 배치 크기입니다(기본값: 1). |
| `grad_accumulation_steps` | INT | 예 | 1-1024 | 학습에 사용할 그래디언트 누적 단계 수입니다(기본값: 1). |
| `steps` | INT | 예 | 1-100000 | LoRA를 학습할 단계 수입니다(기본값: 16). |
| `learning_rate` | FLOAT | 예 | 0.0000001-1.0 | 학습에 사용할 학습률입니다(기본값: 0.0005). |
| `rank` | INT | 예 | 1-128 | LoRA 레이어의 순위(rank)입니다(기본값: 8). |
| `optimizer` | COMBO | 예 | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | 학습에 사용할 최적화기입니다(기본값: "AdamW"). |
| `loss_function` | COMBO | 예 | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | 학습에 사용할 손실 함수입니다(기본값: "MSE"). |
| `seed` | INT | 예 | 0-18446744073709551615 | 학습에 사용할 시드입니다(LoRA 가중치 초기화 및 노이즈 샘플링을 위한 생성기에 사용됨)(기본값: 0). |
| `training_dtype` | COMBO | 예 | "bf16"<br>"fp32"<br>"none" | 학습에 사용할 데이터 타입입니다. 'none'은 모델의 기본 계산 데이터 타입을 유지하며 재정의하지 않습니다. fp16 모델의 경우 GradScaler가 자동으로 활성화됩니다(기본값: "bf16"). |
| `lora_dtype` | COMBO | 예 | "bf16"<br>"fp32" | LoRA에 사용할 데이터 타입입니다(기본값: "bf16"). |
| `quantized_backward` | BOOLEAN | 예 | - | training_dtype이 'none'이고 양자화된 모델에서 학습할 때, 활성화되면 역전파 시 양자화된 행렬 곱셈을 사용합니다(기본값: False). |
| `algorithm` | COMBO | 예 | 여러 옵션 사용 가능 | 학습에 사용할 알고리즘입니다. |
| `gradient_checkpointing` | BOOLEAN | 예 | - | 학습에 그래디언트 체크포인팅을 사용합니다(기본값: True). |
| `checkpoint_depth` | INT | 예 | 1-5 | 그래디언트 체크포인팅의 깊이 수준입니다(기본값: 1). |
| `offloading` | BOOLEAN | 예 | - | GPU 메모리를 절약하기 위해 학습 중 모델 가중치를 CPU로 오프로드합니다(기본값: False). |
| `existing_lora` | COMBO | 예 | 여러 옵션 사용 가능 | 추가할 기존 LoRA입니다. 새 LoRA의 경우 None으로 설정합니다(기본값: "[None]"). |
| `bucket_mode` | BOOLEAN | 예 | - | 해상도 버킷 모드를 활성화합니다. 활성화되면 ResolutionBucket 노드에서 사전 버킷된 잠재 표현을 기대합니다(기본값: False). |
| `bypass_mode` | BOOLEAN | 예 | - | 학습을 위한 바이패스 모드를 활성화합니다. 활성화되면 어댑터가 가중치 수정 대신 순방향 훅을 통해 적용됩니다. 가중치를 직접 수정할 수 없는 양자화된 모델에 유용합니다(기본값: False). |

**참고:** 긍정 컨디셔닝 입력의 수는 잠재 이미지의 수와 일치해야 합니다. 여러 이미지에 대해 하나의 긍정 컨디셔닝만 제공된 경우, 모든 이미지에 대해 자동으로 반복됩니다.

**`training_dtype` 참고:** "none"으로 설정하면 모델의 기본 계산 데이터 타입이 유지됩니다. fp16 모델의 경우 그래디언트 계산 중 언더플로를 방지하기 위해 GradScaler가 자동으로 활성화됩니다. `fp16_accumulation`도 활성화된 경우(`--fast` 플래그를 통해), 이 조합은 수치적으로 불안정하여 NaN 값을 유발할 수 있습니다.

**`quantized_backward` 참고:** 이 매개변수는 `training_dtype`이 "none"으로 설정되고 모델이 양자화된 모델인 경우에만 관련됩니다. 역전파 중 양자화된 행렬 곱셈을 활성화합니다.

**`bypass_mode` 참고:** 활성화되면 어댑터가 모델 가중치를 직접 수정하는 대신 순방향 훅을 통해 적용됩니다. 이는 가중치를 직접 수정할 수 없는 양자화된 모델에 특히 유용합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `lora` | LORA_MODEL | 저장하거나 다른 모델에 적용할 수 있는 학습된 LoRA 가중치입니다. |
| `loss_map` | LOSS_MAP | 시간에 따른 학습 손실 값을 포함하는 딕셔너리입니다. |
| `steps` | INT | 완료된 총 학습 단계 수입니다(기존 LoRA의 이전 단계 포함). |