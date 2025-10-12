> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/ko.md)

ChromaRadianceOptions 노드를 사용하면 Chroma Radiance 모델의 고급 설정을 구성할 수 있습니다. 기존 모델을 래핑하고 시그마 값에 기반하여 디노이징 과정에서 특정 옵션을 적용하며, NeRF 타일 크기 및 기타 radiance 관련 매개변수에 대한 미세 조정 제어를 가능하게 합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | 필수 | - | - | Chroma Radiance 옵션을 적용할 모델 |
| `preserve_wrapper` | BOOLEAN | 선택사항 | True | - | 활성화하면 기존 모델 함수 래퍼가 존재할 경우 이를 위임합니다. 일반적으로 활성화된 상태로 유지해야 합니다. |
| `start_sigma` | FLOAT | 선택사항 | 1.0 | 0.0 - 1.0 | 이 옵션이 적용될 첫 번째 시그마 값입니다. |
| `end_sigma` | FLOAT | 선택사항 | 0.0 | 0.0 - 1.0 | 이 옵션이 적용될 마지막 시그마 값입니다. |
| `nerf_tile_size` | INT | 선택사항 | -1 | -1 이상 | 기본 NeRF 타일 크기를 재정의할 수 있습니다. -1은 기본값(32)을 사용함을 의미합니다. 0은 비타일링 모드를 사용함을 의미합니다(많은 VRAM이 필요할 수 있음). |

**참고:** Chroma Radiance 옵션은 현재 시그마 값이 `end_sigma`와 `start_sigma` 사이(포함)에 있을 때만 효과가 적용됩니다. `nerf_tile_size` 매개변수는 0 이상의 값으로 설정된 경우에만 적용됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | Chroma Radiance 옵션이 적용된 수정된 모델 |
