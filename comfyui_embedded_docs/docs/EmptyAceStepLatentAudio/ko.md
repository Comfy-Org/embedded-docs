# EmptyAceStepLatentAudio

EmptyAceStepLatentAudio 노드는 지정된 지속 시간의 빈 잠재 오디오 샘플을 생성합니다. 0으로 채워진 무음 오디오 잠재 배치를 생성하며, 길이는 입력된 초(seconds) 값과 오디오 처리 매개변수를 기반으로 계산됩니다. 이 노드는 잠재 표현이 필요한 오디오 처리 워크플로우를 초기화하는 데 유용합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `seconds` | 오디오 지속 시간(초) (기본값: 120.0) | FLOAT | 예 | 1.0 - 1000.0 (step 0.1) |
| `batch_size` | 배치 내 잠재 이미지 수 (기본값: 1) | INT | 예 | 1 - 4096 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 0으로 채워진 빈 잠재 오디오 샘플을 반환합니다. 출력에는 `samples` 텐서와 "audio"로 설정된 `type` 필드가 포함됩니다. | LATENT |

참고: 잠재 길이는 내부 샘플 레이트 44100Hz를 사용하여 `seconds` 값으로부터 산출됩니다. 즉, `int(seconds × 44100 / 512 / 8)` 프레임으로 계산됩니다. 결과 잠재 텐서는 0으로 완전히 채워집니다.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/ko.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
