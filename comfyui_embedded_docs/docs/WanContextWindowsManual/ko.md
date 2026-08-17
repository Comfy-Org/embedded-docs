# WAN 컨텍스트 창 (수동)

Wan Context Windows (Manual) 노드를 사용하면 2차원 처리를 수행하는 Wan 유사 모델에 대한 컨텍스트 창을 수동으로 구성할 수 있습니다. 이 노드는 창 길이, 겹침, 스케줄링 방법 및 융합 기법을 지정하여 샘플링 중에 컨텍스트 창 설정을 적용하므로 모델이 다양한 컨텍스트 영역을 처리하는 방식을 제어할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 샘플링 중에 컨텍스트 창을 적용할 모델입니다. | MODEL | 예 | - |
| `context_length` | 실제 프레임 기준 컨텍스트 창의 길이입니다. 4n + 1이어야 합니다. (기본값: 81) | INT | 예 | 1 to 16384 (step 4) |
| `context_overlap` | 실제 프레임 기준 컨텍스트 창의 겹침입니다. (기본값: 30) | INT | 예 | 0 or greater |
| `context_schedule` | 컨텍스트 창에 대한 단계 종속 스케줄링 알고리즘입니다. (기본값: "uniform_standard") | COMBO | 예 | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | 컨텍스트 창의 보폭입니다. uniform 스케줄에만 적용됩니다. (기본값: 1) | INT | 예 | 1 or greater |
| `closed_loop` | 컨텍스트 창 루프를 닫을지 여부입니다. 루프형(looped) 스케줄에만 적용됩니다. (기본값: False) | BOOLEAN | 예 | True or False |
| `fuse_method` | 컨텍스트 창을 융합하는 데 사용할 방법입니다. (기본값: "pyramid") | COMBO | 예 | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | FreeNoise 노이즈 셔플링을 적용할지 여부입니다. 창 혼합을 개선합니다. (기본값: True) | BOOLEAN | 예 | True or False |
| `retain_first_frame` | 모든 컨텍스트 창의 첫 번째 I2V 프레임을 유지합니다. (초기 참조 유지에 도움이 될 수 있습니다). (기본값: False) | BOOLEAN | 예 | True or False |
| `split_conds_to_windows` | 여러 컨디셔닝(ConditionCombine으로 생성됨)을 지역 인덱스를 기준으로 각 창에 분할할지 여부입니다. (기본값: False) | BOOLEAN | 예 | True or False |

**참고:** `context_stride`는 uniform 스케줄에만 영향을 주며, `closed_loop`는 루프형(looped) 스케줄에만 적용됩니다. `context_length`는 4n + 1 패턴을 따라야 합니다. 이 노드는 `context_length`와 `context_overlap`을 적용하기 전에 실제 프레임에서 모델 단위로 변환하며, `context_length`는 최소 1, `context_overlap`은 최소 0을 적용합니다. `context_stride`, `closed_loop`, `freenoise`, `split_conds_to_windows` 입력은 고급 옵션입니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 컨텍스트 창 구성이 적용된 모델입니다. | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/ko.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
