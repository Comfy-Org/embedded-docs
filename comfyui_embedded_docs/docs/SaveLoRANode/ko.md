> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/ko.md)

SaveLoRA 노드는 LoRA(Low-Rank Adaptation) 모델을 출력 디렉토리에 저장합니다. LoRA 모델을 입력으로 받아 자동으로 생성된 파일명으로 safetensors 파일을 생성합니다. 파일명 접두사를 사용자 정의할 수 있으며, 선택적으로 학습 스텝 수를 파일명에 포함하여 더 체계적으로 관리할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `lora` | LORA_MODEL | 예 | - | 저장할 LoRA 모델입니다. LoRA 레이어가 적용된 모델을 사용하지 마세요. |
| `prefix` | STRING | 예 | - | 저장할 LoRA 파일에 사용할 접두사입니다 (기본값: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | 아니오 | - | 선택사항: LoRA가 학습된 스텝 수로, 저장되는 파일의 이름을 지정하는 데 사용됩니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| *없음* | - | 이 노드는 어떤 출력도 반환하지 않지만, LoRA 모델을 출력 디렉토리에 저장합니다. |
