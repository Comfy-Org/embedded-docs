# ChromaRadianceOptions

ChromaRadianceOptions 노드를 사용하면 Chroma Radiance 모델의 고급 설정을 구성할 수 있습니다. 기존 모델을 래핑하고 시그마 값에 따라 디노이징 프로세스 중에 특정 옵션을 적용하여 NeRF 타일 크기 및 기타 라디언스 관련 매개변수를 세밀하게 제어할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | Chroma Radiance 옵션을 적용할 모델 | MODEL | 예 | - |
| `preserve_wrapper` | 활성화하면 기존 모델 함수 래퍼가 존재하는 경우 해당 래퍼에 위임합니다. 일반적으로 활성화된 상태로 두는 것이 좋습니다. (기본값: True) | BOOLEAN | 아니요 | - |
| `start_sigma` | 이 옵션이 적용되는 첫 번째 시그마입니다. (기본값: 1.0) | FLOAT | 아니요 | 0.0 ~ 1.0 |
| `end_sigma` | 이 옵션이 적용되는 마지막 시그마입니다. (기본값: 0.0) | FLOAT | 아니요 | 0.0 ~ 1.0 |
| `nerf_tile_size` | 기본 NeRF 타일 크기를 재정의할 수 있습니다. -1은 기본값(32)을 사용함을 의미합니다. 0은 비타일링 모드를 사용함을 의미합니다(많은 VRAM이 필요할 수 있음). (기본값: -1) | INT | 아니요 | -1 이상 |
| `force_sequential_txt_ids` | 0 대신 순차적 텍스트 토큰 ID 사용을 강제합니다. 2026-05-22부터 2026-06-01까지의 체크포인트 중 이러한 방식으로 학습되었지만 state dict에 `__sequential__` 키가 포함되지 않은 체크포인트에 사용해야 합니다. (기본값: False) | BOOLEAN | 아니요 | - |

**참고:** Chroma Radiance 옵션은 현재 시그마 값이 `end_sigma`와 `start_sigma` 사이(경계 포함)에 있을 때만 적용됩니다. `nerf_tile_size` 매개변수는 0 이상의 값으로 설정된 경우에만 적용됩니다. `force_sequential_txt_ids` 매개변수는 True로 설정된 경우에만 적용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model` | Chroma Radiance 옵션이 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/ko.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
