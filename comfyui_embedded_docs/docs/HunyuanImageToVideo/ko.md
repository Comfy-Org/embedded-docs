# HunyuanImageToVideo

HunyuanImageToVideo 노드는 Hunyuan 비디오 모델을 사용하여 이미지를 비디오 잠재 표현으로 변환합니다. 이 노드는 컨디셔닝 입력과 선택적 시작 이미지를 받아 비디오 생성 모델에서 추가 처리할 수 있는 비디오 잠재 표현을 생성합니다. 이 노드는 시작 이미지가 비디오 생성 과정에 영향을 미치는 방식을 제어하는 다양한 가이던스 유형을 지원합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 안내하기 위한 긍정적 컨디셔닝 입력 | CONDITIONING | 예 | - |
| `vae` | 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 | VAE | 예 | - |
| `width` | 출력 비디오의 가로 크기(픽셀) (기본값: 848, 단계: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력 비디오의 세로 크기(픽셀) (기본값: 480, 단계: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 출력 비디오의 프레임 수 (기본값: 53, 단계: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 동시에 생성할 비디오 수 (기본값: 1) | INT | 예 | 1 to 4096 |
| `guidance_type` | 비디오 생성에 시작 이미지를 통합하는 방법 (기본값: "v1 (concat)") | COMBO | 예 | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | 비디오 생성을 초기화하는 선택적 시작 이미지 | IMAGE | 아니요 | - |

**참고:** `start_image`가 제공되면 노드는 선택된 `guidance_type`에 따라 다른 가이던스 방법을 사용합니다:

- "v1 (concat)": 이미지 잠재 표현과 비디오 잠재 표현을 연결(concat)하고 마스크를 적용하여 이미지를 비디오에 혼합합니다.
- "v2 (replace)": 초기 비디오 프레임을 이미지 잠재 표현으로 대체하고 노이즈 마스크를 적용합니다.
- "custom": 이미지를 가이던스를 위한 참조 잠재 표현으로 사용합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `positive` | `start_image`가 제공될 때 이미지 가이던스가 적용된 수정된 긍정적 컨디셔닝 | CONDITIONING |
| `latent` | 비디오 생성 모델에서 추가 처리를 위한 준비가 된 비디오 잠재 표현 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
