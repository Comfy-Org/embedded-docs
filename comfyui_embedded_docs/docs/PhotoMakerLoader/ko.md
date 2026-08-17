# 포토메이커 로드

PhotoMakerLoader 노드는 사용 가능한 모델 파일에서 PhotoMaker 모델을 로드합니다. 지정된 모델 파일을 읽어 ID 기반 이미지 생성 작업에 사용할 PhotoMaker ID 인코더를 준비합니다. 이 노드는 실험적 기능으로 표시되며 테스트 목적으로 사용됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | 로드할 PhotoMaker 모델 파일의 이름입니다. 사용 가능한 옵션은 `photomaker` 폴더에 있는 모델 파일에 따라 결정됩니다. | COMBO | 예 | 여러 옵션 사용 가능 |

참고: 선택한 모델 파일은 `photomaker` 폴더에 존재해야 합니다. 지정된 파일을 찾을 수 없으면 노드에서 오류가 발생합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `photomaker_model` | ID 인코딩 작업에 사용할 준비가 된, ID 인코더가 포함된 로드된 PhotoMaker 모델입니다. | PHOTOMAKER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/ko.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
