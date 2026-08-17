# NormalizeVideoLatentStart

이 노드는 비디오 잠재 표현의 처음 몇 프레임을 조정하여 이후 프레임처럼 보이도록 만듭니다. 비디오의 뒷부분에 있는 일련의 참조 프레임에서 평균과 변화량을 계산하고, 이러한 동일한 특성을 시작 프레임에 적용합니다. 이를 통해 비디오 시작 부분에서 더 부드럽고 일관된 시각적 전환이 만들어집니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `latent` | 처리할 비디오 잠재 표현입니다. | LATENT | 예 | - |
| `start_frame_count` | 시작 지점부터 정규화할 잠재 프레임 수입니다(기본값: 4). | INT | 예 | 1 to 16384 (최대 해상도) |
| `reference_frame_count` | 시작 프레임 이후에 참조로 사용할 잠재 프레임 수입니다(기본값: 5). | INT | 예 | 1 to 16384 (최대 해상도) |

**참고:** `reference_frame_count`는 시작 프레임 이후에 사용 가능한 프레임 수로 자동 제한됩니다. 비디오 잠재 표현이 1프레임뿐인 경우 정규화가 수행되지 않으며 원래 잠재 표현이 변경 없이 반환됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `latent` | 시작 프레임이 정규화된 처리된 비디오 잠재 표현입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/ko.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
