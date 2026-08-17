# AV Latent 연결

`LTXVConcatAVLatent` 노드는 비디오 잠재 변수와 오디오 잠재 변수를 단일 결합 잠재 변수로 병합하여 LTXV 또는 MiniMax H3와 같은 오디오-비주얼 모델에 사용합니다. 두 입력의 `samples`를 함께 묶고, 입력 중 하나에 `noise_mask`가 포함된 경우 해당 마스크도 함께 묶습니다. 비디오 잠재 변수가 이미 AV 잠재 변수인 경우, 노드는 비디오 스트림을 유지하고 제공된 오디오 잠재 변수로 오디오 스트림을 교체합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `video_latent` | 비디오 데이터의 잠재 표현입니다. | LATENT | 예 |  |
| `audio_latent` | 비디오 잠재 변수와 결합할 오디오 데이터의 잠재 표현입니다. | LATENT | 예 |  |

**오디오 길이 참고:** `video_latent`이 이미 AV 잠재 변수인 경우, `audio_latent`은 하나의 차원을 제외한 모든 차원에서 포함된 오디오 스트림과 일치해야 합니다. 노드는 해당 차원을 따라 오디오를 잘라내거나 0으로 패딩하여 기존 스트림 길이에 맞춥니다. 패딩된 끝부분은 마스킹되지 않은 상태로 남아 모델이 생성할 수 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `latent` | 비디오와 오디오 `samples`가 쌍으로 포함된 잠재 변수입니다. 입력 중 하나라도 `noise_mask`를 제공하면 출력에도 쌍을 이루는 `noise_mask`가 포함되며, 누락된 마스크는 1로 채워집니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/ko.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
