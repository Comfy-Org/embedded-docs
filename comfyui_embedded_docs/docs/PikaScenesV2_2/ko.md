> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/ko.md)

PikaScenes v2.2 노드는 여러 이미지를 결합하여 모든 입력 이미지의 객체가 포함된 비디오를 생성합니다. 최대 다섯 개의 서로 다른 이미지를 재료로 업로드하고, 이를 매끄럽게 혼합한 고품질 비디오를 생성할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | 예 | - | 생성할 내용에 대한 텍스트 설명 |
| `negative_prompt` | STRING | 예 | - | 생성에서 피해야 할 내용에 대한 텍스트 설명 |
| `seed` | INT | 예 | - | 생성을 위한 랜덤 시드 값 |
| `resolution` | STRING | 예 | - | 비디오의 출력 해상도 |
| `duration` | INT | 예 | - | 생성된 비디오의 지속 시간 |
| `ingredients_mode` | COMBO | 아니오 | "creative"<br>"precise" | 재료 결합 모드 (기본값: "creative") |
| `aspect_ratio` | FLOAT | 아니오 | 0.4 - 2.5 | 종횡비 (너비 / 높이) (기본값: 1.778) |
| `image_ingredient_1` | IMAGE | 아니오 | - | 비디오 생성에 재료로 사용될 이미지 |
| `image_ingredient_2` | IMAGE | 아니오 | - | 비디오 생성에 재료로 사용될 이미지 |
| `image_ingredient_3` | IMAGE | 아니오 | - | 비디오 생성에 재료로 사용될 이미지 |
| `image_ingredient_4` | IMAGE | 아니오 | - | 비디오 생성에 재료로 사용될 이미지 |
| `image_ingredient_5` | IMAGE | 아니오 | - | 비디오 생성에 재료로 사용될 이미지 |

**참고:** 최대 5개의 이미지 재료를 제공할 수 있지만, 비디오를 생성하려면 최소한 하나의 이미지가 필요합니다. 노드는 제공된 모든 이미지를 사용하여 최종 비디오 구성을 생성합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 모든 입력 이미지를 결합하여 생성된 비디오 |