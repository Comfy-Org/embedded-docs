이 노드는 `ComfyUI/models/checkpoints` 폴더에 있는 모델을 감지하며,
또한 extra_model_paths.yaml 파일에서 설정한 추가 경로의 모델도 읽어옵니다.
때때로 **ComfyUI 인터페이스를 새로 고침**해야 해당 폴더의 모델 파일을 읽을 수 있습니다.

unCLIPCheckpointLoader 노드는 unCLIP 모델에 맞춰진 체크포인트를 로드하도록 설계되었습니다. 이 노드는 지정된 체크포인트에서 모델, CLIP 비전 모듈 및 VAE를 검색하고 초기화하여, 추가 작업이나 분석을 위한 설정 과정을 간소화합니다.

## 입력

| 필드      | Comfy dtype       | 설명                                                                       |
|------------|-------------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| `COMBO[STRING]`    | 로드할 체크포인트의 이름을 지정하며, 사전 정의된 디렉토리에서 올바른 체크포인트 파일을 식별하고 검색하여 모델과 설정의 초기화를 결정합니다. |

## 출력

| 필드       | Comfy dtype   | 설명                                                              | Python dtype         |
|-------------|---------------|--------------------------------------------------------------------------|---------------------|
| `model`     | `MODEL`       | 체크포인트에서 로드된 주요 모델을 나타냅니다.                   | `torch.nn.Module`   |
| `clip`      | `CLIP`        | 체크포인트에서 로드된 CLIP 모듈을 나타내며, 사용 가능한 경우에 한합니다.      | `torch.nn.Module`   |
| `vae`       | `VAE`         | 체크포인트에서 로드된 VAE 모듈을 나타내며, 사용 가능한 경우에 한합니다.        | `torch.nn.Module`   |
| `clip_vision`| `CLIP_VISION` | 체크포인트에서 로드된 CLIP 비전 모듈을 나타내며, 사용 가능한 경우에 한합니다.| `torch.nn.Module`   |
