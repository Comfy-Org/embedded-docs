
VAEDecode 노드는 지정된 변분 오토인코더(VAE)를 사용하여 잠재 표현을 이미지로 디코딩하도록 설계되었습니다. 이는 압축된 데이터 표현에서 이미지를 생성하고, 잠재 공간 인코딩에서 이미지를 재구성하는 데 도움을 줍니다.

## 입력

| 매개변수  | 데이터 유형 | 설명                                                                                                                                                                    |
| --------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `samples` | `LATENT`    | 'samples' 매개변수는 이미지로 디코딩될 잠재 표현을 나타냅니다. 이는 디코딩 과정에서 이미지를 재구성하는 데 필요한 압축 데이터를 제공합니다.                             |
| `vae`     | VAE         | 'vae' 매개변수는 잠재 표현을 이미지로 디코딩하는 데 사용될 변분 오토인코더 모델을 지정합니다. 이는 디코딩 메커니즘과 재구성된 이미지의 품질을 결정하는 데 필수적입니다. |

## 출력

| 매개변수 | 데이터 유형 | 설명                                                                        |
| -------- | ----------- | --------------------------------------------------------------------------- |
| `image`  | `IMAGE`     | 출력은 제공된 잠재 표현을 지정된 VAE 모델을 사용하여 재구성한 이미지입니다. |
