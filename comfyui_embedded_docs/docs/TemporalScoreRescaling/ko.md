# TSR - 시간적 점수 재조정

이 노드는 확산 모델에 TSR(Temporal Score Rescaling)을 적용합니다. 노이즈 제거 과정 중 예측된 노이즈 또는 점수(score)를 재조정하여 모델의 샘플링 동작을 수정하며, 이를 통해 생성 출력의 다양성을 조절할 수 있습니다. 이 기능은 CFG(Classifier-Free Guidance) 이후에 실행되는 함수로 구현됩니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | TSR 함수로 패치할 확산 모델입니다. | MODEL | 예 | - |
| `tsr_k` | 재조정 강도를 제어합니다. k 값이 낮을수록 이미지 생성 시 더 상세한 결과를 생성하고, k 값이 높을수록 더 부드러운 결과를 생성합니다. k = 1로 설정하면 재조정이 비활성화됩니다. (기본값: 0.95) | FLOAT | 아니요 | 0.01 - 100.0 |
| `tsr_sigma` | 재조정이 얼마나 일찍 적용되는지 제어합니다. 값이 클수록 더 일찍 적용됩니다. (기본값: 1.0) | FLOAT | 아니요 | 0.01 - 100.0 |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `patched_model` | 샘플링 과정에 TSR(Temporal Score Rescaling) 함수가 적용된 입력 모델입니다. | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/ko.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
