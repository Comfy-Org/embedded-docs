# 마스크 미리보기

MaskPreview 노드는 마스크 데이터를 ComfyUI 인터페이스에서 직접 시각적으로 미리 볼 수 있게 해주므로, 워크플로우 중에 마스크를 검사할 수 있습니다. 이 노드는 ComfyUI 출력 디렉터리에 저장하지 않고 미리 보기를 표시하며, 마스크를 출력으로 그대로 전달합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `mask` | 미리 볼 마스크 데이터입니다. | MASK | 예 | - |
| `filename_prefix` | 출력 파일 이름의 접두사입니다. (기본값: "ComfyUI") | STRING | 아니요 | - |
| `prompt` | 메타데이터용 프롬프트 정보입니다. (자동으로 제공됩니다) | PROMPT | 아니요 | - |
| `extra_pnginfo` | 메타데이터용 추가 PNG 정보입니다. (자동으로 제공됩니다) | EXTRA_PNGINFO | 아니요 | - |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `mask` | 미리 보기가 완료된 마스크 데이터로, 변경 없이 그대로 전달됩니다. | MASK |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/ko.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
