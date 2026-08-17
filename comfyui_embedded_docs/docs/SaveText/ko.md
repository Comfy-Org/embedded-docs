# 텍스트 저장

Save Text 노드는 텍스트 내용을 출력 디렉터리의 파일에 저장합니다. .txt, .csv, .md 또는 .json 형식으로 저장할 수 있으며, 유효한 JSON이 제공되면 자동으로 JSON 예쁘게 출력(pretty-printing)을 처리합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `text` | 파일에 저장할 텍스트 내용입니다. 이 입력은 다른 노드에서 연결해야 합니다. | STRING | 예 | - |
| `filename_prefix` | 출력 파일 이름의 접두사입니다. 기존 파일을 덮어쓰지 않도록 5자리 카운터가 추가됩니다 (기본값: "ComfyUI"). | STRING | 아니요 | - |
| `format` | 텍스트를 저장할 파일 형식입니다 (기본값: "txt"). "json"을 선택하면 유효한 JSON 텍스트가 2칸 들여쓰기로 예쁘게 출력되며, 그 외의 경우에는 텍스트가 원래대로 저장됩니다. | COMBO | 아니요 | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `text` | 파일에 저장된 원본 텍스트 내용입니다 | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/ko.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
