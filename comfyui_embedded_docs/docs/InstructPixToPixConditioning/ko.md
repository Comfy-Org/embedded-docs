# InstructPixToPix 조건 설정

InstructPixToPixConditioning 노드는 입력 이미지와 긍정 및 부정 텍스트 프롬프트 컨디셔닝을 결합하여 InstructPix2Pix 이미지 편집을 위한 컨디셔닝 데이터를 준비합니다. VAE를 사용하여 이미지를 잠재 표현으로 인코딩하고, 해당 잠재 표현을 두 컨디셔닝 세트에 모두 첨부하며, 동일한 차원의 0으로 채워진 잠재 표현을 생성합니다. 이미지의 너비 또는 높이가 8픽셀의 배수가 아닌 경우, 인코딩 전에 이미지가 자동으로 크롭됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 원하는 이미지 특성에 대한 텍스트 프롬프트와 설정이 포함된 긍정 컨디셔닝 데이터입니다. | CONDITIONING | 예 | - |
| `negative` | 원하지 않는 이미지 특성에 대한 텍스트 프롬프트와 설정이 포함된 부정 컨디셔닝 데이터입니다. | CONDITIONING | 예 | - |
| `vae` | 입력 이미지를 잠재 표현으로 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `pixels` | 잠재 공간으로 처리 및 인코딩될 입력 이미지입니다. | IMAGE | 예 | - |

**참고:** 입력 이미지는 VAE 인코딩 프로세스와의 호환성을 보장하기 위해 너비와 높이 모두 8픽셀의 배수로 내림 처리되어 자동으로 크롭됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 인코딩된 이미지 잠재 표현이 첨부된 긍정 컨디셔닝 데이터입니다. | CONDITIONING |
| `negative` | 인코딩된 이미지 잠재 표현이 첨부된 부정 컨디셔닝 데이터입니다. | CONDITIONING |
| `latent` | 인코딩된 이미지와 동일한 차원의 0으로 채워진 잠재 텐서입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/ko.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
