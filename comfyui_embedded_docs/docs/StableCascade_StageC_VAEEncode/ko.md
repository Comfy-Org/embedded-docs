> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/ko.md)

StableCascade_StageC_VAEEncode 노드는 Stable Cascade 모델을 위한 잠재 표현을 생성하기 위해 VAE 인코더를 통해 이미지를 처리합니다. 입력 이미지를 받아 지정된 VAE 모델을 사용하여 압축한 후, 두 가지 잠재 표현을 출력합니다: 하나는 스테이지 C용이고 다른 하나는 스테이지 B용 자리 표시자입니다. compression 매개변수는 인코딩 전에 이미지가 축소되는 정도를 제어합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `이미지` | IMAGE | 예 | - | 잠재 공간으로 인코딩될 입력 이미지 |
| `vae` | VAE | 예 | - | 이미지 인코딩에 사용되는 VAE 모델 |
| `압축` | INT | 아니오 | 4-128 | 인코딩 전에 이미지에 적용되는 압축 계수 (기본값: 42) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `StageB 잠재 이미지` | LATENT | Stable Cascade 모델의 스테이지 C용으로 인코딩된 잠재 표현 |
| `stage_b` | LATENT | 스테이지 B용 자리 표시자 잠재 표현 (현재는 0을 반환합니다) |
