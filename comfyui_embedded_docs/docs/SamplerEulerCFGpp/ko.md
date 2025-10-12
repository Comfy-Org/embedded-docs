> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/ko.md)

SamplerEulerCFGpp 노드는 출력물을 생성하기 위한 Euler CFG++ 샘플링 방법을 제공합니다. 이 노드는 사용자 선호도에 따라 선택할 수 있는 두 가지 다른 구현 버전의 Euler CFG++ 샘플러를 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `버전` | STRING | 예 | `"regular"`<br>`"alternative"` | 사용할 Euler CFG++ 샘플러의 구현 버전 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 구성된 Euler CFG++ 샘플러 인스턴스를 반환합니다 |
