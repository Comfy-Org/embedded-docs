# 컨트롤넷을 VAE와 함께 적용

이 노드는 Stable Diffusion 3 컨디셔닝에 ControlNet 가이던스를 적용합니다. positive 및 negative 컨디셔닝 입력과 ControlNet 모델 및 이미지를 받아 조절 가능한 강도와 타이밍 매개변수로 제어 가이던스를 적용하여 생성 과정에 영향을 줍니다.

**참고:** 이 노드는 더 이상 사용되지 않는(deprecated) 것으로 표시되었으며 향후 버전에서 제거될 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | ControlNet 가이던스를 적용할 positive 컨디셔닝입니다 | CONDITIONING | 예 | - |
| `negative` | ControlNet 가이던스를 적용할 negative 컨디셔닝입니다 | CONDITIONING | 예 | - |
| `control_net` | 가이던스에 사용할 ControlNet 모델입니다 | CONTROL_NET | 예 | - |
| `vae` | 프로세스에 사용되는 VAE 모델입니다 | VAE | 예 | - |
| `image` | ControlNet이 가이던스로 사용할 입력 이미지입니다 | IMAGE | 예 | - |
| `strength` | ControlNet 효과의 강도입니다 (기본값: 1.0) | FLOAT | 예 | 0.0 - 10.0 |
| `start_percent` | 생성 과정에서 ControlNet이 적용되기 시작하는 지점입니다 (기본값: 0.0) | FLOAT | 예 | 0.0 - 1.0 |
| `end_percent` | 생성 과정에서 ControlNet이 적용을 중단하는 지점입니다 (기본값: 1.0) | FLOAT | 예 | 0.0 - 1.0 |

**참고:** `strength`가 0으로 설정되면 노드는 ControlNet을 적용하지 않고 positive 및 negative 컨디셔닝을 변경 없이 반환합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `positive` | ControlNet 가이던스가 적용된 수정된 positive 컨디셔닝입니다 | CONDITIONING |
| `negative` | ControlNet 가이던스가 적용된 수정된 negative 컨디셔닝입니다 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/ko.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
