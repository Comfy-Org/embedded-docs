
LatentCompositeMasked 노드는 두 개의 잠재 표현을 지정된 좌표에서 혼합하도록 설계되었으며, 마스크를 사용하여 더 정교한 합성을 가능하게 합니다. 이 노드는 한 이미지의 일부를 다른 이미지 위에 겹쳐 복잡한 잠재 이미지를 생성할 수 있으며, 소스 이미지를 완벽하게 맞추기 위해 크기를 조정할 수 있습니다.

## 입력

| 매개변수        | 데이터 유형 | 설명                                                                                                                                           |
| --------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `destination`   | `LATENT`    | 다른 잠재 표현이 합성될 잠재 표현입니다. 합성 작업의 기본 레이어로 작용합니다.                                                                 |
| `source`        | `LATENT`    | 목적지에 합성될 잠재 표현입니다. 이 소스 레이어는 지정된 매개변수에 따라 크기 조정 및 위치 지정이 가능합니다.                                  |
| `x`             | `INT`       | 소스가 배치될 목적지 잠재 표현의 x-좌표입니다. 소스 레이어의 정밀한 위치 지정을 허용합니다.                                                    |
| `y`             | `INT`       | 소스가 배치될 목적지 잠재 표현의 y-좌표로, 정확한 오버레이 위치 지정을 가능하게 합니다.                                                        |
| `resize_source` | `BOOLEAN`   | 소스 잠재 표현을 합성 전에 목적지의 크기에 맞추어 조정할지 여부를 나타내는 불리언 플래그입니다.                                                |
| `mask`          | `MASK`      | 소스를 목적지에 블렌딩하는 것을 제어하는 데 사용할 수 있는 선택적 마스크입니다. 마스크는 최종 합성에서 소스의 어느 부분이 보일지를 정의합니다. |

## 출력

| 매개변수 | 데이터 유형 | 설명                                                                                                 |
| -------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| `latent` | `LATENT`    | 소스를 목적지에 합성한 후, 선택적으로 마스크를 사용하여 선택적 블렌딩을 수행한 결과 잠재 표현입니다. |
