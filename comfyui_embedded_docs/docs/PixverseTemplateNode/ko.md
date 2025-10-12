> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/ko.md)

PixVerse Template 노드를 사용하면 PixVerse 비디오 생성을 위해 사용 가능한 템플릿 중에서 선택할 수 있습니다. 이 노드는 선택한 템플릿 이름을 PixVerse API에서 비디오 생성에 필요한 해당 템플릿 ID로 변환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `템플릿` | STRING | 예 | 여러 옵션 사용 가능 | PixVerse 비디오 생성에 사용할 템플릿입니다. 사용 가능한 옵션은 PixVerse 시스템에 미리 정의된 템플릿에 해당합니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `pixverse_template` | INT | 선택한 템플릿 이름에 해당하는 템플릿 ID로, 다른 PixVerse 노드에서 비디오 생성에 사용할 수 있습니다. |
