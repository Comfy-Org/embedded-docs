# WanSCAILToVideo

WanSCAILToVideo 노드는 비디오 생성을 위한 컨디셔닝과 빈 잠재 공간을 준비합니다. 참조 이미지, 포즈 비디오, CLIP 비전 출력, 이전 프레임 청크와 같은 선택적 입력을 처리하여 비디오 모델의 긍정 및 부정 컨디셔닝에 임베딩합니다. 이 노드는 수정된 컨디셔닝과 지정된 비디오 크기의 빈 잠재 텐서를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 긍정(positive) 컨디셔닝 입력입니다. | CONDITIONING | 예 | - |
| `negative` | 부정(negative) 컨디셔닝 입력입니다. | CONDITIONING | 예 | - |
| `vae` | 이미지와 비디오 프레임을 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `width` | 출력 비디오의 너비(픽셀 단위)입니다 (기본값: 512). 32 단위로 조절할 수 있습니다. | INT | 예 | 32 ~ MAX_RESOLUTION |
| `height` | 출력 비디오의 높이(픽셀 단위)입니다 (기본값: 896). 32 단위로 조절할 수 있습니다. | INT | 예 | 32 ~ MAX_RESOLUTION |
| `length` | 비디오의 프레임 수입니다 (기본값: 81). 1부터 시작하여 4 단위로 조절할 수 있습니다. | INT | 예 | 1 ~ MAX_RESOLUTION |
| `batch_size` | 한 배치에서 생성할 비디오 수입니다 (기본값: 1). | INT | 예 | 1 ~ 4096 |
| `pose_strength` | 포즈 잠재 표현의 강도입니다 (기본값: 1.0). | FLOAT | 예 | 0.0 ~ 10.0 |
| `pose_start` | 포즈 컨디셔닝의 시작 단계입니다 (기본값: 0.0). | FLOAT | 예 | 0.0 ~ 1.0 |
| `pose_end` | 포즈 컨디셔닝의 종료 단계입니다 (기본값: 1.0). | FLOAT | 예 | 0.0 ~ 1.0 |
| `video_frame_offset` | 이 청크(chunk)가 시작되는 누적 출력 프레임입니다. 이전 청크의 `video_frame_offset` 출력에서 연결하십시오 (기본값: 0). | INT | 예 | 0 ~ MAX_RESOLUTION |
| `previous_frame_count` | 앵커링에 사용할 `previous_frames`의 꼬리 프레임 수입니다. SCAIL-2는 5로 학습되었습니다 (81프레임 청크, 76프레임 스텝) (기본값: 5). | INT | 예 | 1 ~ MAX_RESOLUTION |
| `pose_video` | 포즈 컨디셔닝에 사용되는 비디오입니다. 메인 비디오 해상도의 절반으로 축소됩니다. | IMAGE | 아니요 | - |
| `pose_video_mask` | SCAIL-2 전용입니다. `pose_video`와 동일한 해상도의 신원별 색상 SAM3 마스크 비디오입니다. | IMAGE | 아니요 | - |
| `replacement_mode` | SCAIL-2 전용입니다. False = 애니메이션 모드 (`pose_video_mask`의 배경은 검은색이어야 함). True = 대체 모드 (`pose_video_mask`의 배경은 흰색이어야 함). 기본값: False. | BOOLEAN | 아니요 | - |
| `reference_image` | 참조 이미지입니다. 첫 번째 이미지가 기본 참조 이미지이며 모든 개체를 그 위에 합성합니다. SCAIL-2: 추가 배치 이미지는 추가 뷰(뒷모습, 클로즈업, 가려진 배경)로 사용되며, 각각 해당 개체 색상의 일치하는 `reference_image_mask`가 필요합니다. | IMAGE | 아니요 | - |
| `reference_image_mask` | SCAIL-2 전용입니다. 색상 참조 마스크로, `reference_image`와 배치 매칭됩니다 (첫 번째 = 기본 참조 마스크, 나머지 = 추가 `reference_image`에 대한 개체 마스크). | IMAGE | 아니요 | - |
| `clip_vision_output` | 컨디셔닝을 위한 CLIP 비전 특징입니다. 모델은 화면 비율에 맞춰 늘리는 리사이즈 방식으로 학습되었습니다. | CLIP_VISION_OUTPUT | 아니요 | - |
| `previous_frames` | SCAIL-2 전용입니다. 이전 청크의 완전히 디코딩된 출력입니다. 마지막 `previous_frame_count`개만 확장 앵커로 사용됩니다. | IMAGE | 아니요 | - |

**참고:**

- `pose_video` 및 `pose_video_mask` 입력은 `video_frame_offset`부터 시작하여 슬라이스됩니다. 해당 오프셋 이후 프레임이 없으면 비디오는 무시됩니다. 그런 다음 둘 중 더 짧은 길이에 맞춰 함께 잘리며 `length` 프레임으로 제한됩니다. `pose_video`는 인코딩 전에 메인 비디오 해상도의 절반으로 축소됩니다.
- `reference_image_mask` 입력은 `reference_image`도 함께 제공될 때만 적용됩니다. `reference_image` 배치의 각 이미지는 단일 프레임 잠재 참조로 개별 인코딩됩니다. 대체 모드(`replacement_mode=True`)에서는 참조 이미지가 알파 매트로 참조 이미지 마스크를 사용하여 검은 배경 위에 합성됩니다.
- `clip_vision_output`이 제공되면 긍정 및 부정 컨디셔닝 모두에 적용됩니다.
- `previous_frames`가 제공되면 마지막 `previous_frame_count` 프레임만 확장 앵커로 사용됩니다. 출력 잠재 표현은 이들 프레임의 인코딩으로 부분적으로 채워지고, 노이즈 마스크가 잠재 출력에 포함되며, `video_frame_offset`은 유지된 프레임 수를 빼서 조정됩니다 (0 미만이 되지 않음).

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `positive` | 수정된 긍정 컨디셔닝으로, 포함될 수 있는 요소는 임베딩된 참조 이미지 잠재 표현, CLIP 비전 출력, 포즈 비디오 잠재 표현, 드라이빙 마스크, 참조 마스크 또는 이전 프레임 잠재 표현입니다. | CONDITIONING |
| `negative` | 수정된 부정 컨디셔닝으로, 포함될 수 있는 요소는 임베딩된 참조 이미지 잠재 표현, CLIP 비전 출력, 포즈 비디오 잠재 표현, 드라이빙 마스크, 참조 마스크 또는 이전 프레임 잠재 표현입니다. | CONDITIONING |
| `latent` | 형태가 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`인 빈 잠재 텐서입니다. `previous_frames`가 제공되면 잠재 표현이 인코딩된 이전 프레임으로 부분적으로 채워지고 노이즈 마스크가 포함됩니다. | LATENT |
| `video_frame_offset` | 조정된 오프셋 + 길이입니다. 순차 비디오 생성을 위해 다음 청크에 연결합니다. | INT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
