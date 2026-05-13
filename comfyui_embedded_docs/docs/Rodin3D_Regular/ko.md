> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/ko.md)

# Rodin 3D Regular 노드

Rodin 3D Regular 노드는 Rodin API를 사용하여 3D 에셋을 생성합니다. 입력 이미지를 받아 Rodin 서비스를 통해 처리하여 3D 모델을 만듭니다. 이 노드는 작업 생성부터 최종 3D 모델 파일 다운로드까지 전체 워크플로를 처리합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 예 | - | 3D 모델 생성에 사용되는 입력 이미지입니다. 여러 이미지를 제공할 수 있습니다. |
| `Seed` | INT | 예 | - | 재현 가능한 결과를 위한 난수 시드 값입니다. |
| `Material_Type` | STRING | 예 | - | 3D 모델에 적용할 재질 유형입니다. |
| `Polygon_count` | STRING | 예 | - | 생성된 3D 모델의 목표 폴리곤 수입니다. 이 매개변수는 품질 수준과 메시 복잡성을 결정합니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 생성된 3D 모델의 파일 경로입니다(하위 호환성을 위해 유지됨). |
| `GLB` | FILE3DGLB | GLB 형식으로 생성된 3D 모델입니다. |

---
**Source fingerprint (SHA-256):** `f937be3aa579baf4407434839e741141d6bd63c09b7e0bdc49a9e92a10d7a130`
