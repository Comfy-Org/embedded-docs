> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/ko.md)

이 노드는 Tencent Hunyuan3D API를 사용하여 3D 모델에 UV 전개를 수행합니다. 3D 모델 파일을 입력으로 받아 API로 전송하여 처리하고, 처리된 모델을 OBJ 및 FBX 형식으로, 그리고 생성된 UV 텍스처 이미지를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | 예 | GLB<br>OBJ<br>FBX | 입력 3D 모델 (GLB, OBJ 또는 FBX). 모델은 30000개 미만의 면을 가져야 합니다. |
| `seed` | INT | 아니요 | 0 ~ 2147483647 | 시드 값 (기본값: 1). 이 값은 노드를 재실행할지 여부를 제어하지만, 시드 값과 관계없이 결과는 비결정적입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | 처리된 3D 모델 파일 (OBJ 형식). |
| `FBX` | FILE3D | 처리된 3D 모델 파일 (FBX 형식). |
| `Image` | IMAGE | 생성된 UV 텍스처 이미지. |