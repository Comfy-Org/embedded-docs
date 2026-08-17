# LTXV 빈 latent 오디오

LTXV Empty Latent Audio 노드는 빈(0으로 채워진) 잠재 오디오 텐서 배치를 생성합니다. 제공된 Audio VAE 모델의 구성을 사용하여 채널 수 및 주파수 빈과 같은 잠재 공간의 올바른 차원을 결정합니다. 오디오 잠재 변수의 수는 Audio VAE 모델을 사용하여 프레임 수와 프레임 속도로부터 계산됩니다. 이 빈 잠재 변수는 ComfyUI 내에서 오디오 생성 또는 조작 워크플로우의 시작점 역할을 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `frames_number` | 프레임 수입니다. 기본값: 97. | INT | 예 | 1 to 1000 |
| `frame_rate` | 초당 프레임 수입니다. 부동 소수점 또는 정수 값을 허용합니다. 기본값: 25.0. | FLOAT (or INT) | 예 | 1.0 to 1000.0 |
| `batch_size` | 배치 내 잠재 오디오 샘플 수입니다. 기본값: 1. | INT | 예 | 1 to 4096 |
| `audio_vae` | 구성을 가져올 Audio VAE 모델입니다. | VAE | 예 | N/A |

**참고:** `audio_vae` 입력은 필수입니다. 이 입력이 제공되지 않으면 노드에서 오류가 발생합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `Latent` | 입력 Audio VAE에 맞게 구성된 구조 (batch_size, z_channels, num_audio_latents, audio_freq)의 빈 잠재 오디오 텐서입니다. 출력에는 "audio"로 설정된 `type` 필드도 포함됩니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/ko.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
