# 3D 파일 생성(splat에서)

SplatToFile3D는 가우시안 스플랫을 Save 또는 Preview 3D 노드에서 사용할 수 있는 File3D 객체로 변환합니다. 출력 파일 형식을 선택할 수 있습니다. 이 노드는 배치당 하나의 항목만 지원합니다. 둘 이상의 항목이 입력되면 첫 번째 항목만 사용하고 경고를 기록합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `splat` | 파일로 직렬화할 가우시안 스플랫 데이터입니다. 배치당 하나의 항목만 지원됩니다. 둘 이상의 항목이 제공되면 첫 번째 항목만 사용됩니다. | SPLAT | 예 | - |
| `format` | 3D 파일의 출력 파일 형식입니다. ply: 완전한 구면 조화 함수를 포함하는 표준 3D 가우시안 스플랫. ksplat: mkkellogg SplatBuffer(레벨 0, 비압축), 기본 색상만 포함. spz: Niantic gzip 압축(약 10배 작음), 기본 색상만 포함(기본값: "ply") | COMBO | 예 | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model_3d` | 선택한 형식으로 직렬화된 가우시안 스플랫 데이터를 포함하는 File3D 객체로, 저장 또는 미리보기에 사용할 준비가 되었습니다 | FILE3D |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/ko.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
