# 컨트롤넷 인페인팅 AliMama 적용

이 노드는 ControlNet 조건부를 인페인팅 작업에 적용하기 위해 긍정 및 부정 조건부를 제어 이미지 및 마스크와 결합합니다. 이미지와 마스크를 처리하여 생성 과정을 안내하는 수정된 조건부를 생성하므로, 인페인팅할 영역을 정밀하게 제어할 수 있습니다. 또한 강도 및 타이밍 제어 기능을 지원하여 생성 중 ControlNet의 영향을 조정할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 원하는 콘텐츠로 생성 과정을 안내하는 긍정 조건부입니다. | CONDITIONING | 예 | - |
| `negative` | 원치 않는 콘텐츠에서 생성 과정을 멀어지게 하는 부정 조건부입니다. | CONDITIONING | 예 | - |
| `control_net` | 생성에 대한 추가 제어를 제공하는 ControlNet 모델입니다. | CONTROL_NET | 예 | - |
| `vae` | 이미지 인코딩 및 디코딩에 사용되는 VAE입니다. | VAE | 예 | - |
| `image` | ControlNet의 제어 안내로 사용되는 입력 이미지입니다. | IMAGE | 예 | - |
| `mask` | 이미지에서 인페인팅할 영역을 정의하는 마스크입니다. | MASK | 예 | - |
| `strength` | ControlNet 효과의 강도입니다(기본값: 1.0). | FLOAT | 예 | 0.0 ~ 10.0 |
| `start_percent` | 고급 옵션. ControlNet 영향이 시작되는 생성 과정의 비율입니다(기본값: 0.0). | FLOAT | 예 | 0.0 ~ 1.0 |
| `end_percent` | 고급 옵션. ControlNet 영향이 중지되는 생성 과정의 비율입니다(기본값: 1.0). | FLOAT | 예 | 0.0 ~ 1.0 |

**참고:** 선택한 ControlNet에서 `concat_mask`가 활성화된 경우 마스크 값이 반전(1 - 마스크)되고, 반전된 마스크의 크기 조정 버전이 이미지에 적용되며, 반전된 마스크는 ControlNet에 전달되는 추가 연결(concat) 데이터에 포함됩니다. `concat_mask`가 비활성화된 경우 `mask` 입력은 사용되지 않습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 인페인팅을 위해 ControlNet이 적용된 수정된 긍정 조건부입니다. | CONDITIONING |
| `negative` | 인페인팅을 위해 ControlNet이 적용된 수정된 부정 조건부입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/ko.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
