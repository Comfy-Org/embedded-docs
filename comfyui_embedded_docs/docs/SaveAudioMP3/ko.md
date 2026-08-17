# 오디오 저장 (MP3)

SaveAudioMP3 노드는 오디오 데이터를 MP3 파일로 저장합니다. 오디오 입력을 받아 사용자 지정 가능한 파일 이름 접두사와 품질 설정으로 출력 디렉터리에 저장합니다. 이 노드는 더 이상 사용되지 않으며 향후 버전에서 제거될 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `audio` | MP3 파일로 저장할 오디오 데이터 | AUDIO | 예 | - |
| `filename_prefix` | 출력 파일 이름의 접두사(기본값: "audio/ComfyUI") | STRING | 아니요 | - |
| `quality` | MP3 인코딩 품질 설정(기본값: "V0"). V0는 고품질을 위해 가변 비트레이트를 사용하며, 128k와 320k는 각각 128kbps와 320kbps의 고정 비트레이트를 사용합니다 | COMBO | 아니요 | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | 시스템에서 자동으로 제공되는 내부 프롬프트 데이터 | PROMPT | 아니요 | - |
| `extra_pnginfo` | 시스템에서 자동으로 제공되는 추가 PNG 정보 | EXTRA_PNGINFO | 아니요 | - |

**참고:** `audio` 입력이 None인 경우(예: 원본 비디오에 오디오 트랙이 없는 경우), 노드는 ValueError를 발생시킵니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `audio` | MP3 파일로 저장된 오디오 데이터 | AUDIO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/ko.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
