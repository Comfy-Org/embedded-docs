
## 입력

| 매개변수     | Comfy 타입 | 설명                                                                               |
| ------------ | ---------- | --------------------------------------------------------------------------------- |
| `width`      | `INT`      | 비디오 너비, 기본값 848, 최소 16, 최대 `nodes.MAX_RESOLUTION`, 단계 크기 16      |
| `height`     | `INT`      | 비디오 높이, 기본값 480, 최소 16, 최대 `nodes.MAX_RESOLUTION`, 단계 크기 16      |
| `length`     | `INT`      | 비디오 길이, 기본값 25, 최소 1, 최대 `nodes.MAX_RESOLUTION`, 단계 크기 4         |
| `batch_size` | `INT`      | 배치 크기, 기본값 1, 최소 1, 최대 4096                                          |

## 출력

| 매개변수     | Comfy 타입 | 설명                                                                              |
| ------------ | ---------- | -------------------------------------------------------------------------------- |
| `samples`    | `LATENT`   | 생성된 잠재 비디오 샘플, 제로 텐서를 포함하며 처리 및 생성 작업을 위한 준비가 되어 있음 |
