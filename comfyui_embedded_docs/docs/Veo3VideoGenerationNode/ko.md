> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/ko.md)

Google의 Veo 3 API를 사용하여 텍스트 프롬프트에서 비디오를 생성합니다. 이 노드는 veo-3.0-generate-001과 veo-3.0-fast-generate-001 두 가지 Veo 3 모델을 지원합니다. 오디오 생성과 고정된 8초 길이를 포함한 Veo 3 특화 기능으로 기본 Veo 노드를 확장합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 비디오에 대한 텍스트 설명 (기본값: "") |
| `aspect_ratio` | COMBO | 예 | "16:9"<br>"9:16" | 출력 비디오의 화면비 (기본값: "16:9") |
| `negative_prompt` | STRING | 아니오 | - | 비디오에서 피해야 할 내용을 안내하는 부정 텍스트 프롬프트 (기본값: "") |
| `duration_seconds` | INT | 아니오 | 8-8 | 출력 비디오의 길이(초) (Veo 3은 8초만 지원함) (기본값: 8) |
| `enhance_prompt` | BOOLEAN | 아니오 | - | AI 지원으로 프롬프트를 향상시킬지 여부 (기본값: True) |
| `person_generation` | COMBO | 아니오 | "ALLOW"<br>"BLOCK" | 비디오에서 사람 생성 허용 여부 (기본값: "ALLOW") |
| `seed` | INT | 아니오 | 0-4294967295 | 비디오 생성을 위한 시드 (0은 무작위) (기본값: 0) |
| `image` | IMAGE | 아니오 | - | 비디오 생성을 안내하는 선택적 참조 이미지 |
| `model` | COMBO | 아니오 | "veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | 비디오 생성에 사용할 Veo 3 모델 (기본값: "veo-3.0-generate-001") |
| `generate_audio` | BOOLEAN | 아니오 | - | 비디오용 오디오 생성. 모든 Veo 3 모델에서 지원됩니다. (기본값: False) |

**참고:** `duration_seconds` 매개변수는 모든 Veo 3 모델에서 8초로 고정되어 있으며 변경할 수 없습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 파일 |