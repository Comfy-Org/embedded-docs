> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/ko.md)

# Moonvalley 비디오-투-비디오 노드

Moonvalley Marey 비디오-투-비디오 노드는 입력 비디오를 텍스트 설명에 기반하여 새로운 비디오로 변환합니다. Moonvalley API를 사용하여 사용자의 프롬프트와 일치하면서도 원본 비디오의 움직임이나 포즈 특성을 보존하는 비디오를 생성합니다. 텍스트 프롬프트와 다양한 생성 매개변수를 통해 출력 비디오의 스타일과 내용을 제어할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 생성할 비디오를 설명하는 텍스트 (여러 줄 입력 가능) |
| `negative_prompt` | STRING | 아니요 | - | 네거티브 프롬프트 텍스트 (기본값: 광범위한 네거티브 설명 목록) |
| `seed` | INT | 예 | 0 ~ 4294967295 | 랜덤 시드 값 (기본값: 9) |
| `video` | VIDEO | 예 | - | 출력 비디오 생성에 사용되는 참조 비디오. 최소 5초 이상이어야 합니다. 5초를 초과하는 비디오는 자동으로 잘립니다. MP4 형식만 지원됩니다. |
| `control_type` | COMBO | 아니요 | "Motion Transfer"<br>"Pose Transfer" | 제어 유형 선택 (기본값: "Motion Transfer") |
| `motion_intensity` | INT | 아니요 | 0 ~ 100 | control_type이 "Motion Transfer"인 경우에만 사용됨 (기본값: 100) |
| `steps` | INT | 예 | 1 ~ 100 | 추론 단계 수 (기본값: 33) |

**참고:** `motion_intensity` 매개변수는 `control_type`이 "Motion Transfer"로 설정된 경우에만 적용됩니다. "Pose Transfer"를 사용하는 경우 이 매개변수는 무시됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 출력 |

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
