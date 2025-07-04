
LatentCrop 노드는 이미지의 잠재 표현에서 자르기 작업을 수행하도록 설계되었습니다. 자르기 영역의 크기와 위치를 지정하여 잠재 공간의 목표 지향적 수정을 가능하게 합니다.

## 입력

| 매개변수  | 데이터 유형 | 설명                                                                                                           |
| --------- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| `samples` | `LATENT`    | 'samples' 매개변수는 자를 잠재 표현을 나타냅니다. 이는 자르기 작업이 수행될 데이터를 정의하는 데 필수적입니다. |
| `width`   | `INT`       | 자르기 영역의 너비를 지정합니다. 이는 출력 잠재 표현의 크기에 직접적인 영향을 미칩니다.                        |
| `height`  | `INT`       | 자르기 영역의 높이를 지정하여 결과적으로 잘린 잠재 표현의 크기에 영향을 줍니다.                                |
| `x`       | `INT`       | 자르기 영역의 시작 x-좌표를 결정하여 원래 잠재 표현 내에서 자르기의 위치에 영향을 줍니다.                      |
| `y`       | `INT`       | 자르기 영역의 시작 y-좌표를 결정하여 원래 잠재 표현 내에서 자르기의 위치를 설정합니다.                         |

## 출력

| 매개변수 | 데이터 유형 | 설명                                                  |
| -------- | ----------- | ----------------------------------------------------- |
| `latent` | `LATENT`    | 출력은 지정된 자르기가 적용된 수정된 잠재 표현입니다. |
