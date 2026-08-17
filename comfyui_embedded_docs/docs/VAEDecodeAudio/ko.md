# 오디오 VAE 디코드

VAEDecodeAudio 노드는 Variational Autoencoder를 사용하여 잠재 표현을 오디오 파형으로 다시 변환합니다. 인코딩된 오디오 샘플을 가져와 VAE를 통해 처리하여 원본 오디오를 재구성하며, 일관된 출력 레벨을 보장하기 위해 정규화를 적용합니다. 결과 오디오는 표준 샘플 레이트인 44100Hz로 반환되며, 입력 샘플에 샘플 레이트가 포함된 경우 해당 샘플 레이트로 반환됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `samples` | 잠재 공간에 있는 인코딩된 오디오 샘플로, 오디오 파형으로 디코딩됩니다. | LATENT | 예 | - |
| `vae` | 잠재 샘플을 오디오로 디코딩하는 데 사용되는 Variational Autoencoder 모델입니다. | VAE | 예 | - |

참고: `samples`에 중첩된 잠재 데이터가 포함된 경우 마지막 요소만 디코딩에 사용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `AUDIO` | 정규화된 볼륨과 샘플 레이트(기본값: 44100Hz, 또는 입력 `samples`에 포함된 샘플 레이트가 있는 경우 해당 값)를 가진 디코딩된 오디오 파형입니다. | AUDIO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/ko.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
