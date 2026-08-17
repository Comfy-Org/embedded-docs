# 모델 샘플링 (SD3)

ModelSamplingSD3 노드는 모델에 Stable Diffusion 3 샘플링 매개변수를 적용합니다. shift 매개변수를 조정하여 모델의 샘플링 동작을 수정하며, 이 매개변수는 샘플링 분포 특성을 제어합니다. 이 노드는 지정된 샘플링 구성이 적용된 입력 모델의 수정된 복사본을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | SD3 샘플링 매개변수를 적용할 입력 모델입니다. | MODEL | 예 | - |
| `shift` | 샘플링 shift 매개변수를 제어합니다 (기본값: 3.0). | FLOAT | 예 | 0.0 - 100.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | SD3 샘플링 매개변수가 적용된 수정된 모델입니다. | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/ko.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
