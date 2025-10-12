> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/ko.md)

이 노드를 사용하면 사전에 존재하는 UUID를 이용해 Recraft의 Infinite Style Library에서 스타일을 선택할 수 있습니다. 제공된 스타일 식별자를 기반으로 스타일 정보를 검색하여 다른 Recraft 노드에서 사용할 수 있도록 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `스타일 ID` | STRING | 예 | 유효한 UUID | Infinite Style Library에서 가져온 스타일의 UUID입니다. |

**참고:** `style_id` 입력은 비워둘 수 없습니다. 빈 문자열이 제공되면 노드에서 예외가 발생합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Recraft의 Infinite Style Library에서 선택한 스타일 객체입니다 |
