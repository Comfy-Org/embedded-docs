> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/ko.md)

WanAnimateToVideo 노드는 포즈 참조, 얼굴 표정, 배경 요소 등 여러 조건 입력을 결합하여 비디오 콘텐츠를 생성합니다. 다양한 비디오 입력을 처리하여 일관된 애니메이션 시퀀스를 생성하면서 프레임 간의 시간적 일관성을 유지합니다. 이 노드는 잠재 공간 연산을 처리하며 기존 비디오의 모션 패턴을 이어서 비디오를 확장할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 원하는 콘텐츠 생성을 유도하기 위한 긍정적 조건 |
| `negative` | CONDITIONING | 예 | - | 원하지 않는 콘텐츠에서 생성 방향을 전환하기 위한 부정적 조건 |
| `vae` | VAE | 예 | - | 이미지 데이터 인코딩 및 디코딩에 사용되는 VAE 모델 |
| `width` | INT | 아니오 | 16 to MAX_RESOLUTION | 출력 비디오 너비 (픽셀) (기본값: 832, 단계: 16) |
| `height` | INT | 아니오 | 16 to MAX_RESOLUTION | 출력 비디오 높이 (픽셀) (기본값: 480, 단계: 16) |
| `length` | INT | 아니오 | 1 to MAX_RESOLUTION | 생성할 프레임 수 (기본값: 77, 단계: 4) |
| `batch_size` | INT | 아니오 | 1 to 4096 | 동시에 생성할 비디오 수 (기본값: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 아니오 | - | 추가 조건을 위한 선택적 CLIP 비전 모델 출력 |
| `reference_image` | IMAGE | 아니오 | - | 생성을 위한 시작점으로 사용되는 참조 이미지 |
| `face_video` | IMAGE | 아니오 | - | 얼굴 표정 안내를 제공하는 비디오 입력 |
| `pose_video` | IMAGE | 아니오 | - | 포즈 및 모션 안내를 제공하는 비디오 입력 |
| `continue_motion_max_frames` | INT | 아니오 | 1 to MAX_RESOLUTION | 이전 모션에서 이어갈 최대 프레임 수 (기본값: 5, 단계: 4) |
| `background_video` | IMAGE | 아니오 | - | 생성된 콘텐츠와 합성할 배경 비디오 |
| `character_mask` | MASK | 아니오 | - | 선택적 처리를 위한 캐릭터 영역을 정의하는 마스크 |
| `continue_motion` | IMAGE | 아니오 | - | 시간적 일관성을 위해 이어갈 이전 모션 시퀀스 |
| `video_frame_offset` | INT | 아니오 | 0 to MAX_RESOLUTION | 모든 입력 비디오에서 탐색할 프레임 수. 청크 방식으로 더 긴 비디오를 생성하는 데 사용됩니다. 비디오를 확장하기 위해 이전 노드의 video_frame_offset 출력에 연결하세요. (기본값: 0, 단계: 1) |

**매개변수 제약 조건:**

- `pose_video`가 제공되고 `trim_to_pose_video` 로직이 활성화된 경우, 출력 길이는 포즈 비디오 지속 시간에 맞게 조정됩니다
- `face_video`는 처리 시 자동으로 512x512 해상도로 크기 조정됩니다
- `continue_motion` 프레임은 `continue_motion_max_frames` 매개변수에 의해 제한됩니다
- 입력 비디오들(`face_video`, `pose_video`, `background_video`, `character_mask`)은 처리 전에 `video_frame_offset`만큼 오프셋됩니다
- `character_mask`에 프레임이 하나만 포함된 경우, 모든 프레임에 걸쳐 반복됩니다
- `clip_vision_output`가 제공된 경우, 긍정적 및 부정적 조건 모두에 적용됩니다

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 추가 비디오 컨텍스트가 포함된 수정된 긍정적 조건 |
| `negative` | CONDITIONING | 추가 비디오 컨텍스트가 포함된 수정된 부정적 조건 |
| `latent` | LATENT | 잠재 공간 형식으로 생성된 비디오 콘텐츠 |
| `trim_latent` | INT | 다운스트림 처리를 위한 잠재 공간 트리밍 정보 |
| `trim_image` | INT | 참조 모션 프레임을 위한 이미지 공간 트리밍 정보 |
| `video_frame_offset` | INT | 청크 방식으로 비디오 생성을 계속하기 위한 업데이트된 프레임 오프셋 |
