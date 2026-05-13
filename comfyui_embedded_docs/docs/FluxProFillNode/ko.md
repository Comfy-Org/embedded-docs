> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/en.md)

마스크와 프롬프트를 기반으로 이미지를 인페인트합니다. 이 노드는 Flux.1 모델을 사용하여 제공된 텍스트 설명에 따라 이미지의 마스크 영역을 채우고, 주변 이미지와 일치하는 새로운 콘텐츠를 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 인페인트할 입력 이미지 |
| `mask` | MASK | 예 | - | 이미지에서 채워야 할 영역을 정의하는 마스크 |
| `prompt` | STRING | 아니요 | - | 이미지 생성을 위한 프롬프트 (기본값: 빈 문자열) |
| `prompt_upsampling` | BOOLEAN | 아니요 | - | 프롬프트에 업샘플링을 수행할지 여부입니다. 활성화하면 프롬프트가 자동으로 수정되어 더 창의적인 생성을 유도하지만, 결과는 비결정적입니다(동일한 시드로도 완전히 동일한 결과가 생성되지 않습니다). (기본값: false) |
| `guidance` | FLOAT | 아니요 | 1.5-100 | 이미지 생성 과정의 안내 강도 (기본값: 60) |
| `steps` | INT | 아니요 | 15-50 | 이미지 생성 과정의 단계 수 (기본값: 50) |
| `seed` | INT | 아니요 | 0-18446744073709551615 | 노이즈 생성에 사용되는 난수 시드입니다. (기본값: 0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output_image` | IMAGE | 프롬프트에 따라 마스크 영역이 채워진 생성된 이미지 |

---
**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`
