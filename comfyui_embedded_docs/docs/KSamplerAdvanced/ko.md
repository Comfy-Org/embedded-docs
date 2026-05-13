> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/ko.md)

KSamplerAdvanced 노드는 고급 구성과 기술을 제공하여 샘플링 프로세스를 개선하도록 설계되었습니다. 기본 KSampler 기능을 개선하여 모델에서 샘플을 생성하기 위한 보다 정교한 옵션을 제공하는 것을 목표로 합니다.

## 입력

| 매개변수 | 데이터 타입 | 설명 |
|---|---|---|
| `model` | MODEL | 샘플을 생성할 모델을 지정하며, 샘플링 과정에서 중요한 역할을 합니다. |
| `add_noise` | COMBO[STRING] | 샘플링 과정에 노이즈를 추가할지 여부를 결정하며, 생성된 샘플의 다양성과 품질에 영향을 줍니다. |
| `noise_seed` | INT | 노이즈 생성을 위한 시드 값을 설정하여 샘플링 과정의 재현성을 보장합니다. |
| `steps` | INT | 샘플링 과정에서 수행할 단계 수를 정의하며, 출력물의 세부 묘사와 품질에 영향을 줍니다. |
| `cfg` | FLOAT | 조건화 계수를 제어하여 샘플링 과정의 방향과 공간에 영향을 줍니다. |
| `sampler_name` | COMBO[STRING] | 사용할 특정 샘플러를 선택하여 샘플링 기술을 사용자 정의할 수 있습니다. |
| `scheduler` | COMBO[STRING] | 샘플링 과정을 제어하기 위한 스케줄러를 선택하며, 샘플의 진행과 품질에 영향을 줍니다. |
| `positive` | CONDITIONING | 샘플링을 원하는 속성으로 안내하기 위한 긍정적 조건을 지정합니다. |
| `negative` | CONDITIONING | 샘플링이 특정 속성에서 멀어지도록 유도하기 위한 부정적 조건을 지정합니다. |
| `latent_image` | LATENT | 샘플링 과정에서 사용할 초기 잠재 이미지를 제공하며, 시작점 역할을 합니다. |
| `start_at_step` | INT | 샘플링 과정의 시작 단계를 결정하여 샘플링 진행을 제어할 수 있습니다. |
| `end_at_step` | INT | 샘플링 과정의 종료 단계를 설정하여 샘플링 범위를 정의합니다. |
| `return_with_leftover_noise` | COMBO[STRING] | 잔여 노이즈가 있는 상태로 샘플을 반환할지 여부를 나타내며, 최종 출력물의 외관에 영향을 줍니다. |

## 출력

| 매개변수 | 데이터 타입 | 설명 |
|---|---|---|
| `latent` | LATENT | 출력은 모델에서 생성된 잠재 이미지를 나타내며, 적용된 구성과 기술을 반영합니다. |