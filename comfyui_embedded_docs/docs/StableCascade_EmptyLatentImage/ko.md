> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/ko.md)

StableCascade_EmptyLatentImage 노드는 Stable Cascade 모델을 위한 빈 잠재 텐서를 생성합니다. 이 노드는 입력 해상도와 압축 설정에 기반하여 적절한 차원을 가진 두 개의 별도 잠재 표현(스테이지 C용과 스테이지 B용)을 생성합니다. 이 노드는 Stable Cascade 생성 파이프라인의 시작점을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `너비` | INT | 예 | 256 ~ MAX_RESOLUTION | 출력 이미지의 너비 (픽셀 단위) (기본값: 1024, 단계: 8) |
| `높이` | INT | 예 | 256 ~ MAX_RESOLUTION | 출력 이미지의 높이 (픽셀 단위) (기본값: 1024, 단계: 8) |
| `압축` | INT | 예 | 4 ~ 128 | 스테이지 C의 잠재 차원을 결정하는 압축 계수 (기본값: 42, 단계: 1) |
| `배치 크기` | INT | 아니오 | 1 ~ 4096 | 배치에서 생성할 잠재 샘플의 수 (기본값: 1) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `StageB 잠재 이미지` | LATENT | 차원이 [batch_size, 16, height//compression, width//compression]인 스테이지 C 잠재 텐서 |
| `stage_b` | LATENT | 차원이 [batch_size, 4, height//4, width//4]인 스테이지 B 잠재 텐서 |