> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/ko.md)

입력 이미지와 텍스트 프롬프트를 기반으로 비디오를 생성합니다. 이 노드는 이미지를 입력받아 지정된 모션 및 품질 설정을 적용하여 정적 이미지를 움직이는 시퀀스로 변환하는 애니메이션 비디오를 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `이미지` | IMAGE | 예 | - | 비디오로 변환할 입력 이미지 |
| `프롬프트` | STRING | 예 | - | 비디오 생성을 위한 프롬프트 |
| `품질` | COMBO | 예 | `res_540p`<br>`res_1080p` | 비디오 품질 설정 (기본값: res_540p) |
| `길이(초)` | COMBO | 예 | `dur_2`<br>`dur_5`<br>`dur_10` | 생성된 비디오의 길이(초 단위) |
| `모션 모드` | COMBO | 예 | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | 비디오 생성에 적용되는 모션 스타일 |
| `시드` | INT | 예 | 0-2147483647 | 비디오 생성을 위한 시드 값 (기본값: 0) |
| `부정 프롬프트` | STRING | 아니오 | - | 이미지에서 원하지 않는 요소에 대한 선택적 텍스트 설명 |
| `PixVerse 템플릿` | CUSTOM | 아니오 | - | 생성 스타일에 영향을 주기 위한 선택적 템플릿으로, PixVerse Template 노드에서 생성됨 |

**참고:** 1080p 품질을 사용할 경우 모션 모드는 자동으로 normal로 설정되며 길이는 5초로 제한됩니다. 5초 이외의 길이를 사용할 경우 모션 모드도 자동으로 normal로 설정됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 입력 이미지와 매개변수를 기반으로 생성된 비디오 |