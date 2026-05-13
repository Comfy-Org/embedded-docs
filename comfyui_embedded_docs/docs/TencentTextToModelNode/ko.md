> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/ko.md)

이 문서는 AI로 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/en.md)

이 노드는 Tencent의 Hunyuan3D Pro API를 사용하여 텍스트 설명으로부터 3D 모델을 생성합니다. 생성 작업 요청을 전송하고, 결과를 폴링하며, 최종 모델 파일을 GLB 및 OBJ 형식으로 다운로드합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `"3.0"`<br>`"3.1"` | 사용할 Hunyuan3D 모델의 버전입니다. `3.1` 모델에서는 LowPoly 옵션을 사용할 수 없습니다. |
| `prompt` | STRING | 예 | - | 생성할 3D 모델의 텍스트 설명입니다. 최대 1024자까지 지원합니다. |
| `face_count` | INT | 예 | 3000 - 1500000 | 생성된 3D 모델의 목표 면 수입니다. 기본값: 500000. |
| `generate_type` | DYNAMICCOMBO | 예 | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | 생성할 3D 모델의 유형입니다. 사용 가능한 옵션과 관련 매개변수는 다음과 같습니다:<br>- **Normal**: 표준 모델을 생성합니다. `pbr` 매개변수(기본값: `False`)를 포함합니다.<br>- **LowPoly**: 저폴리곤 모델을 생성합니다. `polygon_type`(`"triangle"` 또는 `"quadrilateral"`) 및 `pbr`(기본값: `False`) 매개변수를 포함합니다.<br>- **Geometry**: 지오메트리 전용 모델을 생성합니다. |
| `seed` | INT | 아니요 | 0 - 2147483647 | 생성을 위한 시드 값입니다. 시드와 관계없이 결과는 비결정적입니다. 새 시드를 설정하면 노드가 다시 실행되어야 하는지 여부를 제어합니다. 기본값: 0. |

**참고:** `generate_type` 매개변수는 동적입니다. `"LowPoly"`를 선택하면 `polygon_type` 및 `pbr`에 대한 추가 입력이 표시됩니다. `"Normal"`을 선택하면 `pbr`에 대한 입력이 표시됩니다. `"Geometry"`를 선택하면 추가 입력이 표시되지 않습니다.

**제약 사항:** `"LowPoly"` 생성 유형은 `"3.1"` 모델과 함께 사용할 수 없습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 이전 버전과의 호환성을 위한 레거시 출력입니다. |
| `GLB` | FILE3DGLB | GLB 파일 형식으로 생성된 3D 모델입니다. |
| `OBJ` | FILE3DOBJ | OBJ 파일 형식으로 생성된 3D 모델입니다. |
| `texture_image` | IMAGE | 생성된 OBJ 파일에서 추출한 텍스처 이미지입니다(사용 가능한 경우). |

---
**Source fingerprint (SHA-256):** `e35f5165941cc7761639dd72e78141326d37d5e169be9a0e326afcbcdc572b7d`
