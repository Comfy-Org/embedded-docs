> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/ko.md)

SetUnionControlNetType 노드를 사용하면 조건화에 사용할 제어 네트워크 유형을 지정할 수 있습니다. 기존 제어 네트워크를 입력받아 선택에 따라 제어 유형을 설정하며, 지정된 유형 구성으로 수정된 제어 네트워크의 사본을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `control_net` | CONTROL_NET | 예 | - | 새로운 유형 설정으로 수정할 제어 네트워크 |
| `type` | STRING | 예 | `"auto"`<br>사용 가능한 모든 UNION_CONTROLNET_TYPES 키 | 적용할 제어 네트워크 유형. 자동 유형 감지를 위해 "auto"를 사용하거나 사용 가능한 옵션 중 특정 제어 네트워크 유형을 선택합니다 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `control_net` | CONTROL_NET | 지정된 유형 설정이 적용된 수정된 제어 네트워크 |