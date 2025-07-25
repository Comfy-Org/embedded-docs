`CLIP 텍스트 인코딩 (SDXL Refiner)`  노드는 SDXL Refiner 모델 전용으로, 텍스트 프롬프트에 미적 점수와 차원 정보(가로·세로 크기)를 결합해 보다 정밀한 생성 조건을 만들어 줍니다. 마치 전문 아트 디렉터처럼, 창작 의도뿐 아니라 미적 기준과 출력 사양까지 함께 반영해 최종 결과물의 완성도를 높입니다.

## SDXL Refiner 소개

SDXL Refiner는 SDXL 기본 모델로 생성된 결과물에 디테일을 더하고 품질을 끌어올리는 역할을 합니다.
비유하자면, 작업물을 넘겨받아 마지막 손질을 맡는 전문 보정 디자이너와도 같습니다.

1. 먼저, 기본 모델이 만든 예비 이미지나 텍스트 설명을 넘겨받습니다.
2. 이후, 미적 점수와 텍스트 인코딩에 사용될 이미지 크기 설정값(가로·세로)을 기준으로 정제 방향을 조정합니다.
3. 마지막으로, 머리카락이나 질감처럼 미세한 디테일(고주파 영역)을 다듬어 이미지를 보다 깔끔하고 정돈된 형태로 마무리합니다.

Refiner는 두 가지 방식으로 사용될 수 있습니다:

- 기본 모델이 만든 이미지를 사후 보정(Post-processing)하는 독립 정제 단계로 사용하거나,
- 생성이 거의 완료된 마지막 단계에서 정제 작업을 맡는 방식으로도 활용할 수 있습니다.

## 입력

| 매개변수 이름 | 데이터 유형 | 입력 유형 | 기본값 | 값 범위 | 설명 |
|--------------|------------|-----------|--------|---------|------|
| `clip` | CLIP | Required | - | - | 텍스트 토큰화와 인코딩에 사용되는 CLIP 모델 인스턴스로, 텍스트를 모델이 이해할 수 있는 형식으로 변환하는 핵심 구성 요소 |
| `ascore` | FLOAT | Optional | 6.0 | 0.0-1000.0 | 생성된 이미지의 시각적 품질과 미적 요소를 제어합니다. 작품의 품질 기준을 설정하는 것과 유사합니다:<br/>- 높은 점수(7.5-8.5): 더 정교하고 세부적인 효과를 추구<br/>- 중간 점수(6.0-7.0): 균형 잡힌 품질 제어<br/>- 낮은 점수(2.0-3.0): 부정적 프롬프트에 적합 |
| `너비` | INT | Required | 1024 | 64-16384 | 출력 이미지의 너비(픽셀)를 지정합니다. 8의 배수여야 합니다. SDXL은 총 픽셀 수가 1024×1024(약 1M 픽셀)에 가까울 때 가장 잘 작동합니다 |
| `높이` | INT | Required | 1024 | 64-16384 | 출력 이미지의 높이(픽셀)를 지정합니다. 8의 배수여야 합니다. SDXL은 총 픽셀 수가 1024×1024(약 1M 픽셀)에 가까울 때 가장 잘 작동합니다 |
| `text` | STRING | Required | - | - | 텍스트 프롬프트 설명으로, 여러 줄 입력과 동적 프롬프트 구문을 지원합니다. Refiner에서 텍스트 프롬프트는 원하는 시각적 품질과 세부 특성을 설명하는 데 더 중점을 두어야 합니다 |

## 출력

| 출력 이름 | 데이터 유형 | 설명 |
|-----------|------------|------|
| `조건` | CONDITIONING | 텍스트 의미론, 미적 기준, 차원 정보의 통합 인코딩을 포함하는 정제된 조건부 출력으로, SDXL Refiner 모델의 정확한 이미지 정제를 안내하기 위해 특별히 설계되었습니다 |

## 참고 사항

1. 이 노드는 SDXL Refiner 모델을 위해 특별히 최적화되었으며 일반 CLIPTextEncode 노드와는 다릅니다
2. 미적 점수 7.5가 기준선으로 권장되며, 이는 SDXL 훈련에서 사용되는 표준 설정입니다
3. 모든 차원 매개변수는 8의 배수여야 하며, 총 픽셀 수가 1024×1024(약 1M 픽셀)에 가까운 것이 권장됩니다
4. Refiner 모델은 이미지 세부 사항과 품질 향상에 중점을 두므로, 텍스트 프롬프트는 장면 내용보다는 원하는 시각적 효과를 강조해야 합니다
5. 실제 사용에서 Refiner는 일반적으로 생성의 후반 단계(약 마지막 20% 단계)에서 사용되며, 세부 사항 최적화에 중점을 둡니다
