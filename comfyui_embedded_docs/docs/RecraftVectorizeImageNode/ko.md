> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/ko.md)

입력 이미지로부터 SVG를 동기식으로 생성합니다. 이 노드는 입력 배치의 각 이미지를 처리하고 결과를 단일 SVG 출력으로 결합하여 래스터 이미지를 벡터 그래픽 형식으로 변환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | SVG 형식으로 변환할 입력 이미지 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `SVG` | SVG | 처리된 모든 이미지를 결합하여 생성된 벡터 그래픽 출력 |

---
**Source fingerprint (SHA-256):** `acd6b5bdb90ad01c0201e434fff84923dbe8a253f7fc5c46efb2d7413f49a8bd`
