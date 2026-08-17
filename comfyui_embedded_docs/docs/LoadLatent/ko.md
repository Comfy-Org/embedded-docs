# 잠재 데이터 로드

LoadLatent 노드는 입력 디렉토리에 .latent 파일로 이전에 저장된 잠재 표현을 로드합니다. 선택한 파일에서 잠재 텐서 데이터를 읽고 필요한 크기 조정을 적용한 후 다른 노드에서 사용할 수 있도록 결과를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `latent` | 입력 디렉토리의 사용 가능한 파일 중에서 로드할 .latent 파일을 선택합니다. | COMBO | 예 | 입력 디렉토리의 모든 .latent 파일 |

참고: `latent_format_version_0` 마커를 포함하지 않는 .latent 파일의 경우, 로드된 잠재 텐서에 1/0.18215를 곱하여 다른 노드에서 기대하는 형식과 크기 조정이 일치하도록 합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `LATENT` | 선택한 파일에서 로드된 잠재 표현 데이터를 반환합니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/ko.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
