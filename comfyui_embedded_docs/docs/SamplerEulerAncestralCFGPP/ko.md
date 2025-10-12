> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/ko.md)

SamplerEulerAncestralCFGPP 노드는 분류자 없는 지도(Classifier-Free Guidance)와 Euler Ancestral 방법을 사용하여 이미지를 생성하기 위한 특수 샘플러를 생성합니다. 이 샘플러는 선조 샘플링(Ancestral Sampling) 기법과 지도 조건화를 결합하여 일관성을 유지하면서 다양한 이미지 변형을 생성합니다. 노이즈 및 스텝 크기 조정을 제어하는 매개변수를 통해 샘플링 과정을 미세 조정할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | 예 | 0.0 - 1.0 | 샘플링 중 스텝 크기를 제어하며, 값이 높을수록 더 공격적인 업데이트를 수행합니다 (기본값: 1.0) |
| `s_noise` | FLOAT | 예 | 0.0 - 10.0 | 샘플링 과정 중 추가되는 노이즈의 양을 조정합니다 (기본값: 1.0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 이미지 생성 파이프라인에서 사용할 수 있도록 구성된 샘플러 객체를 반환합니다 |
