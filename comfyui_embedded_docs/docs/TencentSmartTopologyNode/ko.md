> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/ko.md)

이 문서는 AI로 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/en.md)

이 노드는 3D 모델에 대해 스마트 리토폴로지를 수행합니다. 리토폴로지는 더 적은 폴리곤 수를 가진 새롭고 깔끔한 메시를 자동으로 생성하는 과정입니다. Tencent Hunyuan 3D API에 연결하여 모델을 처리하며, GLB 및 OBJ 파일 형식을 지원합니다. 이 노드는 처리된 모델을 OBJ 파일로 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | 예 | - | 입력 3D 모델(GLB 또는 OBJ). 파일은 GLB 또는 OBJ 형식이어야 하며, 200MB를 초과할 수 없습니다. |
| `polygon_type` | STRING | 예 | `"triangle"`<br>`"quadrilateral"` | 표면 구성 유형입니다. |
| `face_level` | STRING | 예 | `"medium"`<br>`"high"`<br>`"low"` | 폴리곤 감소 수준입니다. |
| `seed` | INT | 아니요 | 0 ~ 2147483647 | 시드는 노드 재실행 여부를 제어합니다. 시드 값과 관계없이 결과는 비결정적입니다. (기본값: 0) |

**참고:** `seed` 매개변수는 노드의 재실행을 트리거하는 데 사용되지만, 동일한 시드 값에 대해 최종 출력이 동일하다고 보장되지는 않습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | 최적화된 토폴로지가 적용된 처리된 3D 모델로, OBJ 형식으로 반환됩니다. |