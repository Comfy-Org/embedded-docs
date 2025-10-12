> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/ko.md)

PhotoMakerLoader 노드는 사용 가능한 모델 파일에서 PhotoMaker 모델을 불러옵니다. 지정된 모델 파일을 읽어서 신원 기반 이미지 생성 작업에 사용할 PhotoMaker ID 인코더를 준비합니다. 이 노드는 실험적으로 표시되어 있으며 테스트 목적으로 사용됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `포토메이커 파일명` | STRING | 예 | 사용 가능한 여러 옵션 | 불러올 PhotoMaker 모델 파일의 이름입니다. 사용 가능한 옵션은 photomaker 폴더에 있는 모델 파일에 따라 결정됩니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `photomaker_model` | PHOTOMAKER | 불러온 PhotoMaker 모델로, ID 인코더를 포함하며 신원 인코딩 작업에 사용할 준비가 되어 있습니다. |
