> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/ko.md)

TorchCompileModel 노드는 모델의 성능을 최적화하기 위해 PyTorch 컴파일을 적용합니다. 입력 모델의 복사본을 생성하고 지정된 백엔드를 사용하여 PyTorch의 컴파일 기능으로 래핑합니다. 이를 통해 추론 과정에서 모델의 실행 속도를 향상시킬 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `모델` | MODEL | 예 | - | 컴파일 및 최적화할 모델 |
| `백엔드` | STRING | 예 | "inductor"<br>"cudagraphs" | 최적화에 사용할 PyTorch 컴파일 백엔드 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `모델` | MODEL | PyTorch 컴파일이 적용된 컴파일된 모델 |