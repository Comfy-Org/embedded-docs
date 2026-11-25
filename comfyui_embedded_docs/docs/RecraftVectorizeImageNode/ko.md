# Recraft 벡터 생성 (이미지 → 벡터)

입력 이미지로부터 SVG 벡터 그래픽을 생성합니다. 이 노드는 각 이미지를 Recraft API로 전송하고 결과를 단일 SVG 출력으로 결합하여 래스터 이미지를 확장 가능한 벡터 형식으로 변환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `이미지` | SVG 형식으로 변환할 입력 이미지입니다. 여러 이미지의 배치 처리를 지원합니다. | IMAGE | 예 | - |
| `version` | 벡터라이저 버전입니다. `v1`은 표준 버전이며, `v1_pro`(Vectorizer Pro)는 부드러운 곡선, 직선 및 날카로운 모서리로 더 깔끔한 SVG를 생성하며, 레터링과 복잡한 모양에 가장 적합합니다(기본값: "v1"). | COMBO | 아니요 | "v1"<br>"v1_pro" |
| `shape_stacking` | SVG에서 도형이 쌓이는 방식입니다. `hierarchical`은 도형을 서로 위에 겹쳐 쌓고, `cut_out`은 플로터, 비닐 커터, 스크린 인쇄용으로 절대 겹치지 않는 도형을 만듭니다(기본값: "hierarchical"). | COMBO | 아니요 | "hierarchical"<br>"cut_out" |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `SVG` | 처리된 모든 이미지를 단일 SVG 문서로 결합한 생성된 벡터 그래픽 출력입니다. | SVG |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/ko.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
