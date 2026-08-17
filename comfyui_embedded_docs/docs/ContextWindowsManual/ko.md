# 컨텍스트 윈도우 (수동)

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 샘플링 중 컨텍스트 창을 적용할 모델입니다. | MODEL | 예 | - |
| `context_length` | 컨텍스트 창의 길이입니다 (기본값: 16). | INT | 아니오 | 1+ |
| `context_overlap` | 컨텍스트 창의 겹침입니다 (기본값: 4). | INT | 아니오 | 0+ |
| `context_schedule` | 컨텍스트 창에 대한 단계 종속 스케줄링 알고리즘입니다 (기본값: STATIC_STANDARD). | COMBO | 아니오 | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | 컨텍스트 창의 스트라이드입니다. 균일 스케줄에만 적용됩니다 (기본값: 1). | INT | 아니오 | 1+ |
| `closed_loop` | 컨텍스트 창 루프를 닫을지 여부입니다. 루프형 스케줄에만 적용됩니다 (기본값: False). | BOOLEAN | 아니오 | - |
| `fuse_method` | 컨텍스트 창을 융합하는 데 사용할 방법입니다 (기본값: PYRAMID). | COMBO | 아니오 | `"PYRAMID"`<br>`"LIST_STATIC"` |
| `dim` | 컨텍스트 창을 적용할 차원입니다 (기본값: 0). | INT | 아니오 | 0-5 |
| `freenoise` | FreeNoise 노이즈 셔플링을 적용할지 여부입니다. 창 혼합을 개선합니다 (기본값: False). | BOOLEAN | 아니오 | - |
| `cond_retain_index_list` | 각 창의 컨디셔닝 텐서에 유지할 잠재 인덱스 목록입니다. concat 스타일 I2V 모델(예: Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD)의 경우 인코딩된 시작 이미지는 c_concat 컨디셔닝 채널에 있습니다. 이 값을 '0'으로 설정하면 모든 창의 sub-pos 0에서 해당 시작 이미지 콘텐츠가 유지됩니다 (기본값: ""). | STRING | 아니오 | - |
| `split_conds_to_windows` | 여러 컨디셔닝(ConditionCombine으로 생성됨)을 영역 인덱스에 따라 각 창으로 분할할지 여부입니다 (기본값: False). | BOOLEAN | 아니오 | - |
| `latent_retain_index_list` | 각 창의 노이즈 잠재 자체에 유지할 잠재 인덱스 목록입니다. 참조 콘텐츠(예: 시작 이미지)가 별도의 컨디셔닝 채널이 아닌 노이즈 잠재에 직접 있는 워크플로우에 사용합니다 (예: LTXV, AnimateDiff와 같은 인플레이스(in-place) 스타일 I2V). `cond_retain_index_list`와 독립적입니다 (기본값: ""). | STRING | 아니오 | - |
| `causal_window_fix` | 0이 아닌 인덱스의 컨텍스트 창에 인과적 수정 프레임을 추가할지 여부입니다 (기본값: True). | BOOLEAN | 아니오 | - |

**매개변수 제약 조건:**

- `context_stride`는 균일 스케줄이 선택된 경우에만 사용됩니다.
- `closed_loop`는 루프형 스케줄에만 적용됩니다.
- `dim`은 0 이상 5 이하여야 합니다.
- `cond_retain_index_list`는 문자열로 된 쉼표로 구분된 정수 인덱스 목록을 필요로 합니다 (예: "0,1,2").
- `latent_retain_index_list`는 문자열로 된 쉼표로 구분된 정수 인덱스 목록을 필요로 하며 (예: "0,1,2"), `cond_retain_index_list`와 독립적입니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `model` | 샘플링 중 컨텍스트 창이 적용된 모델입니다. | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/ko.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
