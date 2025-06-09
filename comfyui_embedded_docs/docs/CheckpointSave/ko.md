`체크포인트 저장` 노드는 완전한 Stable Diffusion 모델(UNet, CLIP 및 VAE 구성 요소 포함)을 **.safetensors** 형식의 체크포인트 파일로 저장하도록 설계되었습니다.

이 노드는 주로 모델 병합 워크플로우에서 사용됩니다. `ModelMergeSimple`, `ModelMergeBlocks` 등의 노드를 통해 새로운 병합 모델을 생성한 후, 이 노드를 사용하여 결과를 재사용 가능한 체크포인트 파일로 저장할 수 있습니다.

## 입력

| 매개변수 | 데이터 유형 | 설명 |
|----------|------------|------|
| `모델` | MODEL | 저장할 주요 모델을 나타냅니다. 모델의 현재 상태를 캡처하여 나중에 복원하거나 분석하는 데 필수적입니다. |
| `clip` | CLIP | 주요 모델과 연관된 CLIP 모델의 매개변수로, 주요 모델과 함께 그 상태를 저장할 수 있습니다. |
| `vae` | VAE | 변분 오토인코더(VAE) 모델의 매개변수로, 주요 모델 및 CLIP과 함께 그 상태를 나중에 사용하거나 분석할 수 있도록 저장합니다. |
| `파일명 접두사` | STRING | 저장할 체크포인트의 파일 이름 접두사를 지정합니다. |

또한, 이 노드에는 메타데이터를 위한 두 개의 숨겨진 입력이 있습니다:

**prompt (PROMPT)**: 워크플로우 프롬프트 정보
**extra_pnginfo (EXTRA_PNGINFO)**: 추가 PNG 정보

## 출력

이 노드는 체크포인트 파일을 출력하며, 해당 출력 파일 경로는 `output/checkpoints/` 디렉토리입니다.

## 아키텍처 호환성

- 현재 완전 지원: SDXL, SD3, SVD 및 기타 주요 아키텍처, [소스 코드](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189) 참조
- 기본 지원: 다른 아키텍처도 저장 가능하나 표준화된 메타데이터 정보 없음

## 관련 링크

관련 소스 코드: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)
