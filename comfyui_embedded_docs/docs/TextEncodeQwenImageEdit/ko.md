# TextEncodeQwenImageEdit

TextEncodeQwenImageEdit 노드는 텍스트 프롬프트와 선택적 이미지를 처리하여 이미지 생성 또는 편집을 위한 컨디셔닝 데이터를 생성합니다. CLIP 모델을 사용하여 입력을 토큰화하고, VAE를 사용하여 참조 이미지를 선택적으로 인코딩하여 참조 잠재 벡터를 생성할 수 있습니다. 이미지가 제공되면 일관된 처리 크기를 유지하기 위해 이미지가 자동으로 크기 조정됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `clip` | 텍스트 및 이미지 토큰화에 사용되는 CLIP 모델 | CLIP | 예 | - |
| `prompt` | 컨디셔닝 생성을 위한 텍스트 프롬프트로, 여러 줄 입력 및 동적 프롬프트를 지원합니다 | STRING | 예 | - |
| `vae` | 참조 이미지를 잠재 벡터로 인코딩하는 데 사용되는 선택적 VAE 모델 | VAE | 아니요 | - |
| `image` | 참조 또는 편집 목적으로 사용되는 선택적 입력 이미지 | IMAGE | 아니요 | - |

**참고:** `image`와 `vae`가 모두 제공되면 노드는 이미지를 참조 잠재 벡터로 인코딩하여 컨디셔닝 출력에 첨부합니다. 이미지는 약 1024x1024 픽셀의 일관된 처리 스케일을 유지하도록 자동으로 크기가 조정됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `CONDITIONING` | 이미지 생성에 사용되는 텍스트 토큰과 선택적 참조 잠재 벡터를 포함하는 컨디셔닝 데이터 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/ko.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
