# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet 노드는 확산 합성 제어 네트워크 패치를 적용하여 기본 모델의 동작을 수정합니다. 이미지 입력과 선택적 마스크를 사용하여 조정 가능한 강도로 모델의 생성 과정을 안내하며, 제어 네트워크의 영향을 통합한 패치된 모델을 생성하여 보다 제어된 이미지 합성을 가능하게 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 제어 네트워크로 패치할 기본 모델 | MODEL | 예 | - |
| `model_patch` | 기본 모델에 적용할 제어 네트워크 패치 모델 | MODEL_PATCH | 예 | - |
| `vae` | 확산 과정에서 사용되는 VAE(변분 오토인코더) | VAE | 예 | - |
| `image` | 제어 네트워크를 안내하는 데 사용되는 입력 이미지(RGB 채널만 사용됨) | IMAGE | 예 | - |
| `strength` | 제어 네트워크 영향의 강도(기본값: 1.0) | FLOAT | 예 | -10.0 to 10.0 (step: 0.01) |
| `mask` | 제어 네트워크가 적용될 영역을 정의하는 선택적 마스크(내부적으로 반전됨) | MASK | 아니오 | - |

**참고:** 마스크가 제공되면 자동으로 반전(1.0 - 마스크)되고 제어 네트워크 처리에 필요한 차원에 맞게 재조정됩니다. 모델 패치가 ZImage Control 유형인 경우 노이즈 리파이너와 더블 블록 모두에 패치가 적용되고, 표준 DiffSynth 제어 네트워크의 경우 더블 블록 패치만 적용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 확산 합성 제어 네트워크 패치가 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/ko.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
