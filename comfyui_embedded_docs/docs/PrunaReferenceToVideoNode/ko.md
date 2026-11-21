# Pruna P-Video-2 Pro Reference to Video

## 입력

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | 사용할 Pruna 비디오 모델입니다. 모델을 선택하면 아래에 해당 입력이 표시됩니다. | DYNAMIC_COMBO | 예 | `"p-video-2-pro-reference"` |

### P-Video-2 Pro Reference 입력

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model.images` | 참조 이미지용 확장 가능한 슬롯입니다(`image_1`, `image_2`, ...). 프롬프트에서는 연결 순서에 따라 `@Image1`부터 `@Image9`까지로 참조합니다. 첫 프레임과 마지막 프레임을 포함하여 최대 9개 이미지까지 사용할 수 있습니다. | AUTOGROW | 아니요 | 0~9개 이미지 |
| `model.videos` | 참조 비디오용 확장 가능한 슬롯입니다(`video_1`, `video_2`, ...). `@Video1`부터 `@Video3`까지로 참조합니다. 각 비디오는 최대 60fps로 2~15초이며, 총 15초까지입니다. 1080p를 초과하는 비디오는 축소됩니다. | AUTOGROW | 아니요 | 0~3개 비디오 |
| `model.audios` | 참조 오디오용 확장 가능한 슬롯입니다(`audio_1`, `audio_2`, ...). `@Audio1`부터 `@Audio3`까지로 참조합니다. 총 15초까지입니다. | AUTOGROW | 아니요 | 0~3개 오디오 클립 |
| `model.prompt` | 비디오를 설명합니다. 참조 항목은 `@Image1`, `@Video1` 또는 `@Audio1`로 참조합니다(기본값: 비어 있음). 최대 5000자까지 입력할 수 있습니다. | STRING | 예 | 1~5000자 |
| `model.first_frame` | 비디오가 시작되는 이미지입니다. 9개 이미지 제한에 포함됩니다. | IMAGE | 아니요 | - |
| `model.last_frame` | 비디오가 끝나는 이미지입니다. 9개 이미지 제한에 포함됩니다. | IMAGE | 아니요 | - |
| `model.keep_audio` | 연결된 오디오를 사운드트랙으로 사용하고 이에 맞춰 비디오를 생성합니다(기본값: False). 오디오는 정확히 하나만 필요합니다. 오디오가 더 짧으면 생성된 사운드가 뒤따르고, 더 길면 비디오 길이에 맞게 잘립니다. | BOOLEAN | 예 | `True`<br>`False` |
| `model.duration` | 비디오 길이(초)입니다(기본값: `"5"`). | COMBO | 예 | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"` |
| `model.resolution` | 출력 해상도입니다(기본값: `"768p"`). 1080p, 2k, 4k는 생성된 768p 비디오를 업스케일합니다. | COMBO | 예 | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `model.mode` | `"cost"`는 더 저렴하고, `"speed"`는 더 빠르게 렌더링합니다(기본값: `"speed"`). | COMBO | 예 | `"cost"`<br>`"speed"` |
| `model.aspect_ratio` | 출력 비디오의 종횡비입니다(기본값: `"16:9"`). `"adaptive"`는 참조 항목들 중 가장 흔한 비율을 사용하며, `enhance_prompt`가 켜져 있으면 재작성된 프롬프트가 대신 비율을 선택합니다. | COMBO | 예 | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `model.enhance_prompt` | 생성 전에 프롬프트를 더 자세하게 재작성합니다. `"max"`는 더 느립니다(기본값: `"turbo"`). 프롬프트에서 참조 항목을 번호로 지칭하는 경우에는 켜 두십시오. 첫 프레임이나 마지막 프레임이 있는 경우 항상 `"turbo"`를 사용합니다. 고급 설정입니다. | COMBO | 예 | `"off"`<br>`"turbo"`<br>`"max"` |
| `model.seed` | 생성용 시드입니다(기본값: 42). 동일한 시드는 `model.enhance_prompt`가 꺼져 있을 때만 결과를 정확히 재현합니다. | INT | 예 | 0 ~ 2147483647<br>단계: 1 |

**참고:**

- 참조 이미지, 비디오, 첫 프레임 또는 마지막 프레임 중 하나 이상을 연결해야 합니다. 그렇지 않으면 노드가 오류와 함께 중지됩니다.
- 첫 프레임과 마지막 프레임을 포함하여 이미지 9개까지 허용되며, 이미지, 프레임, 비디오, 오디오를 통틀어 총 12개의 참조가 허용됩니다.
- 참조 비디오와 참조 오디오는 각각 총 15초로 제한되며, 각 참조 비디오는 최대 60fps에서 2~15초 길이여야 합니다.

## 출력

| Output Name | Description | Data Type |
| --- | --- | --- |
| `video` | 생성된 비디오입니다. | VIDEO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaReferenceToVideoNode/ko.md)

---
**Source fingerprint (SHA-256):** `d6e295b394984c924386ea6432532c7653b4512c646b1f86793be9b98583eef3`
