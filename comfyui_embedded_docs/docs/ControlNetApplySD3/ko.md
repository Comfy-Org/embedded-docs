> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/ko.md)

이 노드는 ControlNet 안내(guidance)를 Stable Diffusion 3 컨디셔닝에 적용합니다. 긍정 및 부정 컨디셔닝 입력과 함께 ControlNet 모델 및 이미지를 입력받아, 조정 가능한 강도 및 타이밍 매개변수로 제어 안내를 적용하여 생성 과정에 영향을 줍니다.

**참고:** 이 노드는 더 이상 사용되지 않음(deprecated)으로 표시되었으며, 향후 버전에서 제거될 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | ControlNet 안내를 적용할 긍정 컨디셔닝 |
| `negative` | CONDITIONING | 예 | - | ControlNet 안내를 적용할 부정 컨디셔닝 |
| `control_net` | CONTROL_NET | 예 | - | 안내에 사용할 ControlNet 모델 |
| `vae` | VAE | 예 | - | 프로세스에 사용되는 VAE 모델 |
| `image` | IMAGE | 예 | - | ControlNet이 안내로 사용할 입력 이미지 |
| `strength` | FLOAT | 예 | 0.0 - 10.0 | ControlNet 효과의 강도 (기본값: 1.0) |
| `start_percent` | FLOAT | 예 | 0.0 - 1.0 | ControlNet이 적용되기 시작하는 생성 과정의 시작 지점 (기본값: 0.0) |
| `end_percent` | FLOAT | 예 | 0.0 - 1.0 | ControlNet 적용이 중단되는 생성 과정의 종료 지점 (기본값: 1.0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | ControlNet 안내가 적용된 수정된 긍정 컨디셔닝 |
| `negative` | CONDITIONING | ControlNet 안내가 적용된 수정된 부정 컨디셔닝 |

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
