# FreeU

FreeU 노드는 모델의 출력 블록에 주파수 영역 수정을 적용하여 이미지 생성 품질을 향상시킵니다. 다양한 채널 그룹의 스케일을 조정하고 특정 특징 맵에 푸리에 필터링을 적용하여 생성 과정에서 모델의 동작을 세밀하게 제어할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | FreeU 수정을 적용할 모델 | MODEL | 예 | - |
| `b1` | model_channels × 4 특징에 대한 백본 스케일링 계수 (기본값: 1.1) | FLOAT | 예 | 0.0 - 10.0 |
| `b2` | model_channels × 2 특징에 대한 백본 스케일링 계수 (기본값: 1.2) | FLOAT | 예 | 0.0 - 10.0 |
| `s1` | model_channels × 4 특징에 대한 스킵 연결 스케일링 계수 (기본값: 0.9) | FLOAT | 예 | 0.0 - 10.0 |
| `s2` | model_channels × 2 특징에 대한 스킵 연결 스케일링 계수 (기본값: 0.2) | FLOAT | 예 | 0.0 - 10.0 |

참고: 수정은 model_channels × 4 및 model_channels × 2 채널을 가진 특징 맵에만 적용됩니다. `b1`/`s1`은 전자에, `b2`/`s2`는 후자에 영향을 줍니다. 다른 특징 맵은 변경되지 않습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | FreeU 패치가 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/ko.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
