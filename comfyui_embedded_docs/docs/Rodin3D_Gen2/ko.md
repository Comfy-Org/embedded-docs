> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/ko.md)

Rodin3D_Gen2 노드는 Rodin API를 사용하여 3D 에셋을 생성합니다. 입력 이미지를 받아 다양한 재질 유형과 폴리곤 수를 가진 3D 모델로 변환합니다. 이 노드는 작업 생성, 상태 폴링, 파일 다운로드를 포함한 전체 생성 과정을 자동으로 처리합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 예 | - | 3D 모델 생성에 사용할 입력 이미지 |
| `Seed` | INT | 아니오 | 0-65535 | 생성을 위한 랜덤 시드 값 (기본값: 0) |
| `Material_Type` | COMBO | 아니오 | "PBR"<br>"Shaded" | 3D 모델에 적용할 재질 유형 (기본값: "PBR") |
| `Polygon_count` | COMBO | 아니오 | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | 생성된 3D 모델의 목표 폴리곤 수 (기본값: "500K-Triangle") |
| `TAPose` | BOOLEAN | 아니오 | - | TAPose 처리를 적용할지 여부 (기본값: False) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 생성된 3D 모델의 파일 경로 |