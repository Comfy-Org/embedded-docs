> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/ko.md)

SaveLoRA 노드는 LoRA(Low-Rank Adaptation) 모델을 파일로 저장합니다. LoRA 모델을 입력으로 받아 출력 디렉토리에 `.safetensors` 파일로 기록합니다. 최종 파일명에 포함될 파일명 접두사와 선택적으로 단계 수를 지정할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `lora` | MODEL | 예 | N/A | 저장할 LoRA 모델입니다. LoRA 레이어가 적용된 모델을 사용하지 마세요. |
| `prefix` | STRING | 예 | N/A | 저장할 LoRA 파일에 사용할 접두사입니다 (기본값: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | 아니요 | N/A | 선택사항: LoRA가 학습된 단계 수로, 저장된 파일의 이름을 지정하는 데 사용됩니다. |

**참고:** `lora` 입력은 순수 LoRA 모델이어야 합니다. LoRA 레이어가 적용된 기본 모델을 제공하지 마세요.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| *없음* | N/A | 이 노드는 워크플로우에 어떤 데이터도 출력하지 않습니다. 디스크에 파일을 저장하는 출력 노드입니다. |
