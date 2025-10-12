> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/ko.md)

# Kling Virtual Try On Node

인물 이미지와 의류 이미지를 입력하여 인물에게 의상을 입혀 볼 수 있습니다. 여러 개의 의류 아이템 사진을 흰색 배경의 단일 이미지로 병합할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `human_image` | IMAGE | 예 | - | 의상을 입혀 볼 인물 이미지 |
| `cloth_image` | IMAGE | 예 | - | 인물에게 입혀 볼 의류 이미지 |
| `model_name` | STRING | 예 | `"kolors-virtual-try-on-v1"` | 사용할 가상 피팅 모델 (기본값: "kolors-virtual-try-on-v1") |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | IMAGE | 의상을 입혀 본 결과 이미지 |