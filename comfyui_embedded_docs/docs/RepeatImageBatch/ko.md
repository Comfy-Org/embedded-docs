
RepeatImageBatch 노드는 주어진 이미지를 지정된 횟수만큼 복제하여 동일한 이미지의 배치를 생성하도록 설계되었습니다. 이 기능은 배치 처리나 데이터 증강과 같은 작업에 여러 인스턴스의 동일한 이미지가 필요한 경우에 유용합니다.

## 입력

| 필드     | 데이터 유형 | 설명                                                                                                                                                   |
| -------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `image`  | `IMAGE`     | 'image' 매개변수는 복제할 이미지를 나타냅니다. 이는 배치 전반에 걸쳐 복제될 콘텐츠를 정의하는 데 중요합니다.                                           |
| `amount` | `INT`       | 'amount' 매개변수는 입력 이미지를 복제해야 하는 횟수를 지정합니다. 이는 출력 배치의 크기에 직접적인 영향을 미치며, 유연한 배치 생성을 가능하게 합니다. |

## 출력

| 필드    | 데이터 유형 | 설명                                                                            |
| ------- | ----------- | ------------------------------------------------------------------------------- |
| `image` | `IMAGE`     | 출력은 입력 이미지와 동일한 이미지의 배치로, 지정된 'amount'에 따라 복제됩니다. |
