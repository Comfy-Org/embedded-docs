> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/ko.md)

LTXVConcatAVLatent 노드는 비디오 잠재 표현과 오디오 잠재 표현을 단일의 연결된 잠재 출력으로 결합합니다. 두 입력의 `samples` 텐서를 병합하고, 존재하는 경우 해당 `noise_mask` 텐서도 함께 병합하여 비디오 생성 파이프라인에서의 추가 처리를 준비합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `video_latent` | LATENT | 예 | | 비디오 데이터의 잠재 표현입니다. |
| `audio_latent` | LATENT | 예 | | 오디오 데이터의 잠재 표현입니다. |

**참고:** `video_latent`와 `audio_latent` 입력의 `samples` 텐서는 연결됩니다. 입력 중 하나에 `noise_mask`가 포함되어 있으면 사용되며, 하나가 누락된 경우 해당 입력에 대해 1로 채워진 마스크(해당 `samples`와 동일한 형태)가 생성됩니다. 그런 다음 결과 마스크도 연결됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `latent` | LATENT | 비디오 및 오디오 입력에서 연결된 `samples`와, 해당되는 경우 연결된 `noise_mask`를 포함하는 단일 잠재 딕셔너리입니다. |
