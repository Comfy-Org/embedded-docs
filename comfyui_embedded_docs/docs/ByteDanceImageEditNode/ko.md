> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/ko.md)

다음은 제공된 영어 문서를 한국어로 번역한 결과입니다.

---

ByteDance Image Edit 노드는 API를 통해 ByteDance의 AI 모델을 사용하여 이미지를 수정할 수 있도록 합니다. 입력 이미지와 원하는 변경 사항을 설명하는 텍스트 프롬프트를 제공하면, 노드가 사용자의 지침에 따라 이미지를 처리합니다. 이 노드는 API 통신을 자동으로 처리하고 수정된 이미지를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Image2ImageModelName 옵션 | 모델 이름 |
| `image` | IMAGE | IMAGE | - | - | 편집할 기본 이미지 |
| `prompt` | STRING | STRING | "" | - | 이미지 편집 지침 |
| `seed` | INT | INT | 0 | 0-2147483647 | 생성에 사용할 시드 |
| `guidance_scale` | FLOAT | FLOAT | 5.5 | 1.0-10.0 | 값이 높을수록 이미지가 프롬프트를 더 정확하게 따릅니다 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 이미지에 "AI 생성" 워터마크를 추가할지 여부 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | ByteDance API에서 반환된 편집된 이미지 |

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
