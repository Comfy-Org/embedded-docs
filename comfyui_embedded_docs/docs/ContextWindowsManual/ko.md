> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/ko.md)

Context Windows (Manual) 노드를 사용하면 샘플링 중 모델에 대한 컨텍스트 창을 수동으로 구성할 수 있습니다. 이 노드는 지정된 길이, 중첩 및 스케줄링 패턴을 가진 중복되는 컨텍스트 세그먼트를 생성하여 데이터를 관리 가능한 청크로 처리하면서 세그먼트 간의 연속성을 유지합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 샘플링 중 컨텍스트 창을 적용할 모델입니다. |
| `context_length` | INT | 아니오 | 1+ | 컨텍스트 창의 길이입니다 (기본값: 16). |
| `context_overlap` | INT | 아니오 | 0+ | 컨텍스트 창의 중첩 정도입니다 (기본값: 4). |
| `context_schedule` | COMBO | 아니오 | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | 컨텍스트 창의 스케줄링 방식입니다. |
| `context_stride` | INT | 아니오 | 1+ | 컨텍스트 창의 스트라이드입니다; 균일 스케줄에서만 적용 가능합니다 (기본값: 1). |
| `closed_loop` | BOOLEAN | 아니오 | - | 컨텍스트 창 루프를 닫을지 여부입니다; 루프 스케줄에서만 적용 가능합니다 (기본값: False). |
| `fuse_method` | COMBO | 아니오 | `PYRAMID`<br>`LIST_STATIC` | 컨텍스트 창을 융합하는 데 사용할 방법입니다 (기본값: PYRAMID). |
| `dim` | INT | 아니오 | 0-5 | 컨텍스트 창을 적용할 차원입니다 (기본값: 0). |

**매개변수 제약 조건:**
- `context_stride`는 균일 스케줄이 선택된 경우에만 사용됩니다
- `closed_loop`는 루프 스케줄에만 적용 가능합니다
- `dim`은 0에서 5 사이(포함)여야 합니다

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 샘플링 중 컨텍스트 창이 적용된 모델입니다. |