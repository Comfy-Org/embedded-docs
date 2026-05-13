> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/ko.md)

ConditioningConcat 노드는 컨디셔닝 벡터를 연결(concatenate)하도록 설계되었으며, 특히 'conditioning_from' 벡터를 'conditioning_to' 벡터에 병합합니다. 이 작업은 두 소스의 컨디셔닝 정보를 하나의 통합된 표현으로 결합해야 하는 시나리오에서 필수적입니다.

## 입력

| 매개변수               | Comfy 데이터 타입 | 설명 |
|-----------------------|--------------------|-------------|
| `대상 조건`     | `CONDITIONING`     | 'conditioning_from' 벡터가 연결될 기본 컨디셔닝 벡터 세트를 나타냅니다. 연결 프로세스의 기준이 됩니다. |
| `추가 조건`   | `CONDITIONING`     | 'conditioning_to' 벡터에 연결될 컨디셔닝 벡터로 구성됩니다. 이 매개변수를 통해 기존 세트에 추가 컨디셔닝 정보를 통합할 수 있습니다. |

## 출력

| 매개변수            | Comfy 데이터 타입 | 설명 |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | 'conditioning_from' 벡터를 'conditioning_to' 벡터에 연결한 결과로 생성된 통합 컨디셔닝 벡터 세트입니다. |