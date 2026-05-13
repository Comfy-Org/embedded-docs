> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/ko.md)

# 개요

Google Veo 2 API를 사용하여 텍스트 프롬프트로 비디오를 생성합니다. 이 노드는 텍스트 설명과 선택적 이미지 입력을 바탕으로 비디오를 제작할 수 있으며, 화면 비율, 재생 시간 등의 매개변수를 제어할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 비디오에 대한 텍스트 설명 (기본값: 비어 있음) |
| `aspect_ratio` | COMBO | 예 | "16:9"<br>"9:16" | 출력 비디오의 화면 비율 (기본값: "16:9") |
| `negative_prompt` | STRING | 아니요 | - | 비디오에서 제외할 내용을 안내하는 부정 텍스트 프롬프트 (기본값: 비어 있음) |
| `duration_seconds` | INT | 아니요 | 5-8 | 출력 비디오의 재생 시간(초) (기본값: 5) |
| `enhance_prompt` | BOOLEAN | 아니요 | - | AI 지원으로 프롬프트를 향상할지 여부 (기본값: True). 고급 매개변수입니다. |
| `person_generation` | COMBO | 아니요 | "ALLOW"<br>"BLOCK" | 비디오에 사람 생성을 허용할지 여부 (기본값: "ALLOW"). 고급 매개변수입니다. |
| `seed` | INT | 아니요 | 0-4294967295 | 비디오 생성을 위한 시드 (0은 무작위) (기본값: 0). 고급 매개변수입니다. |
| `image` | IMAGE | 아니요 | - | 비디오 생성을 안내하는 선택적 참조 이미지 |
| `model` | COMBO | 아니요 | "veo-2.0-generate-001" | 비디오 생성에 사용할 Veo 2 모델 (기본값: "veo-2.0-generate-001") |

**참고:** `generate_audio` 매개변수는 Veo 3.0 모델에서만 사용 가능하며, 선택한 모델에 따라 노드에서 자동으로 처리됩니다. Veo 3.0 모델을 사용할 때는 `enhance_prompt` 매개변수가 강제로 True로 설정됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 파일 |

---
**Source fingerprint (SHA-256):** `1a8b8ffe82fce32566815248f4a2434a1b865b5e5651935ccb3b92c7e38adee9`
