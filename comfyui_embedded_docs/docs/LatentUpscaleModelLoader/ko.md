# Latent 업스케일 모델 불러오기

LatentUpscaleModelLoader 노드는 잠재 표현 업스케일링을 위해 설계된 전용 모델을 로드합니다. 시스템의 지정된 폴더에서 모델 파일을 읽고 해당 유형(720p, 1080p 또는 기타)을 자동으로 감지하여 올바른 내부 모델 아키텍처를 생성하고 구성합니다. 로드된 모델은 잠재 공간 초해상도 작업을 위해 다른 노드에서 사용할 준비가 됩니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model_name` | 로드할 잠재 업스케일 모델 파일의 이름입니다. 사용 가능한 옵션은 ComfyUI의 `latent_upscale_models` 디렉터리에 있는 파일에서 동적으로 채워집니다. | COMBO | 예 | `latent_upscale_models` 폴더의 모든 파일 |

참고: 노드는 파일 내용에서 모델 아키텍처를 자동으로 감지합니다. 720p HunyuanVideo 초해상도 레이어를 포함하는 모델은 720p 모델로, 1080p 스타일 업샘플링 레이어를 가진 모델은 1080p 모델로, 다른 레이어 구조를 가진 모델은 LatentUpsampler 모델로 로드됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `model` | 로드된 잠재 업스케일 모델로, 구성이 완료되어 사용할 준비가 된 상태입니다. | LATENT_UPSCALE_MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/ko.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
