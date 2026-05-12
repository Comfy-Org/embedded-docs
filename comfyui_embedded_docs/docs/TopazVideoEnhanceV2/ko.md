> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/ko.md)

# Topaz Video Enhance V2

**Topaz Video Enhance V2** 노드는 Topaz Labs의 AI 모델을 사용하여 비디오를 업스케일링하고 향상시킬 수 있습니다. 해상도를 높이고, 보간을 통해 프레임 속도를 조정하며, 창의적이거나 사실적인 향상 효과를 적용하여 비디오 영상에 새로운 생명을 불어넣을 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 예 | - | 처리할 입력 비디오입니다. MP4 컨테이너 형식이어야 합니다. |
| `upscaler_model` | COMBO | 예 | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` | 비디오 업스케일링에 사용되는 AI 모델입니다. "Disabled"를 선택하면 업스케일링이 적용되지 않습니다. |
| `upscaler_model.upscaler_resolution` | COMBO | 조건부 | `"FullHD (1080p)"`<br>`"4K (2160p)"` | 업스케일러의 대상 출력 해상도입니다. 업스케일러 모델이 선택된 경우("Disabled"가 아닌 경우) 이 매개변수가 필요합니다. |
| `upscaler_model.creativity` | FLOAT | 조건부 | 0.0 ~ 1.0 (단위 0.1) | 업스케일의 창의적 강도입니다. "Astra 2" 및 "Starlight (Astra) Creative" 모델에서만 사용 가능합니다. 기본값: Astra 2의 경우 0.5, Starlight Creative의 경우 "low"입니다. |
| `upscaler_model.prompt` | STRING | 아니요 | - | 선택적 설명(명령이 아닌) 장면 프롬프트입니다. "Astra 2" 모델에서만 사용 가능합니다. 설정 시 최대 500개의 입력 프레임(~30fps에서 약 15초)으로 제한됩니다. 기본값: 비어 있음. |
| `upscaler_model.sharp` | FLOAT | 아니요 | 0.0 ~ 1.0 (단위 0.01) | 사전 향상 선명도: 0.0=가우시안 블러, 0.5=통과(기본값), 1.0=USM 선명화입니다. "Astra 2" 모델에서만 사용 가능합니다. 기본값: 0.5. |
| `upscaler_model.realism` | FLOAT | 아니요 | 0.0 ~ 1.0 (단위 0.01) | 출력을 사진적 사실성 쪽으로 유도합니다. 모델 기본값을 사용하려면 0으로 두십시오. "Astra 2" 모델에서만 사용 가능합니다. 기본값: 0.0. |
| `interpolation_model` | COMBO | 예 | `"Disabled"`<br>`"apo-8"` | 프레임 보간에 사용되는 AI 모델입니다. "Disabled"를 선택하면 보간이 적용되지 않습니다. |
| `interpolation_model.interpolation_frame_rate` | INT | 조건부 | 15 ~ 240 | 출력 프레임 속도입니다. 보간 모델이 "apo-8"인 경우 필요합니다. 기본값: 60. |
| `interpolation_model.interpolation_slowmo` | INT | 아니요 | 1 ~ 16 | 입력 비디오에 적용되는 슬로우 모션 배율입니다. 예를 들어, 2는 출력을 두 배로 느리게 만들고 재생 시간을 두 배로 늘립니다. 기본값: 1. |
| `interpolation_model.interpolation_duplicate` | BOOLEAN | 아니요 | True/False | 입력에서 중복 프레임을 분석하여 제거합니다. 기본값: False. |
| `interpolation_model.interpolation_duplicate_threshold` | FLOAT | 아니요 | 0.001 ~ 0.1 (단위 0.001) | 중복 프레임 감지 민감도입니다. 기본값: 0.01. |
| `dynamic_compression_level` | COMBO | 아니요 | `"Low"`<br>`"Mid"`<br>`"High"` | 비디오 압축을 위한 CQP 수준입니다. 기본값: "Low". |

**중요 제약 사항:**
- `upscaler_model` 또는 `interpolation_model` 중 하나 이상이 활성화되어야 합니다("Disabled"가 아니어야 함). 그렇지 않으면 오류가 발생합니다.
- 입력 비디오는 MP4 컨테이너 형식이어야 합니다.
- 프롬프트가 있는 "Astra 2" 모델은 최대 500개의 입력 프레임(~30fps에서 약 15초)으로 제한됩니다. 프롬프트가 없으면 더 많은 프레임으로 제한됩니다.
- `upscaler_model`이 "Disabled"가 아닌 경우, `upscaler_resolution` 하위 매개변수가 필요합니다.
- `interpolation_model`이 "Disabled"가 아닌 경우, `interpolation_frame_rate` 하위 매개변수가 필요합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `video` | VIDEO | 선택한 업스케일링 및/또는 보간 필터를 적용한 후 향상된 비디오 출력입니다. |