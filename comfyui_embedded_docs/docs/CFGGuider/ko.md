# CFG 가이드

CFGGuider 노드는 이미지 생성 과정에서 샘플링을 제어하기 위한 가이던스 시스템을 생성합니다. 이 노드는 모델과 함께 positive 및 negative 컨디셔닝 입력을 받은 다음, classifier-free guidance 스케일을 적용하여 원하지 않는 요소를 피하면서 원하는 콘텐츠를 향해 생성을 유도합니다. 이 노드는 샘플링 노드에서 이미지 생성 방향을 제어하는 데 사용할 수 있는 guider 객체를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 가이던스에 사용할 모델 | MODEL | 예 | - |
| `positive` | 원하는 콘텐츠로 생성을 유도하는 포지티브 컨디셔닝 | CONDITIONING | 예 | - |
| `negative` | 원하지 않는 콘텐츠에서 생성을 멀어지게 하는 네거티브 컨디셔닝 | CONDITIONING | 예 | - |
| `cfg` | 컨디셔닝이 생성에 미치는 영향력을 조절하는 classifier-free guidance 스케일 (기본값: 8.0) | FLOAT | 예 | 0.0 to 100.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `GUIDER` | 샘플링 노드에 전달하여 생성 과정을 제어할 수 있는 guider 객체 | GUIDER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/ko.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
