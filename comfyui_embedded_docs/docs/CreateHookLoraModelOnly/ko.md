> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/ko.md)

이 노드는 모델 컴포넌트에만 적용되는 LoRA(Low-Rank Adaptation) 훅을 생성하여 CLIP 컴포넌트에 영향을 주지 않고 모델 동작을 수정할 수 있도록 합니다. LoRA 파일을 로드하고 지정된 강도로 모델에 적용하면서 CLIP 컴포넌트는 변경하지 않고 유지합니다. 이 노드는 이전 훅들과 연결하여 복잡한 수정 파이프라인을 생성할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | 예 | 여러 옵션 사용 가능 | loras 폴더에서 로드할 LoRA 파일 이름 |
| `strength_model` | FLOAT | 예 | -20.0 ~ 20.0 | 모델 컴포넌트에 LoRA를 적용하기 위한 강도 배수 (기본값: 1.0) |
| `prev_hooks` | HOOKS | 아니오 | - | 이 훅과 연결할 선택적 이전 훅들 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `hooks` | HOOKS | 모델 처리에 적용할 수 있는 생성된 LoRA 훅 |