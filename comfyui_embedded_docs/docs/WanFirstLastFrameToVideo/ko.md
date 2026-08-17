# WAN 비디오 생성 (시작-끝 프레임)

WanFirstLastFrameToVideo 노드는 시작 프레임과 끝 프레임을 텍스트 프롬프트와 결합하여 비디오 조건부(conditioning)를 생성합니다. 첫 번째 프레임과 마지막 프레임을 인코딩하고, 생성 과정을 안내하는 마스크를 적용하며, 사용 가능한 경우 CLIP 비전 특징을 통합하여 비디오 생성을 위한 잠재 표현을 생성합니다. 이 노드는 지정된 시작점과 끝점 사이에서 일관된 시퀀스를 생성하도록 비디오 모델을 위한 긍정 및 부정 조건부를 모두 준비합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 안내하는 긍정 텍스트 조건부 | CONDITIONING | 예 | - |
| `negative` | 비디오 생성을 안내하는 부정 텍스트 조건부 | CONDITIONING | 예 | - |
| `vae` | 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 | VAE | 예 | - |
| `width` | 출력 비디오 너비 (기본값: 832, 증가 단위: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력 비디오 높이 (기본값: 480, 증가 단위: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 비디오 시퀀스의 프레임 수 (기본값: 81, 증가 단위: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 동시에 생성할 비디오 수 (기본값: 1) | INT | 예 | 1 to 4096 |
| `clip_vision_start_image` | 시작 이미지에서 추출된 CLIP 비전 특징 | CLIP_VISION_OUTPUT | 아니요 | - |
| `clip_vision_end_image` | 끝 이미지에서 추출된 CLIP 비전 특징 | CLIP_VISION_OUTPUT | 아니요 | - |
| `start_image` | 비디오 시퀀스의 시작 프레임 이미지 | IMAGE | 아니요 | - |
| `end_image` | 비디오 시퀀스의 끝 프레임 이미지 | IMAGE | 아니요 | - |

**참고:** `start_image`와 `end_image`가 모두 제공되면 노드는 이 두 프레임 사이를 전환하는 비디오 시퀀스를 생성합니다. `start_image`는 처리 전에 첫 번째 `length` 프레임으로 잘리고, `end_image`는 마지막 `length` 프레임으로 잘립니다. 하나만 제공되면 누락된 측은 중성 회색 프레임으로 채워집니다. 마스크는 시작 및 끝 프레임이 있는 곳에서는 0으로 설정되고 그 외에는 1로 설정됩니다. `clip_vision_start_image` 및 `clip_vision_end_image` 매개변수는 선택 사항입니다. 둘 다 제공되면 해당 CLIP 비전 특징이 연결되어 긍정 및 부정 조건부 모두에 적용됩니다. 하나만 제공되면 해당 특징만 단독으로 사용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 비디오 프레임 인코딩 및 CLIP 비전 특징이 적용된 긍정 조건부 | CONDITIONING |
| `negative` | 비디오 프레임 인코딩 및 CLIP 비전 특징이 적용된 부정 조건부 | CONDITIONING |
| `latent` | 지정된 비디오 매개변수와 일치하는 차원을 가진 빈 잠재 텐서 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
