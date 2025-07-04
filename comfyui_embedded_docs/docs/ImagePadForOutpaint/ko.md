이 노드는 이미지 외부 확장(outpainting) 과정을 위해 이미지 주변에 패딩을 추가하여 이미지를 준비하는 데 사용됩니다. 이는 이미지의 크기를 조정하여 외부 확장 알고리즘과의 호환성을 보장하고, 원래 경계를 넘어 확장된 이미지 영역을 생성할 수 있도록 합니다.

## 입력

| 매개변수     | 데이터 유형 | 설명                                                                                                   |
| ------------ | ----------- | ------------------------------------------------------------------------------------------------------ |
| `image`      | `IMAGE`     | 'image' 입력은 외부 확장을 위해 준비될 주요 이미지로, 패딩 작업의 기반이 됩니다.                       |
| `left`       | `INT`       | 이미지의 왼쪽에 추가할 패딩의 양을 지정하여 외부 확장을 위한 확장 영역에 영향을 줍니다.                |
| `top`        | `INT`       | 이미지의 상단에 추가할 패딩의 양을 결정하여 외부 확장을 위한 수직 확장에 영향을 줍니다.                |
| `right`      | `INT`       | 이미지의 오른쪽에 추가할 패딩의 양을 정의하여 외부 확장을 위한 수평 확장에 영향을 줍니다.              |
| `bottom`     | `INT`       | 이미지의 하단에 추가할 패딩의 양을 나타내어 외부 확장을 위한 수직 확장에 기여합니다.                   |
| `feathering` | `INT`       | 원본 이미지와 추가된 패딩 간의 전환의 부드러움을 제어하여 외부 확장을 위한 시각적 통합을 향상시킵니다. |

## 출력

| 매개변수 | 데이터 유형 | 설명                                                                                                    |
| -------- | ----------- | ------------------------------------------------------------------------------------------------------- |
| `image`  | `IMAGE`     | 출력 'image'는 외부 확장 과정을 위해 준비된 패딩된 이미지를 나타냅니다.                                 |
| `mask`   | `MASK`      | 출력 'mask'는 원본 이미지와 추가된 패딩의 영역을 나타내며, 외부 확장 알고리즘을 안내하는 데 유용합니다. |
