> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/ko.md)

GLSL Shader 노드는 사용자 정의 GLSL ES 프래그먼트 셰이더 코드를 입력 이미지에 적용합니다. 여러 이미지를 처리하고 균일(uniform) 매개변수(부동 소수점 및 정수)를 받아들여 복잡한 시각 효과를 생성할 수 있는 셰이더 프로그램을 작성할 수 있습니다. 출력 크기는 첫 번째 입력 이미지에 의해 결정되거나 수동으로 설정할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | 예 | 해당 없음 | GLSL 프래그먼트 셰이더 소스 코드 (GLSL ES 3.00 / WebGL 2.0 호환). 기본값: 첫 번째 입력 이미지를 출력하는 기본 셰이더. |
| `size_mode` | COMBO | 예 | `"from_input"`<br>`"custom"` | 출력 크기: 'from_input'은 첫 번째 입력 이미지의 크기를 사용하고, 'custom'은 수동 크기 설정을 허용합니다. |
| `width` | INT | 아니요 | 1 ~ 16384 | `size_mode`가 `"custom"`으로 설정되었을 때 출력 이미지의 너비. 기본값: 512. |
| `height` | INT | 아니요 | 1 ~ 16384 | `size_mode`가 `"custom"`으로 설정되었을 때 출력 이미지의 높이. 기본값: 512. |
| `images` | IMAGE | 예 | 1 ~ 8개 이미지 | 셰이더에 의해 처리될 입력 이미지. 이미지는 셰이더 코드 내에서 `u_image0`부터 `u_image7`(sampler2D)로 사용 가능합니다. |
| `floats` | FLOAT | 아니요 | 0 ~ 8개의 부동 소수점 | 셰이더를 위한 부동 소수점 균일(uniform) 값. 부동 소수점 값은 셰이더 코드 내에서 `u_float0`부터 `u_float7`로 사용 가능합니다. 기본값: 0.0. |
| `ints` | INT | 아니요 | 0 ~ 8개의 정수 | 셰이더를 위한 정수 균일(uniform) 값. 정수 값은 셰이더 코드 내에서 `u_int0`부터 `u_int7`로 사용 가능합니다. 기본값: 0. |

**참고:**
*   `width` 및 `height` 매개변수는 `size_mode`가 `"custom"`으로 설정된 경우에만 필요하며 표시됩니다.
*   최소 하나의 입력 이미지가 필요합니다.
*   셰이더 코드는 항상 출력 크기를 포함하는 `u_resolution` (vec2) 균일(uniform) 변수에 접근할 수 있습니다.
*   최대 8개의 입력 이미지, 8개의 부동 소수점 균일(uniform) 변수, 8개의 정수 균일(uniform) 변수를 제공할 수 있습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE0` | IMAGE | 셰이더의 첫 번째 출력 이미지. 셰이더 코드 내 `layout(location = 0) out vec4 fragColor0`를 통해 사용 가능합니다. |
| `IMAGE1` | IMAGE | 셰이더의 두 번째 출력 이미지. 셰이더 코드 내 `layout(location = 1) out vec4 fragColor1`를 통해 사용 가능합니다. |
| `IMAGE2` | IMAGE | 셰이더의 세 번째 출력 이미지. 셰이더 코드 내 `layout(location = 2) out vec4 fragColor2`를 통해 사용 가능합니다. |
| `IMAGE3` | IMAGE | 셰이더의 네 번째 출력 이미지. 셰이더 코드 내 `layout(location = 3) out vec4 fragColor3`를 통해 사용 가능합니다. |