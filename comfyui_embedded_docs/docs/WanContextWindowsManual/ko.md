> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/ko.md)

WAN Context Windows (Manual) 노드를 사용하면 2차원 처리를 지원하는 WAN 유사 모델에 대한 컨텍스트 창을 수동으로 구성할 수 있습니다. 이 노드는 샘플링 과정에서 창 길이, 오버랩, 스케줄링 방법 및 퓨전 기술을 지정하여 사용자 정의 컨텍스트 창 설정을 적용합니다. 이를 통해 모델이 서로 다른 컨텍스트 영역에서 정보를 처리하는 방식을 정밀하게 제어할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 샘플링 중에 컨텍스트 창을 적용할 모델입니다. |
| `context_length` | INT | 예 | 1 ~ 1048576 | 컨텍스트 창의 길이입니다 (기본값: 81). |
| `context_overlap` | INT | 예 | 0 ~ 1048576 | 컨텍스트 창의 오버랩 정도입니다 (기본값: 30). |
| `context_schedule` | COMBO | 예 | "static_standard"<br>"uniform_standard"<br>"uniform_looped"<br>"batched" | 컨텍스트 창의 스트라이드 방식입니다. |
| `context_stride` | INT | 예 | 1 ~ 1048576 | 컨텍스트 창의 스트라이드 값으로, 균일 스케줄에서만 적용됩니다 (기본값: 1). |
| `closed_loop` | BOOLEAN | 예 | - | 컨텍스트 창 루프를 닫을지 여부로, 루프 스케줄에서만 적용됩니다 (기본값: False). |
| `fuse_method` | COMBO | 예 | "pyramid" | 컨텍스트 창을 퓨전하는 데 사용할 방법입니다 (기본값: "pyramid"). |

**참고:** `context_stride` 매개변수는 균일 스케줄에만 영향을 미치며, `closed_loop`은 루프 스케줄에만 적용됩니다. 컨텍스트 길이와 오버랩 값은 처리 중 최소 유효 값을 보장하도록 자동으로 조정됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 적용된 컨텍스트 창 구성이 포함된 모델입니다. |