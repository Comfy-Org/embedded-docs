> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/ko.md)

LatentUpscaleModelLoader 노드는 잠재 표현(latent representation) 업스케일링을 위해 설계된 특수 모델을 불러옵니다. 시스템의 지정된 폴더에서 모델 파일을 읽고, 그 유형(720p, 1080p 또는 기타)을 자동으로 감지하여 올바른 내부 모델 아키텍처를 인스턴스화하고 구성합니다. 불러온 모델은 이후 다른 노드에서 잠재 공간 초해상도 작업에 사용할 준비가 됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | 예 | *`latent_upscale_models` 폴더 내 모든 파일* | 불러올 잠재 업스케일 모델 파일의 이름입니다. 사용 가능한 옵션은 ComfyUI의 `latent_upscale_models` 디렉토리에 있는 파일들로부터 동적으로 채워집니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | LATENT_UPSCALE_MODEL | 불러온 잠재 업스케일 모델로, 구성이 완료되어 사용 준비가 된 상태입니다. |
