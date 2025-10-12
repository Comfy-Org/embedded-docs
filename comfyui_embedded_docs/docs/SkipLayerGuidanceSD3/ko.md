> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/ko.md)

SkipLayerGuidanceSD3 노드는 건너뛴 레이어를 사용하여 추가적인 classifier-free guidance 세트를 적용하여 세부 구조에 대한 guidance를 향상시킵니다. 이 실험적 구현은 Perturbed Attention Guidance에서 영감을 받았으며, 생성된 출력에서 구조적 세부 사항을 개선하기 위해 네거티브 conditioning 과정에서 특정 레이어를 선택적으로 우회하는 방식으로 작동합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `모델` | MODEL | 예 | - | skip layer guidance를 적용할 모델 |
| `layers` | STRING | 예 | - | 건너뛸 레이어 인덱스의 쉼표로 구분된 목록 (기본값: "7, 8, 9") |
| `크기` | FLOAT | 예 | 0.0 - 10.0 | skip layer guidance 효과의 강도 (기본값: 3.0) |
| `시작 퍼센트` | FLOAT | 예 | 0.0 - 1.0 | 전체 단계의 백분율로 표시된 guidance 적용 시작 지점 (기본값: 0.01) |
| `종료 퍼센트` | FLOAT | 예 | 0.0 - 1.0 | 전체 단계의 백분율로 표시된 guidance 적용 종료 지점 (기본값: 0.15) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `모델` | MODEL | skip layer guidance가 적용된 수정된 모델 |
