# ReferenceTimbreAudio

이 노드는 "ace step 1.5" 프로세스에서 사용할 기준 오디오 음색을 설정합니다. conditioning 입력과 오디오의 선택적 잠재 표현(latent representation)을 받은 다음, 해당 잠재 데이터를 conditioning에 첨부하여 워크플로우의 후속 노드에서 기준 오디오로 사용할 수 있게 합니다. latent가 제공되지 않으면 conditioning은 변경 없이 반환됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `conditioning` | 기준 오디오 정보가 첨부될 conditioning 데이터입니다. | CONDITIONING | 예 |  |
| `latent` | 기준 오디오의 선택적 잠재 표현입니다. 제공되면 해당 샘플이 conditioning에 추가됩니다. | LATENT | 아니요 |  |

`latent`가 제공되면 해당 샘플이 conditioning의 기준 오디오 음색 잠재 변수에 추가됩니다. `latent`가 제공되지 않으면 원래 conditioning이 변경 없이 그대로 전달됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `conditioning` | 선택적 `latent` 입력이 제공된 경우 기준 오디오 음색 잠재 변수를 포함하는 수정된 conditioning 데이터입니다. latent가 제공되지 않으면 원래 conditioning이 변경 없이 반환됩니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/ko.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
