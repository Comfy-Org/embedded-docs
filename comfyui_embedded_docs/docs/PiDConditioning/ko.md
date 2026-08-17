# PiD 컨디셔닝

잠재 이미지와 디그레이드 시그마(degrade sigma) 값을 CONDITIONING 데이터에 첨부합니다. 이는 PiD(Pixel-in-Detail) 디코딩 또는 업스케일링에 사용되며, 처리 전에 잠재 이미지가 얼마나 디그레이드될지 제어할 수 있게 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 잠재 이미지와 디그레이드 시그마를 첨부할 CONDITIONING 데이터입니다. | CONDITIONING | 예 | - |
| `latent` | CONDITIONING에 첨부할 잠재 이미지(VAEEncode 또는 KSampler에서 생성된)입니다. | LATENT | 예 | - |
| `latent_format` | 잠재 이미지의 형식입니다. Flux1(16채널) 및 Flux2(128채널) 잠재 이미지는 "flux"의 채널 차원에서 자동으로 감지됩니다. SD3(16채널), SDXL(4채널) 또는 QwenImage(16채널)의 경우 수동으로 선택합니다(기본값: "flux"). | COMBO | 예 | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0은 깨끗한 잠재 이미지를 의미합니다. 손상된 잠재 출력을 디노이즈하려면 값을 증가시키십시오(기본값: 0.0). | FLOAT | 예 | 0.0~1.0(단계: 0.01) |

참고: `latent_format`이 "flux"인 경우, 노드는 채널 차원을 기준으로 잠재 이미지가 Flux1(16채널)인지 Flux2(128채널)인지 자동으로 감지합니다. 처리된 잠재 이미지가 5차원인 경우, 마지막 차원의 첫 번째 슬라이스만 사용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `CONDITIONING` | 잠재 이미지와 디그레이드 시그마 값이 첨부된 원본 CONDITIONING 데이터입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/ko.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
