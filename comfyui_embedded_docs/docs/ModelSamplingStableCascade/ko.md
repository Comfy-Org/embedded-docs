# 모델 샘플링 (StableCascade)

ModelSamplingStableCascade 노드는 shift 값을 사용하여 샘플링 매개변수를 조정함으로써 모델에 Stable Cascade 샘플링을 적용합니다. 이 노드는 Stable Cascade 생성을 위한 사용자 지정 샘플링 구성을 갖춘 입력 모델의 수정된 복제본을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | Stable Cascade 샘플링을 적용할 입력 모델 | MODEL | 예 | - |
| `shift` | 샘플링 매개변수에 적용할 shift 값 (기본값: 2.0) | FLOAT | 예 | 0.0 - 100.0 (단계: 0.01) |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | Stable Cascade 샘플링이 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/ko.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
