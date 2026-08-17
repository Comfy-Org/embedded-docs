# LCM 확대 샘플러

SamplerLCMUpscale 노드는 Latent Consistency Model(LCM) 샘플링과 이미지 업스케일링 기능을 결합한 특수 샘플링 방법을 제공합니다. 다양한 보간 방법을 사용하여 샘플링 과정 중에 이미지를 업스케일할 수 있으며, 이미지 품질을 유지하면서 더 높은 해상도의 출력을 생성하는 데 유용합니다. 업스케일링은 대상 `scale_ratio`에 도달할 때까지 샘플링 단계에 걸쳐 점진적으로 적용됩니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `scale_ratio` | 업스케일링 중에 적용할 배율입니다 (기본값: 1.0) | FLOAT | 아니요 | 0.1 - 20.0 |
| `scale_steps` | 업스케일링 프로세스에 사용할 단계 수입니다. 자동 계산에는 -1을 사용합니다 (기본값: -1) | INT | 아니요 | -1 - 1000 |
| `upscale_method` | 이미지를 업스케일링하는 데 사용되는 보간 방법입니다 (기본값: bislerp) | COMBO | 예 | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

참고: `scale_steps`가 양수 값으로 설정된 경우, 유효 업스케일링 단계 수는 샘플러의 총 샘플링 단계 수에 의해 제한됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `sampler` | 샘플링 파이프라인에서 사용할 수 있는 구성된 샘플러 객체를 반환합니다. | SAMPLER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/ko.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
