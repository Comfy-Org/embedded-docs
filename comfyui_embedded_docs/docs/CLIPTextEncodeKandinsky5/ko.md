> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/ko.md)

CLIPTextEncodeKandinsky5 노드는 Kandinsky 5 모델과 함께 사용할 텍스트 프롬프트를 준비합니다. 두 개의 개별 텍스트 입력을 받아 제공된 CLIP 모델을 사용하여 토큰화하고, 이를 단일 조건부 출력으로 결합합니다. 이 출력은 이미지 생성 과정을 안내하는 데 사용됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 예 | | 텍스트 프롬프트를 토큰화하고 인코딩하는 데 사용되는 CLIP 모델입니다. |
| `clip_l` | STRING | 예 | | 기본 텍스트 프롬프트입니다. 이 입력은 여러 줄 텍스트와 동적 프롬프트를 지원합니다. |
| `qwen25_7b` | STRING | 예 | | 보조 텍스트 프롬프트입니다. 이 입력은 여러 줄 텍스트와 동적 프롬프트를 지원합니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 두 텍스트 프롬프트에서 생성된 결합된 조건부 데이터로, Kandinsky 5 모델에 입력하여 이미지 생성을 수행할 준비가 되었습니다. |

---
**Source fingerprint (SHA-256):** `80227cf87d46bfa42b07976ab29996ae9583a4c461b2f2408db4b7016d3e1a0c`
