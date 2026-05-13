> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/ko.md)

이 문서는 AI로 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/en.md)

이 노드는 Bria RMBG 2.0 서비스를 사용하여 이미지에서 배경을 제거합니다. 이미지를 외부 API로 전송하여 처리한 후 배경이 제거된 결과를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 배경을 제거할 입력 이미지입니다. |
| `moderation` | COMBO | 아니요 | `"false"`<br>`"true"` | 검열 설정입니다. `"true"`로 설정하면 추가 검열 옵션을 사용할 수 있습니다. |
| `visual_input_moderation` | BOOLEAN | 아니요 | - | 입력 이미지에 대한 시각적 콘텐츠 검열을 활성화합니다. 이 매개변수는 `moderation`이 `"true"`로 설정된 경우에만 사용할 수 있습니다. 기본값: `False`. |
| `visual_output_moderation` | BOOLEAN | 아니요 | - | 출력 이미지에 대한 시각적 콘텐츠 검열을 활성화합니다. 이 매개변수는 `moderation`이 `"true"`로 설정된 경우에만 사용할 수 있습니다. 기본값: `True`. |
| `seed` | INT | 아니요 | 0 ~ 2147483647 | 노드를 다시 실행할지 여부를 제어하는 시드 값입니다. 시드 값과 관계없이 결과는 비결정적입니다. 기본값: `0`. |

**참고:** `visual_input_moderation` 및 `visual_output_moderation` 매개변수는 `moderation` 매개변수에 종속됩니다. 이 매개변수들은 `moderation`이 `"true"`로 설정된 경우에만 활성화되며 필요합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | 배경이 제거된 처리된 이미지입니다. |

---
**Source fingerprint (SHA-256):** `2b2dd3ca0d026af1a2bf3f7222165928527b05b65817073b50230ff18d39bc6c`
