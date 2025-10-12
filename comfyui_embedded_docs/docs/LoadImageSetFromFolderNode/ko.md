> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/ko.md)

LoadImageSetFromFolderNode는 훈련 목적으로 지정된 폴더 디렉터리에서 여러 이미지를 불러옵니다. 일반적인 이미지 형식을 자동으로 감지하며, 선택적으로 다양한 방법을 사용하여 이미지 크기를 조정한 후 배치로 반환할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | 예 | 여러 옵션 사용 가능 | 이미지를 불러올 폴더입니다. |
| `resize_method` | STRING | 아니오 | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | 이미지 크기 조정에 사용할 방법입니다 (기본값: "None"). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 단일 텐서로 불러온 이미지 배치입니다. |