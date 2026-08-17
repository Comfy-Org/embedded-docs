# 오디오 인코더 인코딩

AudioEncoderEncode 노드는 오디오 인코더 모델을 사용하여 오디오 데이터를 인코딩합니다. 오디오 입력을 받아 인코딩된 표현으로 변환하며, 이 표현은 컨디셔닝 파이프라인에서 추가 처리에 사용될 수 있습니다. 이 노드는 원시 오디오 파형을 오디오 기반 머신러닝 애플리케이션에 적합한 형식으로 변환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `audio_encoder` | 오디오 입력을 처리하는 데 사용되는 오디오 인코더 모델 | AUDIO_ENCODER | 예 | - |
| `audio` | 파형 및 샘플 레이트 정보를 포함하는 오디오 데이터 | AUDIO | 예 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 오디오 인코더에 의해 생성된 인코딩된 오디오 표현 | AUDIO_ENCODER_OUTPUT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/ko.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
