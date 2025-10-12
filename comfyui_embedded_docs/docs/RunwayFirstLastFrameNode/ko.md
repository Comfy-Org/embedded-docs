> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/ko.md)

Runway First-Last-Frame to Video 노드는 첫 번째와 마지막 키프레임을 텍스트 프롬프트와 함께 업로드하여 비디오를 생성합니다. Runway의 Gen-3 모델을 사용하여 제공된 시작 프레임과 종료 프레임 사이의 부드러운 전환을 만듭니다. 이는 종료 프레임이 시작 프레임과 크게 다른 복잡한 전환에 특히 유용합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | N/A | 생성을 위한 텍스트 프롬프트 (기본값: 빈 문자열) |
| `start_frame` | IMAGE | 예 | N/A | 비디오에 사용할 시작 프레임 |
| `end_frame` | IMAGE | 예 | N/A | 비디오에 사용할 종료 프레임. gen3a_turbo에서만 지원됩니다. |
| `duration` | COMBO | 예 | 사용 가능한 여러 옵션 | 사용 가능한 Duration 옵션 중에서 비디오 길이 선택 |
| `ratio` | COMBO | 예 | 사용 가능한 여러 옵션 | 사용 가능한 RunwayGen3aAspectRatio 옵션 중에서 화면비 선택 |
| `seed` | INT | 아니오 | 0-4294967295 | 생성을 위한 랜덤 시드 (기본값: 0) |

**매개변수 제약 조건:**

- `prompt`는 최소 1자 이상을 포함해야 합니다
- `start_frame`과 `end_frame` 모두 최대 크기가 7999x7999 픽셀이어야 합니다
- `start_frame`과 `end_frame` 모두 화면비가 0.5에서 2.0 사이여야 합니다
- `end_frame` 매개변수는 gen3a_turbo 모델을 사용할 때만 지원됩니다

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 시작 프레임과 종료 프레임 사이를 전환하는 생성된 비디오 |
