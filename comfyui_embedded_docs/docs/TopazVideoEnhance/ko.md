> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/ko.md)

Topaz Video Enhance 노드는 외부 API를 사용하여 비디오 품질을 향상시킵니다. 비디오 해상도를 업스케일하고, 프레임 보간을 통해 프레임 속도를 높이며, 압축을 적용할 수 있습니다. 이 노드는 입력 MP4 비디오를 처리하고 선택된 설정에 따라 향상된 버전을 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 예 | - | 향상시킬 입력 비디오 파일입니다. |
| `upscaler_enabled` | BOOLEAN | 예 | - | 비디오 업스케일링 기능을 활성화 또는 비활성화합니다 (기본값: True). |
| `upscaler_model` | COMBO | 예 | `"Proteus v3"`<br>`"Artemis v13"`<br>`"Artemis v14"`<br>`"Artemis v15"`<br>`"Gaia v6"`<br>`"Theia v3"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight (Astra) Optimized"`<br>`"Starlight (Astra) Balanced"`<br>`"Starlight (Astra) Quality"`<br>`"Starlight (Astra) Speed"` | 비디오 업스케일링에 사용되는 AI 모델입니다. |
| `upscaler_resolution` | COMBO | 예 | `"FullHD (1080p)"`<br>`"4K (2160p)"` | 업스케일된 비디오의 목표 해상도입니다. |
| `upscaler_creativity` | COMBO | 아니요 | `"low"`<br>`"middle"`<br>`"high"` | 창의성 수준 (Starlight (Astra) Creative에만 적용됨). (기본값: "low") |
| `interpolation_enabled` | BOOLEAN | 아니요 | - | 프레임 보간 기능을 활성화 또는 비활성화합니다 (기본값: False). |
| `interpolation_model` | COMBO | 아니요 | `"apo-8"` | 프레임 보간에 사용되는 모델입니다 (기본값: "apo-8"). |
| `interpolation_slowmo` | INT | 아니요 | 1 ~ 16 | 입력 비디오에 적용되는 슬로우 모션 계수입니다. 예를 들어, 2는 출력을 두 배 느리게 만들고 지속 시간을 두 배로 늘립니다. (기본값: 1) |
| `interpolation_frame_rate` | INT | 아니요 | 15 ~ 240 | 출력 프레임 속도입니다. (기본값: 60) |
| `interpolation_duplicate` | BOOLEAN | 아니요 | - | 입력에서 중복 프레임을 분석하여 제거합니다. (기본값: False) |
| `interpolation_duplicate_threshold` | FLOAT | 아니요 | 0.001 ~ 0.1 | 중복 프레임 감지 민감도입니다. (기본값: 0.01) |
| `dynamic_compression_level` | COMBO | 아니요 | `"Low"`<br>`"Mid"`<br>`"High"` | CQP 수준입니다. (기본값: "Low") |

**참고:** 최소한 하나의 향상 기능이 활성화되어야 합니다. `upscaler_enabled`와 `interpolation_enabled`가 모두 `False`로 설정되면 노드에서 오류가 발생합니다. 입력 비디오는 MP4 형식이어야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `video` | VIDEO | 향상된 출력 비디오 파일입니다. |
