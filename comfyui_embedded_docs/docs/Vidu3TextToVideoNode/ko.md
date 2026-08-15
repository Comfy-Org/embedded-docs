# Vidu Q3 텍스트-비디오 생성

Vidu Q3 텍스트-투-비디오 생성 노드는 텍스트 설명으로 비디오를 생성합니다. Vidu Q3 Pro 또는 Q3 Turbo 모델을 사용하여 프롬프트를 기반으로 비디오 콘텐츠를 생성하며, 비디오의 길이, 해상도, 화면 비율 및 오디오 포함 여부를 제어할 수 있습니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 비디오 생성에 사용할 모델입니다. 모델을 선택하면 화면 비율, 해상도, 지속 시간 및 오디오에 대한 추가 구성 매개변수가 표시됩니다. | COMBO | 예 | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | 비디오 생성을 위한 텍스트 설명으로, 최대 2000자까지 입력할 수 있습니다. | STRING | 예 | N/A |
| `seed` | 생성의 무작위성을 제어하기 위한 시드 값입니다 (기본값: 1). | INT | 예 | 0 ~ 2147483647 |

### viduq3-pro 및 viduq3-turbo 입력

다음 구성 매개변수는 `viduq3-pro` 및 `viduq3-turbo` 모델에서 공통으로 사용됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model.aspect_ratio` | 출력 비디오의 화면 비율입니다. | COMBO | 예 | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | 출력 비디오의 해상도입니다. | COMBO | 예 | `"720p"`<br>`"1080p"` |
| `model.duration` | 출력 비디오의 지속 시간(초)입니다 (기본값: 5). | INT | 예 | 1 ~ 16 |
| `model.audio` | 활성화하면 사운드(대화 및 음향 효과 포함)가 포함된 비디오를 출력합니다 (기본값: False). | BOOLEAN | 예 | True/False |

**참고:** `aspect_ratio`, `resolution`, `duration` 및 `audio` 매개변수는 모델 구성의 일부이므로 `model`을 선택하면 필수로 지정해야 합니다. `prompt`는 비어 있을 수 없으며 2000자를 초과할 수 없습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `video` | 생성된 비디오 파일입니다. | VIDEO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/ko.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
