> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/ko.md)

Kling Single Image Video Effect Node는 단일 참조 이미지를 기반으로 다양한 특수 효과가 적용된 비디오를 생성합니다. 다양한 시각 효과와 장면을 적용하여 정적 이미지를 동적인 비디오 콘텐츠로 변환합니다. 이 노드는 원하는 시각적 결과를 달성하기 위해 다양한 효과 장면, 모델 옵션 및 비디오 지속 시간을 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `이미지` | IMAGE | 예 | - | 참조 이미지. URL 또는 Base64 인코딩 문자열 (data:image 접두사 없음). 파일 크기는 10MB를 초과할 수 없으며, 해상도는 300*300px 이상이어야 하고, 화면비는 1:2.5 ~ 2.5:1 사이여야 합니다. |
| `효과 장면` | COMBO | 예 | KlingSingleImageEffectsScene의 옵션들 | 비디오 생성에 적용할 특수 효과 장면의 유형 |
| `모델 명` | COMBO | 예 | KlingSingleImageEffectModelName의 옵션들 | 비디오 효과 생성에 사용할 특정 모델 |
| `길이` | COMBO | 예 | KlingVideoGenDuration의 옵션들 | 생성된 비디오의 길이 |

**참고:** `effect_scene`, `model_name`, `duration`의 구체적인 옵션은 각각의 열거형 클래스(KlingSingleImageEffectsScene, KlingSingleImageEffectModelName, KlingVideoGenDuration)에서 사용 가능한 값에 따라 결정됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `비디오 ID` | VIDEO | 효과가 적용된 생성된 비디오 |
| `길이` | STRING | 생성된 비디오의 고유 식별자 |
| `길이` | STRING | 생성된 비디오의 지속 시간 |
