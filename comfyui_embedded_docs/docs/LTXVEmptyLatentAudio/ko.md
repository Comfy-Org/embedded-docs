> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/ko.md)

LTXV Empty Latent Audio 노드는 빈(0으로 채워진) 잠재 오디오 텐서 배치를 생성합니다. 제공된 Audio VAE 모델의 구성을 사용하여 채널 수 및 주파수 빈(bin) 수와 같은 잠재 공간의 올바른 차원을 결정합니다. 이 빈 잠재 텐서는 ComfyUI 내에서 오디오 생성 또는 조작 워크플로우의 시작점으로 사용됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `frames_number` | INT | 예 | 1 ~ 1000 | 프레임 수입니다. 기본값은 97입니다. |
| `frame_rate` | INT | 예 | 1 ~ 1000 | 초당 프레임 수입니다. 기본값은 25입니다. |
| `batch_size` | INT | 예 | 1 ~ 4096 | 배치 내 잠재 오디오 샘플의 수입니다. 기본값은 1입니다. |
| `audio_vae` | VAE | 예 | 해당 없음 | 구성을 가져올 Audio VAE 모델입니다. 이 매개변수는 필수입니다. |

**참고:** `audio_vae` 입력은 필수입니다. 제공되지 않으면 노드에서 오류가 발생합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `Latent` | LATENT | 입력 Audio VAE와 일치하도록 구성된 (samples, sample_rate, type) 구조를 가진 빈 잠재 오디오 텐서입니다. |
