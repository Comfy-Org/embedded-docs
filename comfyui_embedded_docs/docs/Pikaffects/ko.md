> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/ko.md)

Pikaffects 노드는 입력 이미지에 다양한 시각 효과를 적용하여 비디오를 생성합니다. 이 노드는 Pika의 비디오 생성 API를 사용하여 정적 이미지를 녹는, 폭발하는, 공중에 떠오르는 등의 특정 효과가 적용된 애니메이션 비디오로 변환합니다. 노드를 사용하려면 Pika 서비스에 접근하기 위한 API 키와 인증 토큰이 필요합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | Pikaffect를 적용할 참조 이미지입니다. |
| `pikaffect` | COMBO | 예 | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | 이미지에 적용할 특정 시각 효과입니다 (기본값: "Cake-ify"). |
| `prompt_text` | STRING | 예 | - | 비디오 생성을 안내하는 텍스트 설명입니다. |
| `negative_prompt` | STRING | 예 | - | 생성된 비디오에서 피해야 할 내용에 대한 텍스트 설명입니다. |
| `seed` | INT | 예 | 0부터 4294967295까지 | 재현 가능한 결과를 위한 랜덤 시드 값입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 적용된 Pikaffect 효과가 포함된 생성된 비디오입니다. |