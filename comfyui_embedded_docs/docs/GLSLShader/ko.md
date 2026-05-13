> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/ko.md)

GLSL 셰이더 노드는 입력 이미지에 사용자 정의 GLSL ES 프래그먼트 셰이더 코드를 적용합니다. 여러 이미지를 처리하고 균일 매개변수(실수, 정수, 부울, 곡선)를 받아들여 복잡한 시각 효과를 생성하는 셰이더 프로그램을 작성할 수 있습니다. 출력 크기는 첫 번째 입력 이미지에 의해 결정되거나 수동으로 설정할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | 예 | 해당 없음 | GLSL 프래그먼트 셰이더 소스 코드(GLSL ES 3.00 / WebGL 2.0 호환). 기본값: 첫 번째 입력 이미지를 출력하는 기본 셰이더. |
| `size_mode` | COMBO | 예 | `"from_input"`<br>`"custom"` | 출력 크기: 'from_input'은 첫 번째 입력 이미지 크기를 사용하고, 'custom'은 수동 크기 설정을 허용합니다. |
| `width` | INT | 아니요 | 1 ~ 16384 | `size_mode`가 `"custom"`으로 설정된 경우 출력 이미지의 너비입니다. 기본값: 512. |
| `height` | INT | 아니요 | 1 ~ 16384 | `size_mode`가 `"custom"`으로 설정된 경우 출력 이미지의 높이입니다. 기본값: 512. |
| `images` | IMAGE | 예 | 1 ~ 8개 이미지 | 셰이더가 처리할 입력 이미지입니다. 이미지는 셰이더 코드에서 `u_image0`부터 `u_image7`(sampler2D)로 사용할 수 있습니다. |
| `floats` | FLOAT | 아니요 | 0 ~ 8개 실수 | 셰이더의 부동소수점 균일 값입니다. 실수는 셰이더 코드에서 `u_float0`부터 `u_float7`로 사용할 수 있습니다. 기본값: 0.0. |
| `ints` | INT | 아니요 | 0 ~ 8개 정수 | 셰이더의 정수 균일 값입니다. 정수는 셰이더 코드에서 `u_int0`부터 `u_int7`로 사용할 수 있습니다. 기본값: 0. |
| `불리언` | BOOLEAN | 아니요 | 0 ~ 8개 부울 | 셰이더의 부울 균일 값입니다. 부울은 셰이더 코드에서 `u_bool0`부터 `u_bool7`(bool)로 사용할 수 있습니다. 기본값: False. |
| `커브` | CURVE | 아니요 | 0 ~ 8개 곡선 | 셰이더의 곡선 균일 값입니다. 곡선은 셰이더 코드에서 `u_curve0`부터 `u_curve7`(sampler2D, 1D LUT)로 사용할 수 있습니다. `texture(u_curve0, vec2(x, 0.5)).r`로 샘플링합니다. |

**참고:**

* `width` 및 `height` 매개변수는 `size_mode`가 `"custom"`으로 설정된 경우에만 필요하며 표시됩니다.
* 최소 하나의 입력 이미지가 필요합니다.
* 셰이더 코드는 항상 출력 크기를 포함하는 `u_resolution`(vec2) 균일에 접근할 수 있습니다.
* 최대 8개의 입력 이미지, 8개의 실수 균일 값, 8개의 정수 균일 값, 8개의 부울 균일 값, 8개의 곡선 균일 값을 제공할 수 있습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE1` | IMAGE | 셰이더의 첫 번째 출력 이미지입니다. 셰이더 코드에서 `layout(location = 0) out vec4 fragColor0`을 통해 사용할 수 있습니다. |
| `IMAGE2` | IMAGE | 셰이더의 두 번째 출력 이미지입니다. 셰이더 코드에서 `layout(location = 1) out vec4 fragColor1`을 통해 사용할 수 있습니다. |
| `IMAGE3` | IMAGE | 셰이더의 세 번째 출력 이미지입니다. 셰이더 코드에서 `layout(location = 2) out vec4 fragColor2`를 통해 사용할 수 있습니다. |
| `IMAGE3` | IMAGE | 셰이더의 네 번째 출력 이미지입니다. 셰이더 코드에서 `layout(location = 3) out vec4 fragColor3`을 통해 사용할 수 있습니다. |

---
**Source fingerprint (SHA-256):** `7830977409a5efab205b7c927eb83499a9e1e8299959b34643c9c3f1f586c058`
