# Runway 이미지 비디오 변환 (Gen3a Turbo)

Runway Image to Video (Gen3a Turbo) 노드는 Runway의 Gen3a Turbo 모델을 사용하여 단일 시작 프레임에서 비디오를 생성합니다. 텍스트 프롬프트와 초기 이미지 프레임을 입력받아 지정된 지속 시간과 화면 비율에 따라 비디오 시퀀스를 생성합니다. 이 노드는 Runway의 API에 연결하여 생성 작업을 원격으로 처리합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 생성에 사용할 텍스트 프롬프트 (기본값: "") | STRING | 예 | N/A |
| `start_frame` | 비디오에 사용할 시작 프레임 | IMAGE | 예 | N/A |
| `duration` | 비디오 지속 시간(초) (기본값: "5") | COMBO | 예 | `"5"`<br>`"10"` |
| `ratio` | 생성된 비디오의 화면 비율 (기본값: "768:1280") | COMBO | 예 | `"768:1280"`<br>`"1280:768"` |
| `seed` | 생성에 사용할 난수 시드 (기본값: 0) | INT | 아니요 | 0 ~ 4294967295 |

**매개변수 제약 조건:**

- `start_frame`의 크기는 7999x7999 픽셀을 초과할 수 없습니다.
- `start_frame`의 화면 비율은 0.5에서 2.0 사이여야 합니다.
- `prompt`에는 최소 한 개 이상의 문자가 포함되어야 합니다 (비어 있을 수 없습니다).

**참고 사항:**

- 이 노드는 더 이상 사용되지 않습니다.
- 생성 전에 Runway는 모범 사례 가이드를 검토할 것을 권장합니다: https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `output` | 생성된 비디오 시퀀스 | VIDEO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/ko.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
