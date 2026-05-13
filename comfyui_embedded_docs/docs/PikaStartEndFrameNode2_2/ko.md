> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/ko.md)

PikaFrames v2.2 노드는 첫 번째 프레임과 마지막 프레임을 결합하여 비디오를 생성합니다. 시작점과 끝점을 정의하는 두 개의 이미지를 업로드하면, AI가 두 이미지 사이의 부드러운 전환을 생성하여 완전한 비디오를 만들어냅니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image_start` | IMAGE | 예 | - | 결합할 첫 번째 이미지입니다. |
| `image_end` | IMAGE | 예 | - | 결합할 마지막 이미지입니다. |
| `prompt_text` | STRING | 예 | - | 원하는 비디오 콘텐츠를 설명하는 텍스트 프롬프트입니다. |
| `negative_prompt` | STRING | 예 | - | 비디오에서 제외할 내용을 설명하는 텍스트입니다. |
| `seed` | INT | 예 | - | 생성 일관성을 위한 무작위 시드 값입니다. |
| `resolution` | STRING | 예 | - | 출력 비디오 해상도입니다. |
| `duration` | INT | 예 | - | 생성된 비디오의 길이입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | AI 전환을 통해 시작 프레임과 끝 프레임을 결합하여 생성된 비디오입니다. |

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
