이 노드는 입력 이미지의 종횡비를 기반으로 Lanczos 알고리즘을 사용하여 Flux Kontext 모델 학습 시 사용된 최적의 크기로 이미지를 조정합니다. 큰 크기의 이미지를 입력하면 모델 출력 품질이 저하되거나 출력에 여러 주체가 나타나는 등의 문제가 발생할 수 있으므로 이 노드가 특히 유용합니다.

## 입력

| 매개변수 이름 | 데이터 유형 | 입력 유형 | 기본값 | 값 범위 | 설명 |
|--------------|------------|-----------|---------|----------|------|
| `image` | IMAGE | 필수 | - | - | 크기를 조정할 입력 이미지 |

## 출력

| 출력 이름 | 데이터 유형 | 설명 |
|-----------|------------|------|
| `image` | IMAGE | 크기가 조정된 이미지 |

## 프리셋 크기 목록

다음은 모델 학습 시 사용된 표준 크기 목록입니다. 노드는 입력 이미지의 종횡비와 가장 가까운 크기를 선택합니다:

| 너비 | 높이 | 종횡비 |
|------|------|--------|
| 672  | 1568 | 0.429  |
| 688  | 1504 | 0.457  |
| 720  | 1456 | 0.494  |
| 752  | 1392 | 0.540  |
| 800  | 1328 | 0.603  |
| 832  | 1248 | 0.667  |
| 880  | 1184 | 0.743  |
| 944  | 1104 | 0.855  |
| 1024 | 1024 | 1.000  |
| 1104 | 944  | 1.170  |
| 1184 | 880  | 1.345  |
| 1248 | 832  | 1.500  |
| 1328 | 800  | 1.660  |
| 1392 | 752  | 1.851  |
| 1456 | 720  | 2.022  |
| 1504 | 688  | 2.186  |
| 1568 | 672  | 2.333  |
