> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/ko.md)

# ByteDance Seedream 노드

ByteDance Seedream 4.5 및 5.0 노드는 최대 4K 해상도에서 통합된 텍스트-이미지 생성 및 정밀한 단일 문장 편집 기능을 제공합니다. 텍스트 프롬프트로 새 이미지를 생성하거나 텍스트 명령어를 사용하여 기존 이미지를 편집할 수 있습니다. 이 노드는 단일 이미지 생성과 여러 관련 이미지의 순차적 생성을 모두 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | 예 | 설명 참조 | 생성에 사용할 Seedream 모델입니다. 사용 가능한 모델로는 seedream-4-0, seedream-4-5 및 seedream-5-0 변형이 있습니다. |
| `prompt` | STRING | 예 | - | 이미지를 생성하거나 편집하기 위한 텍스트 프롬프트입니다. 최소 1자 이상이어야 합니다. |
| `image` | IMAGE | 아니요 | - | 이미지-이미지 생성을 위한 입력 이미지입니다. 단일 또는 다중 참조 생성을 위한 참조 이미지입니다. 대부분의 모델에서 최대 10개의 참조 이미지, seedream-5-0-260128의 경우 최대 14개입니다. |
| `size_preset` | STRING | 아니요 | 여러 옵션 사용 가능 | 권장 크기를 선택합니다. 아래의 너비와 높이를 사용하려면 사용자 정의를 선택하세요. 기본값: RECOMMENDED_PRESETS_SEEDREAM_4의 첫 번째 프리셋. |
| `width` | INT | 아니요 | 1024 ~ 6240 (2단위) | 이미지의 사용자 정의 너비입니다. `size_preset`이 `Custom`으로 설정된 경우에만 값이 적용됩니다. 기본값: 2048. |
| `height` | INT | 아니요 | 1024 ~ 4992 (2단위) | 이미지의 사용자 정의 높이입니다. `size_preset`이 `Custom`으로 설정된 경우에만 값이 적용됩니다. 기본값: 2048. |
| `sequential_image_generation` | STRING | 아니요 | "disabled"<br>"auto" | 그룹 이미지 생성 모드입니다. "disabled"는 단일 이미지를 생성합니다. "auto"는 모델이 여러 관련 이미지(예: 스토리 장면, 캐릭터 변형)를 생성할지 여부를 결정합니다. 기본값: "disabled". |
| `max_images` | INT | 아니요 | 1 ~ 15 (1단위) | sequential_image_generation='auto'일 때 생성할 최대 이미지 수입니다. 총 이미지(입력 + 생성)는 15개를 초과할 수 없습니다. 기본값: 1. |
| `seed` | INT | 아니요 | 0 ~ 2147483647 (1단위) | 생성에 사용할 시드입니다. 기본값: 0. |
| `watermark` | BOOLEAN | 아니요 | - | 이미지에 "AI 생성" 워터마크를 추가할지 여부입니다. 기본값: False. |
| `fail_on_partial` | BOOLEAN | 아니요 | - | 활성화된 경우 요청된 이미지가 누락되거나 오류가 발생하면 실행을 중단합니다. 기본값: True. |

**매개변수 제약 조건 참고 사항:**
- 최소 이미지 해상도는 선택한 모델에 따라 다릅니다: seedream-4-5 및 seedream-5-0 모델의 경우 3.68MP, seedream-4-0 모델의 경우 0.92MP입니다.
- 최대 이미지 해상도는 seedream-5-0 모델의 경우 10.4MP, 다른 모델의 경우 16.78MP입니다.
- 참조 이미지의 종횡비는 1:3에서 3:1 사이여야 합니다.
- `sequential_image_generation`이 "auto"로 설정된 경우 입력 이미지 수와 `max_images`의 합계가 15를 초과할 수 없습니다.
- `width` 및 `height` 매개변수는 `size_preset`이 "Custom"으로 설정된 경우에만 사용됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 입력 매개변수와 프롬프트를 기반으로 생성된 이미지입니다. 단일 이미지 텐서 또는 여러 이미지가 생성된 경우 이미지 텐서 배치를 반환합니다. |

---
**Source fingerprint (SHA-256):** `ce130246026e0f5036e137bea4e193f51097e0812459586dcbeb87ef01975630`
