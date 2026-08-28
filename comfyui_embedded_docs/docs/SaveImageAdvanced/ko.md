# 이미지 저장 (고급)

**Save Image (Advanced)** 노드는 입력 이미지를 ComfyUI 출력 디렉터리에 저장하며, 파일 형식, 비트 심도, 색 공간을 고급 수준으로 제어할 수 있습니다. PNG 또는 EXR 파일로 저장할 수 있으며 워크플로 메타데이터를 저장된 파일에 포함할 수 있습니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `images` | 저장할 이미지입니다. | IMAGE | 예 | - |
| `filename_prefix` | 저장할 파일의 접두사입니다. `%date:yyyy-MM-dd%` 또는 `%Empty Latent Image.width%`와 같은 형식 토큰을 포함할 수 있습니다. (기본값: "ComfyUI") | STRING | 예 | - |
| `format` | 이미지를 저장할 파일 형식입니다. 형식을 선택하면 해당 형식에 대한 추가 옵션이 표시됩니다. | DYNAMIC_COMBO | 예 | `"png"`<br>`"exr"` |

### PNG 입력

다음 옵션은 `format`이 `"png"`로 설정된 경우 표시됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 저장할 PNG 파일의 비트 심도입니다. (기본값: "8-bit") | COMBO | 예 (조건부) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | 입력 텐서의 색 공간입니다. PNG 형식에서는 sRGB만 사용할 수 있습니다. (기본값: "sRGB") | COMBO | 예 (조건부) | `"sRGB"` |

### EXR 입력

다음 옵션은 `format`이 `"exr"`로 설정된 경우 표시됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 저장할 EXR 파일의 비트 심도입니다. (기본값: "32-bit float") | COMBO | 예 (조건부) | `"32-bit float"` |
| `input_color_space` | 입력 텐서의 색 공간입니다. EXR은 항상 해당 색역(gamut)의 장면-선형(scene-linear)으로 기록됩니다.<br>`"sRGB"` — 입력이 sRGB 인코딩된 Rec.709입니다. 역 sRGB EOTF가 적용됩니다.<br>`"HDR"` — 입력이 HLG 인코딩된 Rec.2020(BT.2100)입니다. 역 HLG OETF가 적용되어 장면-선형 광도를 얻습니다.<br>`"linear"` — 입력이 이미 장면-선형(Rec.709 기본색)이며 변경 없이 기록됩니다. 렌더러/합성기 출력에 사용하십시오. (기본값: "sRGB") | COMBO | 예 (조건부) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**매개변수 의존성에 대한 참고 사항:**
- `bit_depth` 및 `input_color_space` 매개변수는 특정 `format`이 선택된 경우에만 사용할 수 있습니다.
- PNG 형식의 경우 "8-bit" 및 "16-bit" 비트 심도만 사용할 수 있으며 색 공간은 "sRGB"만 사용할 수 있습니다.
- EXR 형식의 경우 "32-bit float" 비트 심도만 사용할 수 있으며 색 공간은 "sRGB", "HDR" 또는 "linear"입니다.
- 이미지는 1(회색조), 3(RGB) 또는 4(RGBA) 채널을 가져야 합니다. 다른 채널 수는 지원되지 않으며 오류가 발생합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `images` | 변경 없이 전달되는 입력 이미지입니다. 노드의 UI 출력은 저장된 이미지 결과 목록을 제공하며, 각 결과에는 파일명, 하위 폴더 및 유형("output")이 포함됩니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/ko.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
