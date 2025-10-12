> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/ko.md)

건너뛰기 레이어를 사용한 다른 CFG 네거티브 세트를 활용하여 세부 구조에 대한 안내를 향상시킵니다. 이 일반화된 버전의 SkipLayerGuidance는 모든 DiT 모델에서 사용할 수 있으며 Perturbed Attention Guidance에서 영감을 받았습니다. 원래 실험적 구현은 SD3용으로 만들어졌습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 건너뛰기 레이어 안내를 적용할 모델 |
| `double_layers` | STRING | 예 | - | 건너뛸 더블 블록의 레이어 번호를 쉼표로 구분하여 지정 (기본값: "7, 8, 9") |
| `single_layers` | STRING | 예 | - | 건너뛸 싱글 블록의 레이어 번호를 쉼표로 구분하여 지정 (기본값: "7, 8, 9") |
| `scale` | FLOAT | 예 | 0.0 - 10.0 | 안내 스케일 계수 (기본값: 3.0) |
| `start_percent` | FLOAT | 예 | 0.0 - 1.0 | 안내 적용 시작 비율 (기본값: 0.01) |
| `end_percent` | FLOAT | 예 | 0.0 - 1.0 | 안내 적용 종료 비율 (기본값: 0.15) |
| `rescaling_scale` | FLOAT | 예 | 0.0 - 10.0 | 재조정 스케일 계수 (기본값: 0.0) |

**참고:** `double_layers`와 `single_layers`가 모두 비어있는 경우(레이어 번호가 없는 경우), 이 노드는 안내를 적용하지 않고 원본 모델을 반환합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 건너뛰기 레이어 안내가 적용된 수정된 모델 |