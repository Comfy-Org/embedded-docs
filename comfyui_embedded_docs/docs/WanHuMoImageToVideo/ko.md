# WanHuMo 이미지-비디오 변환

WanHuMoImageToVideo 노드는 이미지-투-비디오 생성에 필요한 컨디셔닝 데이터와 잠재 공간을 준비합니다. 빈 잠재 비디오 텐서를 만들고, 선택적으로 VAE로 참조 이미지를 인코딩하며, 선택적으로 오디오 인코더 출력을 비디오 타이밍에 맞춘 컨디셔닝으로 변환합니다. 이 노드는 긍정 및 부정 컨디셔닝 스트림과 추가 비디오 샘플링을 위한 잠재 텐서를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 원하는 콘텐츠를 향해 비디오 생성이 진행되도록 안내하는 긍정 컨디셔닝 입력입니다. | CONDITIONING | 예 | - |
| `negative` | 원하지 않는 콘텐츠에서 벗어나도록 비디오 생성을 유도하는 부정 컨디셔닝 입력입니다. | CONDITIONING | 예 | - |
| `vae` | 참조 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `width` | 출력 비디오 프레임의 가로 크기(픽셀)입니다. 기본값은 832이며 16으로 나누어 떨어져야 합니다. | INT | 예 | 16 to MAX_RESOLUTION (step 16) |
| `height` | 출력 비디오 프레임의 세로 크기(픽셀)입니다. 기본값은 480이며 16으로 나누어 떨어져야 합니다. | INT | 예 | 16 to MAX_RESOLUTION (step 16) |
| `length` | 생성되는 비디오 시퀀스의 프레임 수입니다. 기본값은 97이며 `(length - 1)`이 4로 나누어 떨어져야 합니다. | INT | 예 | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | 동시에 생성할 비디오 시퀀스 수입니다. 기본값은 1입니다. | INT | 예 | 1 to 4096 |
| `audio_encoder_output` | 선택 사항인 오디오 인코더 출력으로, 오디오 콘텐츠를 기반으로 비디오 생성에 영향을 줍니다. | AUDIO_ENCODER_OUTPUT | 아니요 | - |
| `ref_image` | 선택 사항인 참조 이미지로, 비디오 생성 스타일과 콘텐츠를 안내하는 데 사용됩니다. | IMAGE | 아니요 | - |

**참고:** `ref_image`가 제공되면 `width` x `height` 크기로 조정되고, `vae`로 인코딩된 후 긍정 및 부정 컨디셔닝에 참조 잠재 변수로 추가됩니다. 참조 이미지가 제공되지 않으면 0 벡터 참조 잠재 변수가 사용됩니다. `audio_encoder_output`이 제공되면 해당 오디오 임베딩이 처리되어 두 컨디셔닝 스트림에 오디오 임베딩으로 추가됩니다. 그렇지 않으면 0 벡터 오디오 임베딩이 사용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 참조 잠재 변수와 오디오 임베딩 정보가 추가된 긍정 컨디셔닝입니다. | CONDITIONING |
| `negative` | 참조 잠재 변수와 오디오 임베딩 정보가 추가된 부정 컨디셔닝입니다. | CONDITIONING |
| `latent` | `batch_size`, `length`, `height`, `width`에 따라 0으로 초기화된 비디오 시퀀스를 나타내는 잠재 텐서입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
