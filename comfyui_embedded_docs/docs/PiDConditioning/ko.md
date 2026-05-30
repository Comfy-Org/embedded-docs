> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/ko.md)

## 개요

잠재 이미지와 열화 시그마 값을 CONDITIONING 데이터에 첨부합니다. 이는 PiD(Pixel-in-Detail) 디코딩 또는 업스케일링에 사용되며, 처리 전 잠재 이미지의 열화 정도를 제어할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `포지티브` | CONDITIONING | 예 | - | 잠재 이미지와 열화 시그마를 첨부할 컨디셔닝 데이터입니다. |
| `latent` | LATENT | 예 | - | 컨디셔닝에 첨부할 잠재 이미지(VAEEncode 또는 KSampler에서 생성)입니다. |
| `latent_format` | COMBO | 예 | `"flux"`<br>`"sd3"` | 잠재 이미지의 형식입니다. Flux1 및 Flux2 잠재 이미지는 채널 차원에서 자동으로 감지됩니다. SD3는 수동으로 선택해야 합니다(기본값: "flux"). |
| `degrade_sigma` | FLOAT | 예 | 0.0 ~ 1.0 (단위: 0.01) | 적용할 열화 정도입니다. 0은 깨끗한 잠재 이미지를 의미합니다. 손상된 잠재 이미지 출력을 노이즈 제거하려면 이 값을 높이십시오(기본값: 0.0). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 잠재 이미지와 열화 시그마 값이 첨부된 원본 컨디셔닝 데이터입니다. |

---
**Source fingerprint (SHA-256):** `7c8de543629c2299fc2c1e035e433dfc249af594773a77e65c69dde67eb104d7`
