> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/en.md)

이 노드는 제공된 참조 자료를 기반으로 사람이나 사물이 등장하는 비디오를 생성합니다. Wan 2.7 모델을 사용하여 텍스트 프롬프트로부터 비디오를 생성하며, 단일 캐릭터 퍼포먼스와 다중 캐릭터 상호작용을 지원합니다. 생성이 작동하려면 최소한 하나의 참조 비디오 또는 이미지를 제공해야 합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `"wan2.7-r2v"` | 비디오 생성에 사용할 특정 모델입니다. |
| `model.prompt` | STRING | 예 | - | 비디오를 설명하는 프롬프트입니다. 'character1', 'character2'와 같은 식별자를 사용하여 참조 캐릭터를 지칭합니다. |
| `model.negative_prompt` | STRING | 아니요 | - | 생성된 비디오에서 피해야 할 내용을 설명하는 네거티브 프롬프트입니다(기본값: 비어 있음). |
| `model.resolution` | COMBO | 예 | `"720P"`<br>`"1080P"` | 출력 비디오의 해상도입니다. |
| `model.ratio` | COMBO | 예 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 출력 비디오의 화면 비율입니다. |
| `model.duration` | INT | 예 | 2 ~ 10 | 생성된 비디오의 길이(초)입니다(기본값: 5). |
| `model.reference_videos` | VIDEO | 아니요 | - | 참조 비디오 목록입니다. 최대 3개의 비디오를 추가할 수 있습니다. |
| `model.reference_images` | IMAGE | 아니요 | - | 참조 이미지 목록입니다. 최대 5개의 이미지를 추가할 수 있습니다. |
| `seed` | INT | 아니요 | 0 ~ 2147483647 | 생성에 사용할 시드로, 출력의 무작위성을 제어하는 데 도움이 됩니다(기본값: 0). |
| `watermark` | BOOLEAN | 아니요 | - | 결과물에 AI 생성 워터마크를 추가할지 여부입니다(기본값: False). 고급 설정입니다. |

**중요 제약 사항:**
*   `model.reference_videos` 또는 `model.reference_images` 입력에 최소한 하나의 참조 비디오 또는 참조 이미지를 제공해야 합니다.
*   참조 비디오와 이미지의 총 개수는 5개를 초과할 수 없습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 파일입니다. |

---
**Source fingerprint (SHA-256):** `f28a765e310410fc62241e11dbfe25562c7ae16e8e6ffbfb004face7a7e2b727`
