이 노드는 두 이미지를 지정된 방향(위, 아래, 왼쪽, 오른쪽)으로 결합할 수 있으며, 크기 조정과 이미지 간 간격 설정을 지원합니다.

## 입력

| 매개변수 이름 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|--------------|------------|------------|--------|-------|------|
| `image1` | IMAGE | 필수 | - | - | 결합할 첫 번째 이미지 |
| `image2` | IMAGE | 선택 | None | - | 결합할 두 번째 이미지, 제공되지 않으면 첫 번째 이미지만 반환 |
| `direction` | STRING | 필수 | right | right/down/left/up | 두 번째 이미지를 결합할 방향: right (오른쪽), down (아래), left (왼쪽), up (위) |
| `match_image_size` | BOOLEAN | 필수 | True | True/False | 두 번째 이미지의 크기를 첫 번째 이미지의 크기에 맞출지 여부 |
| `spacing_width` | INT | 필수 | 0 | 0-1024 | 이미지 사이의 간격 너비, 짝수여야 함 |
| `spacing_color` | STRING | 필수 | white | white/black/red/green/blue | 결합된 이미지 사이의 간격 색상 |

> `spacing_color`의 경우, "white/black" 이외의 색상을 사용할 때 `match_image_size`가 `false`로 설정되어 있으면 패딩 영역이 검은색으로 채워집니다

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-----------|------------|------|
| `IMAGE` | IMAGE | 결합된 이미지 |

## 워크플로우 예시

아래 워크플로우에서는 서로 다른 크기의 3개 입력 이미지를 예시로 사용합니다:

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**첫 번째 Image Stitch 노드**

- `match_image_size`: false, 이미지들이 원본 크기로 결합됨
- `direction`: up, `image2`가 `image1` 위에 배치됨
- `spacing_width`: 20
- `spacing_color`: black

출력 이미지 1:

![output1](./asset/output-1.webp)

**두 번째 Image Stitch 노드**

- `match_image_size`: true, 두 번째 이미지가 첫 번째 이미지의 높이나 너비에 맞게 크기 조정됨
- `direction`: right, `image3`가 오른쪽에 나타남
- `spacing_width`: 20
- `spacing_color`: white

출력 이미지 2:

![output2](./asset/output-2.webp)
