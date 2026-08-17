# 포토메이커 인코딩

PhotoMakerEncode는 참조 이미지와 텍스트 프롬프트를 결합하여 AI 이미지 생성을 위한 컨디셔닝 데이터를 생성합니다. 텍스트 프롬프트에서 "photomaker"라는 단어를 검색하고, 해당 단어가 발견되면 PhotoMaker 모델을 사용하여 프롬프트의 해당 위치에 참조 이미지의 시각적 특성을 적용합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `photomaker` | 참조 이미지 처리 및 이미지 기반 임베딩 생성에 사용되는 PhotoMaker 모델 | PHOTOMAKER | 예 | - |
| `image` | 컨디셔닝에 시각적 특성을 제공하는 참조 이미지 | IMAGE | 예 | - |
| `clip` | 텍스트 토큰화 및 인코딩에 사용되는 CLIP 모델 | CLIP | 예 | - |
| `text` | 컨디셔닝 생성을 위한 텍스트 프롬프트. 여러 줄 및 동적 프롬프트를 지원합니다 (기본값: "photograph of photomaker") | STRING | 예 | - |

**참고:** 이미지 기반 컨디셔닝을 적용하려면 텍스트 프롬프트에 "photomaker"라는 단어가 별도의 단어로 포함되어야 합니다 (일치 여부는 대소문자를 구분합니다). 해당 단어가 있으면 이미지의 특성이 프롬프트의 해당 위치에 주입됩니다. "photomaker"가 없으면 이 노드는 이미지의 영향 없이 표준 텍스트 컨디셔닝을 반환합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `CONDITIONING` | 이미지 생성 안내를 위한 이미지 및 텍스트 임베딩을 포함하는 컨디셔닝 데이터와 CLIP 텍스트 인코더의 풀링된 출력 | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/ko.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
