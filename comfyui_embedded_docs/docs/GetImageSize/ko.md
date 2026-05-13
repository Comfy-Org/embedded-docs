> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/ko.md)

GetImageSize 노드는 입력 이미지의 크기와 배치 정보를 추출합니다. 이미지의 너비, 높이 및 배치 크기를 반환하며, 이 정보를 노드 인터페이스에 진행 텍스트로 표시합니다. 원본 이미지 데이터는 변경되지 않고 통과됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 크기 정보를 추출할 입력 이미지 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `width` | INT | 입력 이미지의 너비(픽셀 단위) |
| `height` | INT | 입력 이미지의 높이(픽셀 단위) |
| `batch_size` | INT | 배치 내 이미지 개수 |

---
**Source fingerprint (SHA-256):** `5cd19ae762d2403c6c5d0740cd5f8c17913daea737fddcff8f0d9da2210e82ab`
