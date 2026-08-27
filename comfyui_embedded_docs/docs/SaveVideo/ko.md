# 비디오 저장

Save Video 노드는 입력 비디오를 ComfyUI 출력 디렉토리에 저장합니다. 파일 이름 접두사, 컨테이너 형식, 비디오 코덱, 품질 및 색 공간과 같은 인코딩 옵션을 선택할 수 있습니다. 이 노드는 카운터 증가를 통해 파일 이름을 자동으로 처리하며 저장된 파일에 워크플로우 메타데이터를 포함할 수 있습니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `비디오` | 저장할 비디오입니다. | VIDEO | 예 | - |
| `파일명 접두사` | 저장할 파일의 접두사입니다. `%date:yyyy-MM-dd%` 또는 `%Empty Latent Image.width%`와 같은 형식 정보를 포함하여 노드의 값을 포함할 수 있습니다 (기본값: "video/ComfyUI"). | STRING | 예 | - |
| `포맷` | 출력 컨테이너입니다. 자동(auto)은 가능한 경우 소스 컨테이너를 유지하며, MP4, MKV 및 WebM은 특정 컨테이너를 선택합니다 (기본값: "auto"). | DYNAMIC_COMBO | 예 | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `코덱` | 출력 비디오 코덱입니다. 자동(auto)은 호환 가능한 소스 스트림을 유지합니다. H.264 및 AV1 재인코딩은 SDR, HDR(HLG) 및 HDR PQ를 지원합니다. 형식이 선택된 경우 나타납니다 (기본값: "auto"). | DYNAMIC_COMBO | 아니요 | `"auto"`<br>`"h264"`<br>`"av1"` |

### H.264 입력

이 입력은 `codec`이 `"h264"`일 때 나타납니다. 이 코덱은 `auto`, `mp4` 및 `mkv` 형식과 함께 사용할 수 있습니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `encoding` | 자동(auto)은 호환되는 H.264 스트림을 유지합니다. 재인코딩(re-encode)은 사용자 지정 인코딩 옵션을 적용합니다. | DYNAMIC_COMBO | 아니요 | `"auto"`<br>`"re-encode"` |
| `crf` | 값이 낮을수록 더 높은 품질과 더 큰 파일이 생성됩니다. `encoding`이 `"re-encode"`일 때 나타납니다 (기본값: 23.0). | FLOAT | 아니요 | 0.0 ~ 51.0 |
| `color_space` | 자동(auto)은 이미지로 생성된 비디오에는 sRGB를 사용하고 로드된 비디오의 인식된 색상을 유지합니다. sRGB는 SDR BT.709/sRGB로 기록합니다. HDR은 10비트 BT.2020/HLG로 기록하며, HDR PQ는 BT.2020/PQ로 기록합니다. 기타 입력 픽셀은 이미 선택된 색 공간을 사용하고 있어야 합니다. `encoding`이 `"re-encode"`일 때 나타납니다 (기본값: "auto"). | COMBO | 아니요 | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

### AV1 입력

이 입력은 `codec`이 `"av1"`일 때 나타납니다. 이 코덱은 `auto`, `mp4`, `mkv` 및 `webm` 형식과 함께 사용할 수 있습니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `encoding` | 자동(auto)은 호환되는 AV1 스트림을 유지합니다. 재인코딩(re-encode)은 사용자 지정 인코딩 옵션을 적용합니다. | DYNAMIC_COMBO | 아니요 | `"auto"`<br>`"re-encode"` |
| `crf` | 값이 낮을수록 더 높은 품질과 더 큰 파일이 생성됩니다. `encoding`이 `"re-encode"`일 때 나타납니다 (기본값: 30.0). | FLOAT | 아니요 | 0.0 ~ 63.0 |
| `color_space` | 자동(auto)은 이미지로 생성된 비디오에는 sRGB를 사용하고 로드된 비디오의 인식된 색상을 유지합니다. sRGB는 SDR BT.709/sRGB로 기록합니다. HDR은 10비트 BT.2020/HLG로 기록하며, HDR PQ는 BT.2020/PQ로 기록합니다. 기타 입력 픽셀은 이미 선택된 색 공간을 사용하고 있어야 합니다. `encoding`이 `"re-encode"`일 때 나타납니다 (기본값: "auto"). | COMBO | 아니요 | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

참고: `webm` 형식은 `auto` 및 `av1` 코덱만 지원합니다. `format`이 `"auto"`인 경우 가능하면 소스 컨테이너가 유지됩니다. `color_space`가 `"auto"`인 경우 명시적인 색 공간이 적용되지 않으며 색 공간이 자동으로 결정됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `video` | 변경되지 않은 입력 비디오입니다. | VIDEO |
| `ui` | UI에 표시하기 위한 파일 경로 및 하위 폴더 정보를 포함하여 저장된 비디오 파일의 미리보기입니다. | PREVIEW_VIDEO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/ko.md)

---
**Source fingerprint (SHA-256):** `39b168eab2d6798adfec6ace3d4320f26217d893844ba54e62041cfdf0183e6f`
