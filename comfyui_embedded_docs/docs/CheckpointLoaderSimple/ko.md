이것은 지정된 위치에서 모델 파일을 로드하고 세 가지 핵심 구성 요소(메인 모델, 텍스트 인코더, 이미지 인코더/디코더)로 분해하는 모델 로더 노드입니다.

이 노드는 `ComfyUI/models/checkpoints` 폴더의 모든 모델 파일과 `extra_model_paths.yaml` 파일에서 설정한 추가 경로를 자동으로 감지합니다.

1. **모델 호환성**: 선택한 모델이 워크플로우와 호환되는지 확인하세요. 다양한 모델 유형(SD1.5, SDXL, Flux 등)은 해당 샘플러 및 기타 노드와 함께 사용해야 합니다
2. **파일 관리**: 모델 파일을 `ComfyUI/models/checkpoints` 폴더에 배치하거나 extra_model_paths.yaml을 통해 다른 경로를 설정하세요
3. **인터페이스 새로 고침**: ComfyUI 실행 중에 새 모델 파일이 추가된 경우, 드롭다운 목록에서 새 파일을 보려면 브라우저를 새로 고침(Ctrl+R)해야 합니다

## 입력

| 매개변수 이름 | 데이터 유형 | 입력 방법 | 기본값 | 값 범위 | 설명 |
|--------------|-------------|-----------|--------|---------|------|
| 체크포인트 파일명 | STRING | 드롭다운 선택 | null | checkpoints 폴더의 모든 모델 파일 | 로드할 체크포인트 모델 파일 이름을 선택하며, 후속 이미지 생성에 사용되는 AI 모델을 결정합니다 |

## 출력

| 출력 이름 | 데이터 유형 | 설명 |
|----------|-------------|------|
| 모델 | MODEL | 이미지 노이즈 제거 생성에 사용되는 주요 확산 모델, AI 이미지 생성의 핵심 구성 요소 |
| CLIP | CLIP | 텍스트 프롬프트 인코딩에 사용되는 모델, 텍스트 설명을 AI가 이해할 수 있는 정보로 변환 |
| VAE | VAE | 이미지 인코딩 및 디코딩에 사용되는 모델, 픽셀 공간과 잠재 공간 간의 변환을 담당 |
