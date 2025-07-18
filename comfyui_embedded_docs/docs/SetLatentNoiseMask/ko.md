
이 노드는 잠재 샘플 세트에 노이즈 마스크를 적용하도록 설계되었습니다. 지정된 마스크를 통합하여 입력 샘플을 수정함으로써 노이즈 특성을 변경합니다.

## 입력

| 매개변수  | 데이터 유형 | 설명                                                                                               |
| --------- | ----------- | -------------------------------------------------------------------------------------------------- |
| `samples` | `LATENT`    | 노이즈 마스크가 적용될 잠재 샘플입니다. 이 매개변수는 수정될 기본 콘텐츠를 결정하는 데 중요합니다. |
| `mask`    | `MASK`      | 잠재 샘플에 적용될 마스크입니다. 샘플 내 노이즈 변경의 영역과 강도를 정의합니다.                   |

## 출력

| 매개변수 | 데이터 유형 | 설명                                           |
| -------- | ----------- | ---------------------------------------------- |
| `latent` | `LATENT`    | 적용된 노이즈 마스크로 수정된 잠재 샘플입니다. |
