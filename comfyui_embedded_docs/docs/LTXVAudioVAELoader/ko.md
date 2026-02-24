> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/ko.md)

LTXV Audio VAE Loader 노드는 체크포인트 파일에서 사전 학습된 오디오 변분 자동인코더(VAE) 모델을 불러옵니다. 지정된 체크포인트를 읽어 가중치와 메타데이터를 로드하고, ComfyUI 내 오디오 생성 또는 처리 워크플로우에서 사용할 수 있도록 모델을 준비합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | 예 | `checkpoints` 폴더 내 모든 파일.<br>*예시: `"audio_vae.safetensors"`* | 불러올 오디오 VAE 체크포인트입니다. 이는 ComfyUI `checkpoints` 디렉토리에 있는 모든 파일로 채워진 드롭다운 목록입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `Audio VAE` | VAE | 로드된 오디오 변분 자동인코더 모델로, 다른 오디오 처리 노드에 연결할 준비가 되었습니다. |
