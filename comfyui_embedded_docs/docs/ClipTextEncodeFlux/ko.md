# CLIP 텍스트 인코딩 (FLUX)

`CLIPTextEncodeFlux`는 Flux 아키텍처를 위해 설계된 텍스트 인코딩 노드입니다. CLIP-L과 T5XXL이라는 서로 다른 인코더를 통해 두 개의 개별 텍스트 입력을 처리하고, 이를 guidance 스케일과 결합하여 이미지 생성을 위한 통합 컨디셔닝 출력을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip` | Flux 아키텍처를 지원하는 CLIP 모델로, CLIP-L 및 T5XXL 인코더를 모두 포함합니다. | CLIP | 예 | - |
| `clip_l` | CLIP-L 인코더에서 처리되는 텍스트 입력입니다. 스타일이나 테마와 같은 간결한 키워드 설명에 적합합니다. 여러 줄 입력과 동적 프롬프트를 지원합니다. | STRING | 예 | - |
| `t5xxl` | T5XXL 인코더에서 처리되는 텍스트 입력입니다. 복잡한 장면과 세부 사항을 표현하는 상세한 자연어 설명에 적합합니다. 여러 줄 입력과 동적 프롬프트를 지원합니다. | STRING | 예 | - |
| `guidance` | 텍스트 조건이 생성 과정에 미치는 영향을 제어합니다. 값이 높을수록 텍스트를 더 엄격하게 따릅니다. 기본값: 3.5. | FLOAT | 예 | 0.0 - 100.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `CONDITIONING` | 두 인코더의 결합된 임베딩과 guidance 값을 포함하며, 조건부 이미지 생성에 사용됩니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/ko.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`
