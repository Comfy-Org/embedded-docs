> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/ko.md)

WanFirstLastFrameToVideo 노드는 시작 프레임과 종료 프레임을 텍스트 프롬프트와 결합하여 비디오 컨디셔닝을 생성합니다. 첫 번째 프레임과 마지막 프레임을 인코딩하고, 생성 과정을 안내하는 마스크를 적용하며, 사용 가능한 경우 CLIP 비전 특징을 통합하여 비디오 생성을 위한 잠재 표현을 생성합니다. 이 노드는 지정된 시작점과 종료점 사이에서 일관된 시퀀스를 생성하기 위해 비디오 모델에 대한 긍정 및 부정 컨디셔닝을 모두 준비합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 비디오 생성을 안내하는 긍정 텍스트 컨디셔닝 |
| `negative` | CONDITIONING | 예 | - | 비디오 생성을 안내하는 부정 텍스트 컨디셔닝 |
| `vae` | VAE | 예 | - | 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 |
| `width` | INT | 예 | 16 ~ MAX_RESOLUTION | 출력 비디오 너비 (기본값: 832, 단계: 16) |
| `height` | INT | 예 | 16 ~ MAX_RESOLUTION | 출력 비디오 높이 (기본값: 480, 단계: 16) |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION | 비디오 시퀀스의 프레임 수 (기본값: 81, 단계: 4) |
| `batch_size` | INT | 예 | 1 ~ 4096 | 동시에 생성할 비디오 수 (기본값: 1) |
| `clip_vision_start_image` | CLIP_VISION_OUTPUT | 아니요 | - | 시작 이미지에서 추출된 CLIP 비전 특징 |
| `clip_vision_end_image` | CLIP_VISION_OUTPUT | 아니요 | - | 종료 이미지에서 추출된 CLIP 비전 특징 |
| `start_image` | IMAGE | 아니요 | - | 비디오 시퀀스의 시작 프레임 이미지 |
| `end_image` | IMAGE | 아니요 | - | 비디오 시퀀스의 종료 프레임 이미지 |

**참고:** `start_image`와 `end_image`가 모두 제공되면 노드는 이 두 프레임 사이를 전환하는 비디오 시퀀스를 생성합니다. `clip_vision_start_image` 및 `clip_vision_end_image` 매개변수는 선택 사항이지만, 제공되는 경우 해당 CLIP 비전 특징이 연결되어 긍정 및 부정 컨디셔닝 모두에 적용됩니다. `start_image`는 처리 전에 첫 번째 `length` 프레임으로 잘리고, `end_image`는 마지막 `length` 프레임으로 잘립니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 비디오 프레임 인코딩 및 CLIP 비전 특징이 적용된 긍정 컨디셔닝 |
| `negative` | CONDITIONING | 비디오 프레임 인코딩 및 CLIP 비전 특징이 적용된 부정 컨디셔닝 |
| `latent` | LATENT | 지정된 비디오 매개변수와 일치하는 차원의 빈 잠재 텐서 |

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
