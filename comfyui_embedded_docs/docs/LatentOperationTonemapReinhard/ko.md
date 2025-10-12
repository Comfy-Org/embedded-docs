> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/ko.md)

LatentOperationTonemapReinhard 노드는 잠재 벡터에 Reinhard 톤매핑을 적용합니다. 이 기법은 잠재 벡터를 정규화하고 평균 및 표준 편차를 기반으로 한 통계적 접근 방식을 사용하여 크기를 조정하며, 강도는 승수 매개변수로 제어됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `배율` | FLOAT | 아니요 | 0.0 ~ 100.0 | 톤매핑 효과의 강도를 제어합니다 (기본값: 1.0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | 잠재 벡터에 적용할 수 있는 톤매핑 연산을 반환합니다 |
