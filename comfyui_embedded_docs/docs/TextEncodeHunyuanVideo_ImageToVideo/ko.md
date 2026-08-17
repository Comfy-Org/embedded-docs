# HunyuanVideo 텍스트 인코딩 (이미지 → 비디오)

TextEncodeHunyuanVideo_ImageToVideo 노드는 텍스트 프롬프트와 이미지 임베딩을 결합하여 비디오 생성을 위한 컨디셔닝 데이터를 생성합니다. CLIP 모델을 사용하여 텍스트 입력과 CLIP 비전 출력의 시각적 정보를 모두 처리한 다음, 지정된 이미지 인터리브 설정에 따라 이 두 소스를 혼합하는 토큰을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip` | 토큰화 및 인코딩에 사용되는 CLIP 모델 | CLIP | 예 | - |
| `clip_vision_output` | 이미지 컨텍스트를 제공하는 CLIP 비전 모델의 시각적 임베딩 | CLIP_VISION_OUTPUT | 예 | - |
| `prompt` | 비디오 생성을 안내하는 텍스트 설명입니다. 여러 줄 입력과 동적 프롬프트를 지원합니다. 프롬프트는 참조 이미지를 기반으로 비디오를 설명하도록 모델에 요청하는 템플릿을 사용하여 형식화되며, 주요 내용, 객체 세부 사항, 동작, 배경, 카메라 각도 등의 측면을 다룹니다. | STRING | 예 | - |
| `image_interleave` | 이미지가 텍스트 프롬프트 대비 얼마나 많은 영향을 미치는지를 나타냅니다. 숫자가 높을수록 텍스트 프롬프트의 영향이 커집니다. (기본값: 2, 고급 매개변수) | INT | 예 | 1-512 |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `CONDITIONING` | 비디오 생성을 위해 텍스트와 이미지 정보를 결합한 컨디셔닝 데이터 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
