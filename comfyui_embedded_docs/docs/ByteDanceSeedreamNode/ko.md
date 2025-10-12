> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/ko.md)

ByteDance Seedream 4 노드는 최대 4K 해상도로 통합 텍스트-이미지 생성 및 정밀한 단일 문장 편집 기능을 제공합니다. 텍스트 프롬프트로 새 이미지를 생성하거나 텍스트 지시를 사용하여 기존 이미지를 편집할 수 있습니다. 이 노드는 단일 이미지 생성과 여러 관련 이미지의 순차적 생성을 모두 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | "seedream-4-0-250828" | ["seedream-4-0-250828"] | 모델 이름 |
| `prompt` | STRING | STRING | "" | - | 이미지를 생성하거나 편집하기 위한 텍스트 프롬프트입니다. |
| `image` | IMAGE | IMAGE | - | - | 이미지-대-이미지 생성을 위한 입력 이미지입니다. 단일 또는 다중 참조 생성을 위한 1-10개 이미지 목록입니다. |
| `size_preset` | STRING | COMBO | RECOMMENDED_PRESETS_SEEDREAM_4의 첫 번째 프리셋 | RECOMMENDED_PRESETS_SEEDREAM_4의 모든 레이블 | 권장 크기를 선택하세요. 아래 너비와 높이를 사용하려면 Custom을 선택하세요. |
| `width` | INT | INT | 2048 | 1024-4096 (간격 64) | 이미지의 사용자 정의 너비입니다. 이 값은 `size_preset`이 `Custom`으로 설정된 경우에만 작동합니다. |
| `height` | INT | INT | 2048 | 1024-4096 (간격 64) | 이미지의 사용자 정의 높이입니다. 이 값은 `size_preset`이 `Custom`으로 설정된 경우에만 작동합니다. |
| `sequential_image_generation` | STRING | COMBO | "disabled" | ["disabled", "auto"] | 그룹 이미지 생성 모드입니다. 'disabled'는 단일 이미지를 생성합니다. 'auto'는 모델이 여러 관련 이미지(예: 스토리 장면, 캐릭터 변형)를 생성할지 여부를 결정하도록 합니다. |
| `max_images` | INT | INT | 1 | 1-15 | sequential_image_generation='auto'일 때 생성할 최대 이미지 수입니다. 총 이미지 수(입력 + 생성)는 15개를 초과할 수 없습니다. |
| `seed` | INT | INT | 0 | 0-2147483647 | 생성에 사용할 시드 값입니다. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 이미지에 "AI 생성" 워터마크를 추가할지 여부입니다. |
| `fail_on_partial` | BOOLEAN | BOOLEAN | True | - | 활성화된 경우, 요청된 이미지 중 일부가 누락되거나 오류가 반환되면 실행을 중단합니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 입력 매개변수와 프롬프트를 기반으로 생성된 이미지입니다. |
