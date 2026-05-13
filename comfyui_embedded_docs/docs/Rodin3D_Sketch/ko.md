> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/en.md)

이 노드는 Rodin API를 사용하여 3D 에셋을 생성합니다. 입력 이미지를 받아 외부 서비스를 통해 3D 모델로 변환합니다. 이 노드는 작업 생성부터 최종 3D 모델 파일 다운로드까지 전체 프로세스를 처리합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 예 | - | 3D 모델로 변환할 입력 이미지입니다. 여러 이미지를 제공할 수 있습니다. |
| `Seed` | INT | 아니요 | 0-65535 | 생성을 위한 무작위 시드 값입니다(기본값: 0). 0으로 설정하면 무작위 시드가 사용됩니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 생성된 3D 모델의 파일 경로입니다(하위 호환성 전용). |
| `GLB` | FILE3DGLB | GLB 형식으로 생성된 3D 모델입니다. |

---
**Source fingerprint (SHA-256):** `d3bc71e6a44c11cbeff25351d561e99a7f09ed8ce3544d2968a873b6796512da`
