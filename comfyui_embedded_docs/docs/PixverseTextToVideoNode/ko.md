> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/ko.md)

프롬프트와 출력 크기를 기반으로 동영상을 생성합니다. 이 노드는 텍스트 설명과 다양한 생성 매개변수를 사용하여 동영상 콘텐츠를 생성하며, PixVerse API를 통해 동영상 출력을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `프롬프트` | STRING | 예 | - | 동영상 생성을 위한 프롬프트 (기본값: "") |
| `화면 비율` | COMBO | 예 | PixverseAspectRatio의 옵션 | 생성된 동영상의 화면 비율 |
| `품질` | COMBO | 예 | PixverseQuality의 옵션 | 동영상 품질 설정 (기본값: PixverseQuality.res_540p) |
| `길이(초)` | COMBO | 예 | PixverseDuration의 옵션 | 생성된 동영상의 지속 시간(초 단위) |
| `모션 모드` | COMBO | 예 | PixverseMotionMode의 옵션 | 동영상 생성 모션 스타일 |
| `시드` | INT | 예 | 0부터 2147483647까지 | 동영상 생성을 위한 시드 값 (기본값: 0) |
| `부정 프롬프트` | STRING | 아니오 | - | 이미지에서 원하지 않는 요소에 대한 선택적 텍스트 설명 (기본값: "") |
| `PixVerse 템플릿` | CUSTOM | 아니오 | - | 생성 스타일에 영향을 주기 위한 선택적 템플릿, PixVerse Template 노드로 생성됨 |

**참고:** 1080p 품질을 사용할 때는 모션 모드가 자동으로 normal로 설정되고 지속 시간은 5초로 제한됩니다. 5초가 아닌 지속 시간의 경우에도 모션 모드는 자동으로 normal로 설정됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 동영상 파일 |
