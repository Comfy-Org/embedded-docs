# LTXV Reference Audio (ID-LoRA)

LTXV Reference Audio 노드는 오디오 생성 시 ID-LoRA 화자 정체성 전송을 위해 참조 오디오 클립을 설정합니다. 클립을 컨디셔닝에 인코딩하여 생성된 오디오가 화자의 음성 특성을 따르도록 하며, 선택적으로 정체성 가이던스로 모델을 패치하여 참조 없이 추가 순방향 패스를 실행함으로써 화자 정체성 효과를 증폭합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 정체성 가이던스로 패치할 모델입니다. | MODEL | 예 | - |
| `positive` | 긍정 컨디셔닝 입력입니다. | CONDITIONING | 예 | - |
| `negative` | 부정 컨디셔닝 입력입니다. | CONDITIONING | 예 | - |
| `reference_audio` | 전송할 화자 정체성을 가진 참조 오디오 클립입니다. 약 5초 길이를 권장합니다(학습 시간 기준). 더 짧거나 긴 클립은 음성 정체성 전송 품질을 저하시킬 수 있습니다. | AUDIO | 예 | - |
| `audio_vae` | 인코딩에 사용할 LTXV 오디오 VAE입니다. | VAE | 예 | - |
| `identity_guidance_scale` | 정체성 가이던스의 강도입니다. 각 단계에서 참조 없이 추가 순방향 패스를 실행하여 화자 정체성을 증폭합니다. 비활성화하려면 0으로 설정합니다(추가 패스 없음). (기본값: 3.0) | FLOAT | 아니요 | 0.0 - 100.0 |
| `start_percent` | 정체성 가이던스가 활성화되는 sigma 범위의 시작입니다. (기본값: 0.0) | FLOAT | 아니요 | 0.0 - 1.0 |
| `end_percent` | 정체성 가이던스가 활성화되는 sigma 범위의 끝입니다. (기본값: 1.0) | FLOAT | 아니요 | 0.0 - 1.0 |

참고: 정체성 가이던스는 `start_percent`와 `end_percent`로 정의된 sigma 범위 내에서만 활성화되며, 해당 범위 밖에서는 노이즈 제거 출력이 변경되지 않습니다. 참조 오디오는 긍정 및 부정 컨디셔닝 모두에 추가됩니다. 참조 오디오의 샘플 레이트가 오디오 VAE의 샘플 레이트와 다른 경우, VAE에 맞게 오디오가 자동으로 리샘플링됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 정체성 가이던스 함수로 패치된 모델입니다. | MODEL |
| `positive` | 인코딩된 참조 오디오 데이터를 포함하는 긍정 컨디셔닝입니다. | CONDITIONING |
| `negative` | 인코딩된 참조 오디오 데이터를 포함하는 부정 컨디셔닝입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/ko.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
