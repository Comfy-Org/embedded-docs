# 통합 컨트롤넷 유형 설정

SetUnionControlNetType 노드는 컨디셔닝에 사용되는 제어 네트워크의 제어 유형을 설정할 수 있게 해주는 노드입니다. 기존 제어 네트워크를 가져와 수정된 복사본을 만들고, 선택한 제어 유형을 해당 복사본에 저장하므로 원본은 변경되지 않습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `control_net` | 선택한 제어 유형으로 복사 및 수정할 제어 네트워크 | CONTROL_NET | 예 | - |
| `type` | 복사된 제어 네트워크에 적용할 제어 유형입니다. 제어 유형을 설정하지 않으려면 "auto"를 선택하고, 사용 가능한 유니온 제어 네트워크 유형 중에서 특정 유형을 선택합니다(기본값: "auto"). | COMBO | 예 | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

참고: `type`이 "auto"이면 복사된 제어 네트워크의 제어 유형 목록이 지워집니다. 특정 유형을 선택하면 복사된 제어 네트워크에 해당 유형 번호가 저장됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `control_net` | 선택한 제어 유형이 적용된 제어 네트워크의 수정된 복사본 | CONTROL_NET |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/ko.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
