> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/ko.md)

이 노드는 Recraft API와 함께 사용할 스타일을 구성하며, 특히 "digital_illustration" 스타일을 선택합니다. 선택적 서브스타일을 지정하여 생성될 이미지의 예술적 방향을 더욱 세밀하게 조정할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `하위 스타일` | STRING | 아니요 | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` | 특정 유형의 디지털 일러스트레이션을 지정하는 선택적 서브스타일입니다. 선택하지 않으면 기본 "digital_illustration" 스타일이 사용됩니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | 선택된 "digital_illustration" 스타일과 선택적 서브스타일을 포함하는 구성된 스타일 객체로, 다른 Recraft API 노드로 전달할 준비가 되어 있습니다. |
