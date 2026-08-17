# LTXV 오디오 VAE 로더

LTXV Audio VAE Loader 노드는 체크포인트 파일에서 사전 훈련된 Audio Variational Autoencoder(VAE) 모델을 로드합니다. 지정된 체크포인트를 읽고 해당 가중치와 메타데이터를 로드한 다음, ComfyUI 내에서 오디오 생성 또는 처리 워크플로우에 사용할 수 있도록 모델을 준비합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `ckpt_name` | 로드할 오디오 VAE 체크포인트입니다. ComfyUI `checkpoints` 디렉토리에서 찾은 모든 파일로 채워지는 드롭다운 목록입니다. | COMBO | 예 | `checkpoints` 폴더의 모든 파일(동적으로 채워짐).<br>*예: `"audio_vae.safetensors"`* |

참고: 선택한 체크포인트 파일을 찾을 수 없거나 유효한 오디오 VAE가 포함되지 않은 경우, 노드에서 오류가 발생합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `Audio VAE` | 로드된 Audio Variational Autoencoder 모델로, 다른 오디오 처리 노드에 연결할 준비가 된 상태입니다. | VAE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/ko.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
