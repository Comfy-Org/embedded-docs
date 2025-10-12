> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/ko.md)

DualCFGGuider 노드는 이중 분류자 없는 지도(Classifier-Free Guidance) 샘플링을 위한 지도 시스템을 생성합니다. 두 개의 긍정적 조건 입력과 하나의 부정적 조건 입력을 결합하며, 각 조건 쌍에 서로 다른 지도 스케일을 적용하여 생성된 출력에 각 프롬프트의 영향을 제어합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 지도에 사용할 모델 |
| `cond1` | CONDITIONING | 예 | - | 첫 번째 긍정적 조건 입력 |
| `cond2` | CONDITIONING | 예 | - | 두 번째 긍정적 조건 입력 |
| `negative` | CONDITIONING | 예 | - | 부정적 조건 입력 |
| `cfg_conds` | FLOAT | 예 | 0.0 - 100.0 | 첫 번째 긍정적 조건에 대한 지도 스케일 (기본값: 8.0) |
| `cfg_cond2_negative` | FLOAT | 예 | 0.0 - 100.0 | 두 번째 긍정적 및 부정적 조건에 대한 지도 스케일 (기본값: 8.0) |
| `style` | COMBO | 예 | "regular"<br>"nested" | 적용할 지도 스타일 (기본값: "regular") |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | 샘플링에 사용할 준비된 구성된 지도 시스템 |