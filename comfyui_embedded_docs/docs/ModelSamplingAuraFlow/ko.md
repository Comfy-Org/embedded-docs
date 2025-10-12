> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/ko.md)

ModelSamplingAuraFlow 노드는 AuraFlow 모델 아키텍처에 특화된 샘플링 구성을 확산 모델에 적용합니다. 이 노드는 샘플링 분포를 조정하는 시프트 매개변수를 적용하여 모델의 샘플링 동작을 수정합니다. SD3 모델 샘플링 프레임워크를 상속하며 샘플링 프로세스에 대한 세밀한 제어를 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | AuraFlow 샘플링 구성을 적용할 확산 모델 |
| `shift` | FLOAT | 예 | 0.0 - 100.0 | 샘플링 분포에 적용할 시프트 값 (기본값: 1.73) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | AuraFlow 샘플링 구성이 적용된 수정된 모델 |