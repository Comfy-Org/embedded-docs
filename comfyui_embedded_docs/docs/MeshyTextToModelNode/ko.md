# Meshy: 텍스트 → 모델

Meshy: Text to Model 노드는 Meshy API를 사용하여 텍스트 설명에서 3D 모델을 생성합니다. 프롬프트와 설정을 API에 요청으로 보내고, 생성이 완료될 때까지 대기한 후 결과 모델 파일을 다운로드합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 사용할 AI 모델 버전을 지정합니다. 현재는 "latest" 버전만 사용할 수 있습니다. | COMBO | 예 | `"latest"` |
| `prompt` | 생성할 3D 모델에 대한 텍스트 설명입니다. 길이는 1자 이상 600자 이하여야 합니다. | STRING | 예 | - |
| `style` | 생성된 3D 모델의 예술적 스타일입니다. | COMBO | 예 | `"realistic"`<br>`"sculpture"` |
| `should_remesh` | 생성된 메시의 처리 여부를 제어합니다. "false"로 설정하면 노드는 처리되지 않은 삼각형 메시를 반환합니다. "true"를 선택하면 토폴로지와 폴리곤 수에 대한 추가 매개변수가 표시됩니다. | DYNAMIC_COMBO | 예 | `"true"`<br>`"false"` |
| `topology` | 리메시된 모델의 목표 폴리곤 유형입니다. 이 매개변수는 `should_remesh`가 "true"로 설정된 경우에만 사용할 수 있습니다. | COMBO | 아니요* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 리메시된 모델의 목표 폴리곤 수입니다. 기본값은 300000입니다. 이 매개변수는 `should_remesh`가 "true"로 설정된 경우에만 사용할 수 있습니다. | INT | 아니요* | 100 - 300000 |
| `symmetry_mode` | 생성된 모델의 대칭을 제어합니다. 고급 매개변수입니다. | COMBO | 예 | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | 생성된 모델의 포즈 모드를 지정합니다. 빈 문자열은 특정 포즈가 요청되지 않았음을 의미합니다. 고급 매개변수입니다. | COMBO | 예 | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 시드는 노드를 다시 실행해야 하는지 여부를 제어합니다. 시드와 관계없이 결과는 비결정적입니다. 기본값은 0입니다. | INT | 예 | 0 - 2147483647 |

*참고: `topology` 및 `target_polycount` 매개변수는 조건부로 사용할 수 있습니다. 이 매개변수는 `should_remesh` 매개변수가 "true"로 설정된 경우에만 나타납니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `모델 파일` | 생성된 GLB 모델의 파일 이름입니다. 이 출력은 이전 버전과의 호환성을 위해 제공됩니다. | STRING |
| `meshy_task_id` | Meshy API 작업의 고유 식별자입니다. | MESHY_TASK_ID |
| `GLB` | GLB 형식으로 생성된 3D 모델 파일입니다. | FILE3DGLB |
| `FBX` | FBX 형식으로 생성된 3D 모델 파일입니다. | FILE3DFBX |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/ko.md)

---
**Source fingerprint (SHA-256):** `1860b2d760aa81d611d4f44114591b4d98ccb85075bd1e06beabf462fb58bd53`
