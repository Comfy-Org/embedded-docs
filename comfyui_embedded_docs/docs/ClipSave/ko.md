# CLIP 저장

`CLIPSave` 노드는 CLIP 텍스트 인코더 모델을 SafeTensors 형식으로 디스크에 저장합니다. 이 노드는 고급 모델 병합 워크플로우를 위해 설계되었으며, 모델의 내부 구조를 기반으로 CLIP 모델을 구성 요소(예: CLIP-L, CLIP-G 또는 T5XXL)로 자동 분리하고 각 구성 요소를 별도의 파일로 저장합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip` | 저장할 CLIP 모델입니다. | CLIP | 예 | - |
| `filename_prefix` | 저장될 파일의 접두사 경로와 파일 이름입니다. 노드는 구성 요소 접미사(예: `_clip_l`, `_clip_g`)와 카운터를 추가하여 고유한 파일 이름을 생성합니다(기본값: `clip/ComfyUI`). | STRING | 예 | - |
| `prompt` | 출력 파일에 메타데이터로 저장되는 워크플로우 프롬프트 정보입니다. 이 매개변수는 UI에 표시되지 않습니다. | PROMPT | 아니요 | - |
| `extra_pnginfo` | 출력 파일에 키-값 쌍으로 저장되는 추가 메타데이터입니다. 이 매개변수는 UI에 표시되지 않습니다. | EXTRA_PNGINFO | 아니요 | - |

## 출력

이 노드에는 출력 연결이 없습니다. 처리된 파일을 `ComfyUI/output/` 디렉터리에 직접 저장합니다.

### 저장된 파일 세부정보

노드는 CLIP 모델의 상태 사전(state dictionary)을 분석하고 감지된 각 구성 요소에 대해 별도의 SafeTensors 파일을 저장합니다. 구성 요소는 매개변수 키의 접두사를 통해 식별됩니다. 노드는 다음 접두사를 순서대로 확인합니다:

- `clip_l.` (CLIP-L 텍스트 인코더)
- `clip_g.` (CLIP-G 텍스트 인코더)
- `clip_h.` (CLIP-H 텍스트 인코더)
- `t5xxl.` (T5-XXL 텍스트 인코더)
- `pile_t5xl.` (Pile-T5-XL 텍스트 인코더)
- `mt5xl.` (mT5-XL 텍스트 인코더)
- `umt5xxl.` (UMT5-XXL 텍스트 인코더)
- `t5base.` (T5-Base 텍스트 인코더)
- `gemma2_2b.` (Gemma 2 2B 텍스트 인코더)
- `llama.` (LLaMA 텍스트 인코더)
- `hydit_clip.` (Hydit CLIP 텍스트 인코더)
- 빈 접두사 (기타 CLIP 구성 요소)

감지된 각 구성 요소에 대해 노드는 `{filename}_{counter:05}_.safetensors` 형식의 파일을 생성합니다(예: `ComfyUI_clip_l_00001_.safetensors`). 이때 구성 요소 이름은 파일 이름 접두사에 추가되며, 카운터는 고유한 파일 이름을 보장합니다. 구성 요소가 저장되면 해당 매개변수 키에서 `transformer.` 접두사가 제거됩니다.

각 파일에 기록되는 메타데이터에는 워크플로우 프롬프트와 추가 PNG 정보가 포함됩니다. 단, `--disable-metadata` 명령줄 인수로 메타데이터 저장이 비활성화된 경우에는 예외입니다.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/ko.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
