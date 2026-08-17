# 빈 색조 복사 잠재 이미지

## EmptyChromaRadianceLatentImage

EmptyChromaRadianceLatentImage 노드는 크로마 래디언스(chroma radiance) 워크플로우에서 사용할 수 있도록 지정된 크기의 빈 잠재 이미지를 생성합니다. 이 노드는 0으로 채워진 텐서(3개의 색상 채널 포함)를 생성하여 잠재 공간 작업을 위한 시작점으로 제공합니다. 이 노드를 사용하면 빈 잠재 이미지의 너비, 높이 및 배치 크기를 정의할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `width` | 잠재 이미지의 너비(픽셀 단위)입니다. (기본값: 1024, 16으로 나누어 떨어져야 합니다) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 잠재 이미지의 높이(픽셀 단위)입니다. (기본값: 1024, 16으로 나누어 떨어져야 합니다) | INT | 예 | 16 to MAX_RESOLUTION |
| `batch_size` | 배치에서 생성할 잠재 이미지 수입니다. (기본값: 1) | INT | 아니요 | 1 to 4096 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `samples` | 지정된 크기로 0으로 채워진 생성된 빈 잠재 이미지 텐서입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/ko.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
