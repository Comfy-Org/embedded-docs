# OptimalStepsScheduler

OptimalStepsScheduler 노드는 선택한 모델 유형과 스텝 구성에 따라 확산 모델의 노이즈 스케줄 sigma 값을 계산합니다. `denoise` 매개변수에 따라 총 스텝 수를 조정하고 요청된 스텝 수에 맞게 노이즈 레벨을 보간합니다. 이 노드는 확산 샘플링 프로세스 중에 사용되는 노이즈 레벨을 결정하는 sigma 값의 시퀀스를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model_type` | 노이즈 레벨 계산에 사용할 확산 모델의 유형 | COMBO | 예 | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | 계산할 총 샘플링 스텝 수 (기본값: 20) | INT | 예 | 3-1000 |
| `denoise` | 디노이징 강도를 제어하며, 유효 스텝 수를 조정합니다 (기본값: 1.0) | FLOAT | 예 | 0.0-1.0 |

**참고:** `denoise`가 1.0 미만으로 설정되면 노드는 유효 스텝을 `steps * denoise`로 계산합니다. `denoise`가 0.0으로 설정되면 노드는 빈 텐서를 반환합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `sigmas` | 확산 샘플링을 위한 노이즈 스케줄을 나타내는 sigma 값의 시퀀스 | SIGMAS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/ko.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
