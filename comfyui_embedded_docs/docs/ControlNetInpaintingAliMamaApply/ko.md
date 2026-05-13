> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/ko.md)

# ControlNetInpaintingAliMamaApply

ControlNetInpaintingAliMamaApply 노드는 인페인팅 작업을 위해 ControlNet 컨디셔닝을 적용하여, 포지티브 및 네거티브 컨디셔닝을 제어 이미지 및 마스크와 결합합니다. 입력 이미지와 마스크를 처리하여 생성 과정을 안내하는 수정된 컨디셔닝을 생성하므로, 이미지의 어느 영역을 인페인팅할지 정밀하게 제어할 수 있습니다. 이 노드는 생성 과정의 여러 단계에서 ControlNet의 영향을 미세 조정하기 위한 강도 조정 및 타이밍 제어 기능을 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 원하는 콘텐츠로 생성을 안내하는 포지티브 컨디셔닝 |
| `negative` | CONDITIONING | 예 | - | 원하지 않는 콘텐츠에서 생성을 멀어지게 하는 네거티브 컨디셔닝 |
| `control_net` | CONTROL_NET | 예 | - | 생성에 대한 추가 제어를 제공하는 ControlNet 모델 |
| `vae` | VAE | 예 | - | 이미지 인코딩 및 디코딩에 사용되는 VAE(변이형 오토인코더) |
| `image` | IMAGE | 예 | - | ControlNet의 제어 안내 역할을 하는 입력 이미지 |
| `mask` | MASK | 예 | - | 이미지에서 인페인팅할 영역을 정의하는 마스크 |
| `strength` | FLOAT | 예 | 0.0 ~ 10.0 | ControlNet 효과의 강도 (기본값: 1.0) |
| `start_percent` | FLOAT | 예 | 0.0 ~ 1.0 | 생성 중 ControlNet 영향이 시작되는 시점(백분율) (기본값: 0.0) |
| `end_percent` | FLOAT | 예 | 0.0 ~ 1.0 | 생성 중 ControlNet 영향이 종료되는 시점(백분율) (기본값: 1.0) |

**참고:** ControlNet에서 `concat_mask`가 활성화된 경우, 마스크가 반전되어 처리 전 이미지에 적용되며, 마스크는 ControlNet으로 전송되는 추가 연결 데이터에 포함됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 인페인팅을 위해 ControlNet이 적용된 수정된 포지티브 컨디셔닝 |
| `negative` | CONDITIONING | 인페인팅을 위해 ControlNet이 적용된 수정된 네거티브 컨디셔닝 |

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
