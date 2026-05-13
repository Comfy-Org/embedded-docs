> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/en.md)

Rodin 3D Smooth 노드는 Rodin API를 사용하여 입력 이미지를 처리하고 부드러운 3D 모델로 변환함으로써 3D 에셋을 생성합니다. 여러 이미지를 입력으로 받아 다운로드 가능한 3D 모델 파일을 출력합니다. 이 노드는 작업 생성, 상태 폴링, 파일 다운로드를 포함한 전체 생성 과정을 자동으로 처리합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 예 | - | 3D 모델 생성에 사용할 입력 이미지입니다. 여러 이미지를 제공할 수 있습니다. |
| `Seed` | INT | 예 | - | 생성 일관성을 위한 무작위 시드 값입니다. |
| `Material_Type` | STRING | 예 | - | 3D 모델에 적용할 재질 유형입니다. |
| `Polygon_count` | STRING | 예 | - | 생성된 3D 모델의 목표 폴리곤 수입니다. 메시 품질과 세부 수준을 결정합니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 다운로드된 3D 모델의 파일 경로입니다(하위 호환성 전용). |
| `GLB` | FILE3DGLB | GLB 형식으로 생성된 3D 모델입니다. |

---
**Source fingerprint (SHA-256):** `18783d4a3010234a3640d20c73cdd78e35a0eef7090bd433dba0fcc58e35ad3f`
