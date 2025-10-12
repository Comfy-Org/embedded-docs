> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/ko.md)

Moonvalley Marey Video to Video 노드는 입력된 동영상을 텍스트 설명을 기반으로 새로운 동영상으로 변환합니다. Moonvalley API를 사용하여 원본 동영상의 동작이나 자세 특성을 유지하면서 사용자의 프롬프트와 일치하는 동영상을 생성합니다. 텍스트 프롬프트와 다양한 생성 매개변수를 통해 출력 동영상의 스타일과 내용을 제어할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 생성할 동영상을 설명하는 텍스트 (여러 줄 입력 가능) |
| `negative_prompt` | STRING | 아니오 | - | 부정적 프롬프트 텍스트 (기본값: 다양한 부정적 설명어 목록) |
| `seed` | INT | 예 | 0-4294967295 | 랜덤 시드 값 (기본값: 9) |
| `video` | VIDEO | 예 | - | 출력 동영상을 생성하는 데 사용되는 참조 동영상. 최소 5초 이상이어야 합니다. 5초보다 긴 동영상은 자동으로 잘립니다. MP4 형식만 지원됩니다. |
| `control_type` | COMBO | 아니오 | "Motion Transfer"<br>"Pose Transfer" | 제어 유형 선택 (기본값: "Motion Transfer") |
| `motion_intensity` | INT | 아니오 | 0-100 | control_type이 'Motion Transfer'일 때만 사용됨 (기본값: 100) |
| `steps` | INT | 예 | 1-100 | 추론 단계 수 (기본값: 33) |

**참고:** `motion_intensity` 매개변수는 `control_type`이 "Motion Transfer"로 설정된 경우에만 적용됩니다. "Pose Transfer"를 사용할 때는 이 매개변수가 무시됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 동영상 출력 |