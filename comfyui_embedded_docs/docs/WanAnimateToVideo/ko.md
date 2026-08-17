# 완애니메이트투비디오

이 실험용 노드는 참조 이미지와 선택적 포즈, 얼굴, 배경 비디오를 결합하여 Wan 비디오 생성을 준비합니다. 후속 생성을 위한 컨디셔닝 데이터와 빈 잠재(latent) 비디오 텐서를 구성하고, 기존 비디오를 청크 단위로 확장하는 데 도움이 되는 프레임 오프셋 정보를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 생성 결과를 원하는 콘텐츠로 유도하는 긍정 컨디셔닝입니다. | CONDITIONING | 예 | - |
| `negative` | 원치 않는 콘텐츠에서 생성 결과를 멀어지게 하는 부정 컨디셔닝입니다. | CONDITIONING | 예 | - |
| `vae` | 이미지 데이터를 인코딩하고 디코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `width` | 출력 비디오의 가로 크기(픽셀)입니다. (기본값: 832, 간격: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력 비디오의 세로 크기(픽셀)입니다. (기본값: 480, 간격: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 생성할 프레임 수입니다. (기본값: 77, 간격: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 한 번에 생성할 비디오 수입니다. (기본값: 1) | INT | 예 | 1 to 4096 |
| `clip_vision_output` | 긍정 및 부정 컨디셔닝 모두에 추가 컨디셔닝으로 사용되는 선택적 CLIP 비전 모델 출력입니다. | CLIP_VISION_OUTPUT | 아니요 | - |
| `reference_image` | 생성의 시작점으로 사용되는 참조 이미지입니다. 제공되지 않으면 검은색 이미지(모두 0)가 사용됩니다. | IMAGE | 아니요 | - |
| `face_video` | 얼굴 표정 안내를 제공하는 비디오입니다. 처리될 때 512x512로 크기가 조정되고 -1.0~1.0 범위로 정규화됩니다. | IMAGE | 아니요 | - |
| `pose_video` | 포즈와 동작 안내를 제공하는 비디오입니다. `length`보다 짧으면 마지막 프레임으로 채워집니다. | IMAGE | 아니요 | - |
| `continue_motion_max_frames` | 이전 모션에서 계속할 최대 프레임 수입니다. `continue_motion`의 마지막 이 프레임 수만 사용됩니다. (기본값: 5, 간격: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `background_video` | 생성된 콘텐츠와 합성할 배경 비디오입니다. | IMAGE | 아니요 | - |
| `character_mask` | 선택적 처리를 위해 캐릭터 영역을 정의하는 마스크입니다. 마스크에 프레임이 하나만 있으면 모든 프레임에 반복됩니다. | MASK | 아니요 | - |
| `continue_motion` | 비디오 확장 시 시간적 일관성을 유지하기 위해 사용되는 이전 모션 시퀀스입니다. 마지막 `continue_motion_max_frames` 프레임만 사용됩니다. | IMAGE | 아니요 | - |
| `video_frame_offset` | 모든 입력 비디오에서 탐색할 프레임 수입니다. 더 긴 비디오를 청크 단위로 생성할 때 사용됩니다. 비디오 확장 시 이전 노드의 `video_frame_offset` 출력에 연결하세요. (기본값: 0, 간격: 1) | INT | 예 | 0 to MAX_RESOLUTION |

**매개변수 제약 사항:**

- `pose_video`가 제공되면 더 짧은 포즈 비디오는 `length`에 맞게 마지막 프레임으로 채워집니다. 소스에는 현재 비활성화된 `trim_to_pose_video` 플래그가 있으며, 이 플래그는 대신 출력을 포즈 비디오 길이에 맞춰 줄입니다.
- `face_video`는 512x512로 크기가 조정되고 -1.0~1.0 범위로 정규화됩니다.
- `continue_motion`은 마지막 `continue_motion_max_frames` 프레임으로 제한됩니다. `continue_motion`을 사용하면 `video_frame_offset`이 가져온 프레임 수만큼 줄어들지만 0보다 작아지지는 않습니다.
- 입력 비디오(`face_video`, `pose_video`, `background_video`, `character_mask`)는 `video_frame_offset`만큼 오프셋됩니다. 오프셋이 해당 길이보다 크거나 같으면 입력은 무시되지만, 항상 반복되는 단일 프레임 `character_mask`는 예외입니다.
- `clip_vision_output`이 제공되면 긍정 및 부정 컨디셔닝 모두에 적용됩니다.
- `reference_image`가 제공되지 않으면 검은색 이미지(모두 0)가 참조로 사용됩니다.
- `continue_motion`이 제공되지 않으면 픽셀 값 0.5의 회색 프레임이 모션 부분에 사용됩니다.
- `width`와 `height`는 16 단위로 설정되며, 해당하는 잠재 차원은 `width / 8` 및 `height / 8`입니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 항상 연결된 잠재 이미지와 연결된 마스크를 포함하는 수정된 긍정 컨디셔닝입니다. `clip_vision_output`, `pose_video` 또는 `face_video`가 제공되면 해당 값도 추가됩니다. | CONDITIONING |
| `negative` | 항상 연결된 잠재 이미지와 연결된 마스크를 포함하는 수정된 부정 컨디셔닝입니다. `clip_vision_output`, `pose_video` 또는 `face_video`가 제공되면 해당 값도 추가됩니다. 얼굴 비디오 픽셀은 -1.0으로 설정됩니다. | CONDITIONING |
| `latent` | 0으로 초기화된 빈 잠재 텐서이며 형태는 `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`입니다. | LATENT |
| `trim_latent` | 참조 이미지 잠재 프레임에 해당하는, 시작 부분에서 잘라낼 잠재 프레임 수입니다. | INT |
| `trim_image` | 참조 모션 프레임에 해당하는, 시작 부분에서 잘라낼 이미지 프레임 수입니다. | INT |
| `video_frame_offset` | 청크 단위 비디오 생성을 위한 업데이트된 프레임 오프셋으로, 조정된 입력 오프셋에 생성된 길이를 더한 값입니다. | INT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
