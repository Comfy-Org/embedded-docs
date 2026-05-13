> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/en.md)

이 노드는 Kling AI 모델을 사용하여 입력 비디오와 선택적 참조 이미지를 기반으로 새로운 비디오를 생성합니다. 원하는 콘텐츠를 설명하는 텍스트 프롬프트를 제공하면 노드가 참조 비디오를 그에 맞게 변환합니다. 또한 최대 4개의 추가 참조 이미지를 통합하여 출력의 스타일과 콘텐츠를 안내할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 예 | `"kling-v3-omni"`<br>`"kling-video-o1"` | 비디오 생성에 사용할 특정 Kling 모델입니다(기본값: "kling-v3-omni"). |
| `prompt` | STRING | 예 | 해당 없음 | 비디오 콘텐츠를 설명하는 텍스트 프롬프트입니다. 긍정적 설명과 부정적 설명을 모두 포함할 수 있습니다. |
| `aspect_ratio` | COMBO | 예 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 생성된 비디오의 원하는 화면 비율입니다. |
| `duration` | INT | 예 | 3~10 | 생성된 비디오의 길이(초)입니다(기본값: 3). |
| `reference_video` | VIDEO | 예 | 해당 없음 | 참조로 사용할 비디오입니다. |
| `keep_original_sound` | BOOLEAN | 예 | 해당 없음 | 출력에서 참조 비디오의 오디오를 유지할지 여부를 결정합니다(기본값: True). |
| `reference_images` | IMAGE | 아니요 | 해당 없음 | 최대 4개의 추가 참조 이미지입니다. |
| `resolution` | COMBO | 아니요 | `"1080p"`<br>`"720p"` | 생성된 비디오의 해상도입니다(기본값: "1080p"). |
| `seed` | INT | 아니요 | 0~2147483647 | 시드는 노드 재실행 여부를 제어합니다. 시드와 관계없이 결과는 비결정적입니다(기본값: 0). |

**매개변수 제약 조건:**

* `prompt`는 1자에서 2500자 사이여야 합니다.
* `reference_video`의 길이는 3.0초에서 10.05초 사이여야 합니다.
* `reference_video`의 크기는 720x720픽셀에서 2160x2160픽셀 사이여야 합니다.
* 최대 4개의 `reference_images`를 제공할 수 있습니다. 각 이미지는 최소 300x300픽셀이어야 하며 화면 비율이 1:2.5에서 2.5:1 사이여야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 새로 생성된 비디오입니다. |

---
**Source fingerprint (SHA-256):** `1bed976530603bcf7db67048e89ad6adac218fba8597744f8ece3e16a2ee4993`
