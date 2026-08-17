# Runway 첫-마지막 프레임 비디오 변환

Runway First-Last-Frame to Video 노드는 텍스트 프롬프트와 함께 첫 번째 및 마지막 키프레임을 업로드하여 비디오를 생성합니다. Runway의 Gen-3 모델을 사용하여 제공된 시작 프레임과 종료 프레임 사이의 부드러운 전환을 만듭니다. 이는 종료 프레임이 시작 프레임과 크게 다른 복잡한 전환에 특히 유용합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 생성에 사용할 텍스트 프롬프트 (기본값: 빈 문자열) | STRING | 예 | N/A |
| `start_frame` | 비디오에 사용할 시작 프레임 | IMAGE | 예 | N/A |
| `end_frame` | 비디오에 사용할 종료 프레임. gen3a_turbo에서만 지원됩니다. | IMAGE | 예 | N/A |
| `duration` | 비디오 길이(초) (기본값: "5") | COMBO | 예 | `"5"`<br>`"10"` |
| `ratio` | 생성된 비디오의 화면 비율 (기본값: "768:1280") | COMBO | 예 | `"768:1280"`<br>`"1280:768"` |
| `seed` | 생성에 사용할 무작위 시드. 무작위 시드를 사용하려면 0으로 설정합니다 (기본값: 0). | INT | 아니오 | 0 to 4294967295 |

**매개변수 제약 조건:**

- `prompt`는 최소 1자 이상이어야 합니다.
- `start_frame`과 `end_frame`의 최대 크기는 7999x7999 픽셀이어야 합니다.
- `start_frame`과 `end_frame`의 화면 비율은 0.5에서 2.0 사이여야 합니다.
- `end_frame` 매개변수는 gen3a_turbo 모델을 사용할 때만 지원됩니다.

**참고:** 이 노드는 더 이상 사용되지 않음(deprecated)으로 표시되어 있습니다. 사용 전에 Gen-3에서 키프레임으로 생성하는 Runway의 모범 사례를 검토하시기 바랍니다: https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `output` | 시작 프레임과 종료 프레임 사이를 전환하는 생성된 비디오 | VIDEO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/ko.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
