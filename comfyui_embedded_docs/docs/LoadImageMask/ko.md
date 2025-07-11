
LoadImageMask 노드는 지정된 경로에서 이미지와 관련된 마스크를 로드하도록 설계되었습니다. 이 노드는 다양한 이미지 형식과 조건, 예를 들어 마스크를 위한 알파 채널의 존재 여부를 처리하여, 이미지 조작이나 분석 작업과의 호환성을 보장하기 위해 이미지를 표준 형식으로 변환하여 준비합니다.

## 입력

| 매개변수  | 데이터 유형   | 설명                                                                                                                                                                                                        |
| --------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `image`   | COMBO[STRING] | 'image' 매개변수는 로드하고 처리할 이미지 파일을 지정합니다. 이는 마스크 추출 및 형식 변환을 위한 소스 이미지를 제공하여 출력 결정에 중요한 역할을 합니다.                                                  |
| `channel` | COMBO[STRING] | 'channel' 매개변수는 마스크 생성을 위해 사용할 이미지의 색상 채널을 지정합니다. 이는 다양한 색상 채널을 기반으로 마스크 생성의 유연성을 제공하여, 다양한 이미지 처리 시나리오에서 노드의 유용성을 높입니다. |

## 출력

| 매개변수 | 데이터 유형 | 설명                                                                                                                                |
| -------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `mask`   | `MASK`      | 이 노드는 지정된 이미지와 채널에서 생성된 마스크를 출력하며, 이미지 조작 작업에서 추가 처리를 위해 적합한 표준 형식으로 준비됩니다. |
