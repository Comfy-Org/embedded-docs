이 문서는 원래의 `Apply ControlNet(Advanced)` 노드에 대한 것입니다. 가장 오래된 `Apply ControlNet` 노드는 `Apply ControlNet(Old)`로 이름이 변경되었습니다. 호환성을 위해 comfyui.org에서 다운로드한 많은 워크플로우 폴더에서 `Apply ControlNet(Old)` 노드를 볼 수 있지만, 검색이나 노드 목록에서는 더 이상 `Apply ControlNet(Old)` 노드를 찾을 수 없습니다. 대신 `Apply ControlNet` 노드를 사용하세요.
이 노드는 주어진 이미지와 컨디셔닝에 ControlNet을 적용하여 Depth, OpenPose, Canny, HED 등과 같은 컨트롤 네트워크의 매개변수와 지정된 강도에 따라 이미지의 속성을 조정합니다.

ControlNet을 사용하려면 입력 이미지의 전처리가 필요합니다. ComfyUI 초기 노드에는 전처리기와 ControlNet 모델이 포함되어 있지 않으므로, 먼저 ContrlNet 전처리기[전처리기 다운로드](https://github.com/Fannovel16/comfy_controlnet_preprocessors)와 해당하는 ControlNet 모델을 설치하세요.

## 입력

| 매개변수 | 데이터 유형 | 기능 |
| --- | --- | --- |
| `positive` | `CONDITIONING` | `CLIP 텍스트 인코더` 또는 다른 컨디셔닝 입력에서의 긍정적 컨디셔닝 데이터 |
| `negative` | `CONDITIONING` | `CLIP 텍스트 인코더` 또는 다른 컨디셔닝 입력에서의 부정적 컨디셔닝 데이터 |
| `control_net` | `CONTROL_NET` | 적용할 ControlNet 모델, 일반적으로 `ControlNet 로더` 에서 입력 |
| `image` | `IMAGE` | ControlNet 적용을 위한 이미지, 전처리기로 처리 필요 |
| `vae` | `VAE` | Vae 모델 입력 |
| `strength` | `FLOAT` | 네트워크 조정의 강도를 제어, 값 범위 0~10. 권장 값은 0.5~1.5 사이가 적절합니다. 값이 낮을수록 모델의 자유도가 높고, 값이 높을수록 제약이 엄격해집니다. 값이 너무 높으면 이상한 이미지가 생성될 수 있습니다. |
| `start_percent` | `FLOAT` | 값 0.000~1.000, ControlNet 적용을 시작할 시점을 백분율로 결정, 예를 들어 0.2는 확산 프로세스의 20% 시점에서 ControlNet 가이드가 이미지 생성에 영향을 미치기 시작함을 의미 |
| `end_percent` | `FLOAT` | 값 0.000~1.000, ControlNet 적용을 종료할 시점을 백분율로 결정, 예를 들어 0.8은 확산 프로세스의 80% 시점에서 ControlNet 가이드가 이미지 생성에 대한 영향을 중단함을 의미 |

## 출력

| 매개변수 | 데이터 유형 | 기능 |
| --- | --- | --- |
| `positive` | `CONDITIONING` | ControlNet에 의해 처리된 긍정적 컨디셔닝 데이터, 다음 ControlNet 또는 K 샘플러 노드로 출력 가능 |
| `negative` | `CONDITIONING` | ControlNet에 의해 처리된 부정적 컨디셔닝 데이터, 다음 ControlNet 또는 K 샘플러 노드로 출력 가능 |

**T2IAdaptor 스타일 모델**을 사용하려면 대신 `Apply Style Model` 노드를 사용하세요
