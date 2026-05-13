> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/ko.md)

## 개요

이 노드는 HappyHorse 모델을 사용하여 단일 시작 이미지로부터 짧은 비디오를 생성합니다. 첫 번째 프레임 이미지와 원하는 동작 및 장면을 설명하는 텍스트 프롬프트를 제공하면, 노드가 해당 이미지에서 이어지는 비디오를 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `"happyhorse-1.0-i2v"` | 비디오 생성에 사용할 HappyHorse 모델입니다. |
| `model.prompt` | STRING | 아니요 | 해당 없음 | 요소와 시각적 특징을 설명하는 프롬프트입니다. 영어와 중국어를 지원합니다. (기본값: "") |
| `model.resolution` | COMBO | 예 | `"720P"`<br>`"1080P"` | 출력 비디오의 해상도입니다. (기본값: "720P") |
| `model.duration` | INT | 예 | 3 ~ 15 | 생성된 비디오의 길이(초)입니다. (기본값: 5) |
| `first_frame` | IMAGE | 예 | 해당 없음 | 첫 번째 프레임 이미지입니다. 출력 화면 비율은 이 이미지에서 파생됩니다. |
| `seed` | INT | 아니요 | 0 ~ 2147483647 | 생성에 사용할 시드 값입니다. (기본값: 0) |
| `watermark` | BOOLEAN | 아니요 | True / False | 결과물에 AI 생성 워터마크를 추가할지 여부입니다. (기본값: False) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `video` | VIDEO | 생성된 비디오 파일입니다. |

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`
