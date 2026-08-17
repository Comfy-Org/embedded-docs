# 잠재 데이터 저장

SaveLatent 노드는 잠재 샘플을 디스크에 `.latent` 파일로 저장하여 나중에 사용하거나 공유할 수 있도록 합니다. 지정된 파일 이름 접두사를 사용하여 출력 폴더에 잠재 텐서 데이터를 기록하고, 프롬프트 정보와 같은 선택적 메타데이터를 포함합니다. 또한 이 노드는 원본 잠재 샘플을 변경하지 않은 채 반환하므로 워크플로우에서 계속 사용할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `samples` | 디스크에 저장할 잠재 샘플입니다. | LATENT | 예 | - |
| `filename_prefix` | 출력 파일 이름과 하위 폴더 경로를 생성하는 데 사용되는 접두사입니다. (기본값: "latents/ComfyUI") | STRING | 예 | - |
| `prompt` | 저장된 파일에 JSON 메타데이터로 기록되는 워크플로우 프롬프트 데이터입니다. (숨겨진 입력으로, 자동으로 제공됩니다.) | PROMPT | 아니요 | - |
| `extra_pnginfo` | 저장된 파일에 JSON으로 기록되는 추가 워크플로우 메타데이터입니다. (숨겨진 입력으로, 자동으로 제공됩니다.) | EXTRA_PNGINFO | 아니요 | - |

참고: ComfyUI가 `--disable-metadata` 인수로 시작되지 않는 한 메타데이터는 저장된 `.latent` 파일에 기록됩니다. 저장된 파일은 `{filename}_{5자리 카운터}_.latent` 패턴으로 이름이 지정됩니다(예: `ComfyUI_00001_.latent`).

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `samples` | 변경되지 않은 원본 잠재 샘플입니다. | LATENT |
| `ui` | 저장된 잠재 파일의 파일 위치 세부 정보(파일 이름, 하위 폴더 및 출력 유형)입니다. | UI |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/ko.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
