> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/ko.md)

# ByteDance Seedance 2.0 참조-비디오 노드

ByteDance Seedance 2.0 참조-비디오 노드는 Seedance 2.0 AI 모델을 사용하여 텍스트 프롬프트와 제공된 참조 자료를 기반으로 비디오를 생성, 편집 또는 확장합니다. 이미지, 비디오 및 오디오를 참조 자료로 사용하여 생성 과정을 안내할 수 있으며, 비디오 편집 및 확장과 같은 작업을 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | 사용할 AI 모델입니다. Seedance 2.0은 최대 품질을 위한 모델이며, Seedance 2.0 Fast는 속도에 최적화된 모델입니다. 모델을 선택하면 `prompt`, `resolution`, `duration`, `ratio`, `generate_audio`에 대한 추가 필수 입력과 `reference_images`, `reference_videos`, `reference_audios`, `reference_assets`, `auto_downscale`에 대한 선택적 입력이 표시됩니다. |
| `seed` | INT | 아니요 | 0 ~ 2147483647 | 노드를 다시 실행할지 여부를 제어하는 데 사용되는 숫자입니다. 시드 값과 관계없이 결과는 비결정적입니다(기본값: 0). |
| `watermark` | BOOLEAN | 아니요 | `True` / `False` | 생성된 비디오에 워터마크를 추가할지 여부입니다(기본값: False). |

**중요 제약 사항:**
*   노드가 작동하려면 최소 하나의 참조 이미지 또는 비디오(`reference_images`, `reference_videos` 또는 `reference_assets` 입력을 통해 제공)가 필요합니다.
*   각 참조 비디오는 최소 1.8초 길이여야 합니다. 모든 참조 비디오의 총 길이는 15.1초를 초과할 수 없습니다.
*   각 참조 오디오 클립은 최소 1.8초 길이여야 합니다. 모든 참조 오디오의 총 길이는 15.1초를 초과할 수 없습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `video` | VIDEO | 생성된 비디오 파일입니다. |