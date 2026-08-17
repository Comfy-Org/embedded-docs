# StableCascade_StageC VAE 인코딩

StableCascade_StageC_VAEEncode 노드는 입력 이미지를 VAE 인코더를 통해 처리하여 Stable Cascade 모델용 잠재 표현을 생성합니다. 먼저 압축 계수와 VAE의 다운스케일 비율에 따라 이미지 크기를 조정한 다음, 크기가 조정된 이미지를 인코딩합니다. 이 노드는 두 개의 잠재 텐서를 출력합니다. 하나는 스테이지 C용(실제 인코딩 결과)이고, 다른 하나는 스테이지 B용(0으로 채워진 플레이스홀더)입니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `image` | 잠재 공간으로 인코딩될 입력 이미지 | IMAGE | 예 | - |
| `vae` | 이미지 인코딩에 사용되는 VAE 모델 | VAE | 예 | - |
| `compression` | 인코딩 전에 이미지에 적용되는 압축 계수입니다. 이미지 크기는 이 값으로 나눈 다음 VAE의 다운스케일 비율과 곱해집니다. (기본값: 42) | INT | 아니요 | 4-128 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `stage_c` | Stable Cascade 모델의 스테이지 C에 대한 인코딩된 잠재 표현 | LATENT |
| `stage_b` | 스테이지 B에 대한 플레이스홀더 잠재 표현입니다. 현재 입력 이미지 크기로 계산된 차원을 가진 0으로 채워진 텐서를 반환합니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/ko.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
