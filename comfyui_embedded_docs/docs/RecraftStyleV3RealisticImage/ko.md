> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/ko.md)

이 노드는 Recraft API와 함께 사용할 수 있는 사실적인 이미지 스타일 구성을 생성합니다. realistic_image 스타일을 선택하고 다양한 서브스타일 옵션 중에서 선택하여 출력 결과의 외관을 사용자 정의할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | 예 | 여러 옵션 사용 가능 | realistic_image 스타일에 적용할 특정 서브스타일입니다. "None"으로 설정하면 서브스타일이 적용되지 않습니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | realistic_image 스타일과 선택된 서브스타일 설정을 포함한 Recraft 스타일 구성 객체를 반환합니다. |