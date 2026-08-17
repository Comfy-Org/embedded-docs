# 빈 훈위안 이미지 잠재

EmptyHunyuanImageLatent 노드는 Hunyuan 이미지 생성 모델에 사용할 특정 차원의 빈 잠재 텐서를 생성합니다. 워크플로우의 후속 노드에서 처리할 수 있는 빈 시작점을 생성합니다. 이 노드를 사용하면 잠재 공간의 너비, 높이 및 배치 크기를 지정할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `width` | 생성된 잠재 이미지의 픽셀 단위 너비입니다 (기본값: 2048, 스텝: 32) | INT | 예 | 64 to MAX_RESOLUTION |
| `height` | 생성된 잠재 이미지의 픽셀 단위 높이입니다 (기본값: 2048, 스텝: 32) | INT | 예 | 64 to MAX_RESOLUTION |
| `batch_size` | 배치로 생성할 잠재 샘플 수입니다 (기본값: 1) | INT | 예 | 1 to 4096 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `LATENT` | Hunyuan 이미지 처리를 위해 지정된 차원의 빈 잠재 텐서입니다. 이 텐서는 64개의 채널을 가지며 공간 차원은 요청된 너비와 높이의 1/32입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/ko.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
