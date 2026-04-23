> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/en.md)

이 노드는 ByteDance의 Seedance 2.0 모델을 사용하여 비디오를 생성합니다. 텍스트 프롬프트와 필수 첫 번째 프레임 이미지를 기반으로 비디오를 만듭니다. 선택적으로 마지막 프레임 이미지를 제공하여 비디오 시퀀스의 종료를 안내할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | 비디오 생성에 사용할 모델입니다. Seedance 2.0은 최고 품질을 위한 모델이며, Seedance 2.0 Fast는 속도에 최적화된 모델입니다. 모델을 선택하면 `prompt`, `resolution`, `ratio`, `duration`, `generate_audio`에 대한 추가 입력이 표시됩니다. |
| `first_frame` | IMAGE | 아니요 | - | 비디오의 첫 번째 프레임으로 사용할 이미지입니다. |
| `last_frame` | IMAGE | 아니요 | - | 비디오의 마지막 프레임으로 사용할 이미지입니다. |
| `first_frame_asset_id` | STRING | 아니요 | - | 첫 번째 프레임으로 사용할 Seedance asset_id입니다. `first_frame` 이미지 입력과 동시에 사용할 수 없습니다. 기본값은 빈 문자열입니다. |
| `last_frame_asset_id` | STRING | 아니요 | - | 마지막 프레임으로 사용할 Seedance asset_id입니다. `last_frame` 이미지 입력과 동시에 사용할 수 없습니다. 기본값은 빈 문자열입니다. |
| `seed` | INT | 아니요 | 0 ~ 2147483647 | 시드 값입니다. 이 시드를 변경하면 노드가 다시 실행되지만 결과는 비결정적입니다. 기본값은 0입니다. |
| `watermark` | BOOLEAN | 아니요 | - | 생성된 비디오에 워터마크를 추가할지 여부입니다. 기본값은 False입니다. |

**매개변수 제약 조건:**
*   `first_frame` 이미지 **또는** `first_frame_asset_id` 중 **하나**를 반드시 제공해야 합니다. 둘 다 제공하면 오류가 발생합니다.
*   동일한 프레임에 대해 `last_frame` 이미지와 `last_frame_asset_id`를 모두 제공할 수 없습니다.
*   `model` 입력은 동적 콤보입니다. 모델을 선택한 후에는 표시된 `prompt` 필드(텍스트 설명)를 반드시 입력하고 다른 표시된 매개변수(`resolution`, `ratio`, `duration`, `generate_audio`)를 구성해야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오입니다. |