> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/ko.md)

ByteDance Image 노드는 텍스트 프롬프트를 기반으로 API를 통해 ByteDance 모델을 사용하여 이미지를 생성합니다. 다양한 모델을 선택하고, 이미지 크기를 지정하며, 시드 및 가이던스 스케일과 같은 다양한 생성 매개변수를 제어할 수 있습니다. 이 노드는 ByteDance의 이미지 생성 서비스에 연결되어 생성된 이미지를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedream_3 | Text2ImageModelName 옵션 | 모델 이름 |
| `prompt` | STRING | STRING | - | - | 이미지 생성에 사용되는 텍스트 프롬프트 |
| `size_preset` | STRING | COMBO | - | RECOMMENDED_PRESETS 레이블 | 권장 크기를 선택합니다. 아래의 너비와 높이를 사용하려면 Custom을 선택하세요 |
| `width` | INT | INT | 1024 | 512-2048 (간격 64) | 이미지의 사용자 정의 너비. 이 값은 `size_preset`이 `Custom`으로 설정된 경우에만 작동합니다 |
| `height` | INT | INT | 1024 | 512-2048 (간격 64) | 이미지의 사용자 정의 높이. 이 값은 `size_preset`이 `Custom`으로 설정된 경우에만 작동합니다 |
| `seed` | INT | INT | 0 | 0-2147483647 (간격 1) | 생성에 사용할 시드 (선택 사항) |
| `guidance_scale` | FLOAT | FLOAT | 2.5 | 1.0-10.0 (간격 0.01) | 값이 높을수록 이미지가 프롬프트를 더 밀접하게 따릅니다 (선택 사항) |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 이미지에 "AI 생성" 워터마크를 추가할지 여부 (선택 사항) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | ByteDance API에서 생성된 이미지 |
