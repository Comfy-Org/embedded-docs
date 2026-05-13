> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/ko.md)

UNETLoader 노드는 이름으로 U-Net 모델을 로드하도록 설계되어, 시스템 내에서 사전 훈련된 U-Net 아키텍처를 손쉽게 사용할 수 있도록 합니다.

이 노드는 `ComfyUI/models/diffusion_models` 폴더에 위치한 모델을 감지합니다.

## 입력

| 매개변수 | 데이터 타입 | 설명 |
|-------------|--------------|-------------|
| `unet_name` | COMBO[STRING] | 로드할 U-Net 모델의 이름을 지정합니다. 이 이름은 미리 정의된 디렉터리 구조 내에서 모델을 찾는 데 사용되며, 다양한 U-Net 모델을 동적으로 로드할 수 있도록 합니다. |
| `weight_dtype` | ... | 🚧  fp8_e4m3fn fp9_e5m2 |

## 출력

| 매개변수 | 데이터 타입 | 설명 |
|-----------|-------------|-------------|
| `model`   | MODEL     | 로드된 U-Net 모델을 반환하며, 시스템 내에서 추가 처리 또는 추론에 활용할 수 있도록 합니다. |