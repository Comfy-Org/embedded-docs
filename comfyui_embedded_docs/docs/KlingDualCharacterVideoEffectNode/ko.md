> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/ko.md)

Kling Dual Character Video Effect Node는 선택된 장면을 기반으로 특수 효과가 적용된 비디오를 생성합니다. 두 개의 이미지를 입력받아 첫 번째 이미지를 왼쪽에, 두 번째 이미지를 오른쪽에 배치한 합성 비디오를 만듭니다. 선택된 효과 장면에 따라 다양한 시각적 효과가 적용됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image_left` | IMAGE | 예 | - | 왼쪽 이미지 |
| `image_right` | IMAGE | 예 | - | 오른쪽 이미지 |
| `effect_scene` | COMBO | 예 | 여러 옵션 사용 가능 | 비디오 생성에 적용할 특수 효과 장면 유형 |
| `model_name` | COMBO | 아니오 | 여러 옵션 사용 가능 | 캐릭터 효과에 사용할 모델 (기본값: "kling-v1") |
| `mode` | COMBO | 아니오 | 여러 옵션 사용 가능 | 비디오 생성 모드 (기본값: "std") |
| `duration` | COMBO | 예 | 여러 옵션 사용 가능 | 생성된 비디오의 지속 시간 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 이중 캐릭터 효과가 적용된 생성된 비디오 |
| `duration` | STRING | 생성된 비디오의 지속 시간 정보 |