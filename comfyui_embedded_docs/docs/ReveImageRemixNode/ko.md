> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/ko.md)

# Reve Image Remix 노드

이 문서는 AI로 생성되었습니다. 오류를 발견하시거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/en.md)

Reve Image Remix 노드는 Reve API를 사용하여 새 이미지를 생성합니다. 하나 이상의 참조 이미지와 텍스트 프롬프트를 결합하여 제공된 설명에 기반한 새로운 리믹스 이미지를 만듭니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `reference_images` | IMAGE | 예 | 1~6개 이미지 | 리믹스의 기준으로 사용할 하나 이상의 참조 이미지입니다. 1~6개의 이미지를 추가할 수 있습니다. |
| `prompt` | STRING | 예 | 1~2560자 | 원하는 이미지에 대한 텍스트 설명입니다. XML `<img>` 태그를 사용하여 특정 이미지를 인덱스로 참조할 수 있습니다(예: `<img>0</img>`, `<img>1</img>`). |
| `model` | COMBO | 예 | `reve-remix@20250915`<br>`reve-remix-fast@20251030` | 리믹싱에 사용할 모델 버전입니다. 각 모델 옵션에는 설정 가능한 종횡비와 테스트 시간 스케일링이 포함됩니다. |
| `upscale` | COMBO | 아니요 | `"disabled"`<br>`"enabled"` | 생성된 이미지의 업스케일 여부를 제어합니다. 활성화하면 업스케일 배율을 선택할 수 있습니다. |
| `remove_background` | BOOLEAN | 아니요 | `true`<br>`false` | 활성화하면 생성된 이미지에서 배경 제거를 시도합니다. |
| `seed` | INT | 아니요 | 0~2147483647 | 시드 값입니다. 이 값을 변경하면 노드가 다시 실행되지만 결과는 비결정적입니다. (기본값: 0) |

**참고:** `model` 매개변수는 `aspect_ratio`(예: "auto", "16:9", "1:1") 및 `test_time_scaling`에 대한 중첩 설정을 포함하는 동적 콤보입니다. `upscale` 매개변수를 "enabled"로 설정하면 중첩된 `upscale_factor` 설정이 표시됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | Reve 리믹스 프로세스로 생성된 새 이미지입니다. |