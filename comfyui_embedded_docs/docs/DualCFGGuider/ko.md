> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/ko.md)

DualCFGGuider 노드는 이중 분류기-프리 가이던스 샘플링을 위한 가이던스 시스템을 생성합니다. 두 개의 긍정 조건부 입력과 하나의 부정 조건부 입력을 결합하여, 각 조건부 쌍에 서로 다른 가이던스 스케일을 적용함으로써 생성된 출력물에 대한 각 프롬프트의 영향을 제어합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 가이던스에 사용할 모델 |
| `cond1` | CONDITIONING | 예 | - | 첫 번째 긍정 조건부 입력 |
| `cond2` | CONDITIONING | 예 | - | 두 번째 긍정 조건부 입력 |
| `negative` | CONDITIONING | 예 | - | 부정 조건부 입력 |
| `cfg_conds` | FLOAT | 예 | 0.0 - 100.0 | 첫 번째 긍정 조건부에 대한 가이던스 스케일 (기본값: 8.0) |
| `cfg_cond2_negative` | FLOAT | 예 | 0.0 - 100.0 | 두 번째 긍정 조건부 및 부정 조건부에 대한 가이던스 스케일 (기본값: 8.0) |
| `style` | COMBO | 예 | "regular"<br>"nested" | 적용할 가이던스 스타일 (기본값: "regular"). "nested"로 설정하면 가이던스가 중첩 방식으로 적용됩니다 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | 샘플링에 사용할 준비가 된 구성된 가이던스 시스템 |

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`
