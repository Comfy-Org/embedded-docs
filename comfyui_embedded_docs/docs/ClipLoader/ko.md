이 노드는 주로 CLIP 텍스트 인코더 모델을 독립적으로 로드하는 데 사용됩니다.
모델 파일은 다음 경로에서 감지할 수 있습니다:

- "ComfyUI/models/text_encoders/"
- "ComfyUI/models/clip/"

> ComfyUI 시작 후 모델을 저장한 경우, 최신 모델 파일 경로 목록을 가져오기 위해 ComfyUI 프론트엔드를 새로 고침해야 합니다

지원되는 모델 형식:

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

최신 모델 파일 로드에 대한 자세한 내용은 [folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py)를 참조하세요

## 입력

| 매개변수     | 데이터 유형 | 설명 |
|--------------|-------------|------|
| `CLIP 파일명` | COMBO[STRING] | 로드할 CLIP 모델의 이름을 지정합니다. 이 이름은 미리 정의된 디렉토리 구조 내에서 모델 파일을 찾는 데 사용됩니다. |
| `유형`       | COMBO[STRING] | 로드할 CLIP 모델의 유형을 결정합니다. ComfyUI가 지원하는 모델이 늘어남에 따라 여기에 새로운 유형이 추가됩니다. 자세한 내용은 [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)의 `CLIPLoader` 클래스 정의를 참조하세요. |
| `장치`       | COMBO[STRING] | CLIP 모델을 로드할 장치를 선택합니다. `default`는 GPU에서 모델을 실행하고, `CPU`를 선택하면 CPU에서 강제로 로드합니다. |

### 장치 옵션 설명

**"default"를 선택하는 경우:**

- 충분한 GPU 메모리가 있을 때
- 최상의 성능을 원할 때
- 시스템이 메모리 사용을 자동으로 최적화하도록 할 때

**"cpu"를 선택하는 경우:**

- GPU 메모리가 부족할 때
- 다른 모델(예: UNet)을 위해 GPU 메모리를 예약해야 할 때
- 낮은 VRAM 환경에서 실행할 때
- 디버깅이나 특수 목적이 필요할 때

**성능에 미치는 영향**

CPU에서 실행하면 GPU보다 훨씬 느리지만, 다른 중요한 모델 구성 요소를 위해 귀중한 GPU 메모리를 절약할 수 있습니다. 메모리가 제한된 환경에서는 CLIP 모델을 CPU에 배치하는 것이 일반적인 최적화 전략입니다.

### 지원되는 조합

| 모델 유형 | 해당 인코더 |
|-----------|------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

ComfyUI가 업데이트됨에 따라 이러한 조합이 확장될 수 있습니다. 자세한 내용은 [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)의 `CLIPLoader` 클래스 정의를 참조하세요.

## 출력

| 매개변수 | 데이터 유형 | 설명 |
|----------|-------------|------|
| `clip`   | CLIP        | 하위 작업이나 추가 처리를 위해 준비된 로드된 CLIP 모델입니다. |

## 추가 설명

CLIP 모델은 ComfyUI에서 텍스트 인코더로서 핵심적인 역할을 하며, 텍스트 프롬프트를 확산 모델이 이해할 수 있는 수치 표현으로 변환하는 책임을 집니다. 이를 번역가처럼 생각할 수 있으며, 텍스트를 대규모 모델이 이해할 수 있는 언어로 번역하는 역할을 합니다. 물론 서로 다른 모델에는 고유한 "방언"이 있기 때문에, 서로 다른 아키텍처 간의 텍스트 인코딩 프로세스를 완료하기 위해서는 서로 다른 CLIP 인코더가 필요합니다.
