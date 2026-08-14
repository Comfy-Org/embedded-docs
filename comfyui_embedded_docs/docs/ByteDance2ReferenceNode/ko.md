# ByteDance Seedance 2.0 레퍼런스에서 비디오 생성

이 노드는 ByteDance의 Seedance 2.5 또는 2.0 AI 모델을 사용하여 비디오를 생성, 편집 또는 확장합니다. 텍스트 프롬프트로 비디오를 설명하고 참조 이미지, 비디오 및 오디오를 추가하여 결과를 안내할 수 있습니다. 멀티모달 참조 입력, 비디오 편집 및 비디오 확장을 지원합니다.

## 입력

`model`을 선택하면 아래 매개변수 중 사용 가능한 항목이 결정됩니다. `video_editing` 및 `output_format`은 Seedance 2.5를 선택한 경우에만 표시됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 비디오 생성에 사용되는 AI 모델입니다. Seedance 2.5는 최대 30초 비디오와 mp4/mov 출력을 지원하는 최신 모델입니다. Seedance 2.0은 최고 품질과 1080p/4k를 위한 모델이며, Fast는 속도 최적화를 위한 모델이고, Mini는 가장 빠르고 저렴한 생성을 위한 모델입니다. 모델을 선택하면 아래에 나열된 모델별 입력이 표시됩니다. | COMBO | 예 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | 시드는 노드 재실행 여부를 제어합니다. 시드와 관계없이 결과는 비결정적입니다(기본값: 0). | INT | 예 | 0 ~ 2147483647 |
| `watermark` | 비디오에 워터마크를 추가할지 여부입니다(기본값: False). | BOOLEAN | 예 | `True`<br>`False` |
| `prompt` | 비디오 생성을 위한 텍스트 프롬프트입니다. Seedance 2.5에서는 생성된 대화를 유도하기 위해 말하는 대사를 큰따옴표로 묶으십시오. 공백이 아닌 문자를 하나 이상 포함해야 합니다. | STRING | 예 | 모든 텍스트 |
| `resolution` | 출력 비디오의 해상도입니다. Seedance 2.5, 2.0 Fast 및 2.0 Mini는 480p와 720p를 제공하며, Seedance 2.0은 1080p와 4k도 제공합니다(Seedance 2.5 기본값: 720p). | COMBO | 예 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 출력 비디오의 화면 비율입니다(Seedance 2.5 기본값: `"16:9"`, Seedance 2.0 모델 기본값: `"adaptive"`). | COMBO | 예 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 출력 비디오의 길이(초)입니다(Seedance 2.5: 4-30, 기본값 5, Seedance 2.0 모델: 4-15, 기본값 7). | INT | 예 | 4 ~ 30 (Seedance 2.5)<br>4 ~ 15 (Seedance 2.0)<br>Step: 1 |
| `generate_audio` | 출력 비디오에 대한 오디오 생성을 활성화합니다(기본값: True). | BOOLEAN | 예 | `True`<br>`False` |
| `video_editing` | Seedance 2.5 전용입니다. 프롬프트가 연결된 참조 비디오를 편집하는 경우, 예를 들어 비디오의 객체를 교체하는 경우 활성화합니다. 활성화하면 출력이 소스 클립의 고유 길이와 화면 비율을 유지하며, duration 및 ratio 위젯은 무시됩니다. 새 비디오를 생성하거나 설정한 길이로 비디오를 확장하려면 비활성화된 상태로 두십시오(기본값: False). | BOOLEAN | 예 | `True`<br>`False` |
| `output_format` | Seedance 2.5 전용입니다. 출력 비디오의 컨테이너 형식입니다(기본값: `"mp4"`). | COMBO | 예 | `"mp4"` |
| `reference_images` | 비디오 생성을 안내하는 참조 이미지입니다. 이미지의 최대 변이 6000픽셀을 넘지 않도록 자동 축소되며, 최소 300x300픽셀 이상이어야 하고 화면 비율이 0.4~2.5 사이여야 합니다. | IMAGE | 아니요 | 최대 30 (Seedance 2.5)<br>최대 9 (Seedance 2.0) |
| `reference_videos` | 비디오 생성을 안내하는 참조 비디오입니다. 비디오 편집 및 확장에 사용됩니다. | VIDEO | 아니요 | 최대 10 (Seedance 2.5)<br>최대 3 (Seedance 2.0) |
| `reference_audios` | 비디오 생성을 안내하는 참조 오디오 클립입니다. | AUDIO | 아니요 | 최대 10 (Seedance 2.5)<br>최대 3 (Seedance 2.0) |
| `auto_downscale` | 선택한 해상도에 대한 모델의 픽셀 예산을 초과하는 참조 비디오를 자동으로 축소합니다. 화면 비율은 유지되며 이미 한도 내에 있는 비디오는 변경되지 않습니다(기본값: True). | BOOLEAN | 아니요 | `True`<br>`False` |
| `auto_upscale` | 선택한 해상도에 대한 모델의 최소 픽셀 수 미만인 참조 비디오를 자동으로 확대합니다. 화면 비율은 유지되며 이미 최소 기준을 충족하는 비디오는 변경되지 않습니다. 참고: 저해상도 소스를 확대해도 실제 디테일이 추가되지 않으며 품질이 낮은 생성 결과가 나올 수 있습니다(기본값: False). | BOOLEAN | 아니요 | `True`<br>`False` |
| `reference_assets` | 참조로 사용할 이전에 생성된 Seedance 가상 라이브러리 자산(Image, Video 또는 Audio)의 ID입니다. 각 자산은 존재해야 하며 Active 상태여야 합니다. 프롬프트에서 자산은 asset1, asset 2 등으로 참조할 수 있습니다. 노드는 이러한 토큰을 Image 2와 같은 레이블로 대체합니다. | STRING | 아니요 | 최대 30 (Seedance 2.5)<br>최대 9 (Seedance 2.0) |

**중요 제약 사항:**

* 최소 하나의 참조가 필요합니다. Seedance 2.0, 2.0 Fast 및 2.0 Mini의 경우 `reference_images`, `reference_videos` 또는 이미지/비디오 `reference_assets` 항목을 통해 최소 하나의 이미지 또는 비디오 참조를 제공해야 합니다. Seedance 2.5는 오디오 전용 참조도 추가로 허용합니다.
* 참조 개수는 모델에 따라 다릅니다. Seedance 2.5는 최대 30개의 `reference_images`, 10개의 `reference_videos`, 10개의 `reference_audios` 및 30개의 `reference_assets`를 허용합니다. Seedance 2.0 모델은 최대 9개의 이미지, 3개의 비디오, 3개의 오디오 클립 및 9개의 자산을 허용합니다. 총 개수는 직접 입력과 자산 참조를 합산하여 계산되며 생성 전에 검증됩니다.
* 각 참조 비디오는 최소 1.8초 이상이어야 하며, 각 참조 오디오 클립도 최소 1.8초 이상이어야 합니다. 모든 참조 비디오와 참조 오디오의 총 길이는 선택한 모델의 한도(Seedance 2.0 모델의 경우 15.1초)를 초과할 수 없습니다.
* 참조 비디오는 선택한 해상도에 대한 모델의 픽셀 수 한도도 충족해야 합니다. `auto_downscale`이 활성화된 경우(기본값) 한도를 초과하는 비디오는 자동으로 크기가 조정되며, `auto_upscale`이 활성화된 경우 최소 크기 미만의 비디오는 확대됩니다. 자동 조정 중 하나라도 비활성화된 경우 해당 한도를 벗어나는 비디오는 오류를 발생시킵니다.
* Seedance 2.5에서 `video_editing`이 활성화되면 `duration` 및 `ratio` 입력은 무시되며 출력은 참조 비디오의 고유 길이와 화면 비율을 따릅니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `video` | 생성된 비디오 파일입니다. | VIDEO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/ko.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
