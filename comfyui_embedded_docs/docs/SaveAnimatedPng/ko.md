
SaveAnimatedPNG 노드는 프레임 시퀀스로부터 애니메이션 PNG 이미지를 생성하고 저장하도록 설계되었습니다. 개별 이미지 프레임을 하나의 통합된 애니메이션으로 조립하며, 프레임 지속 시간, 반복, 메타데이터 포함을 사용자 정의할 수 있습니다.

## 입력

| 필드              | 데이터 유형 | 설명                                                                                                     |
| ----------------- | ----------- | -------------------------------------------------------------------------------------------------------- |
| `images`          | `IMAGE`     | 처리되어 애니메이션 PNG로 저장될 이미지 목록입니다. 목록의 각 이미지는 애니메이션의 프레임을 나타냅니다. |
| `filename_prefix` | `STRING`    | 생성된 애니메이션 PNG 파일의 접두사로 사용될 출력 파일의 기본 이름을 지정합니다.                         |
| `fps`             | `FLOAT`     | 애니메이션의 초당 프레임 수로, 프레임이 표시되는 속도를 제어합니다.                                      |
| `compress_level`  | `INT`       | 애니메이션 PNG 파일에 적용되는 압축 수준으로, 파일 크기와 이미지 선명도에 영향을 미칩니다.               |

## 출력

| 필드 | 데이터 유형 | 설명                                                                                                                           |
| ---- | ----------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `ui` | N/A         | 생성된 애니메이션 PNG 이미지를 표시하고 애니메이션이 단일 프레임인지 다중 프레임인지 여부를 나타내는 UI 컴포넌트를 제공합니다. |
