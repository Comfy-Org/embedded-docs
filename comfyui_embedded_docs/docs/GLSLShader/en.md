> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/en.md)

The GLSL Shader node applies custom GLSL ES fragment shader code to input images. It allows you to write shader programs that can process multiple images and accept uniform parameters (floats, integers, booleans, and curves) to create complex visual effects. The output size can be determined by the first input image or set manually.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | Yes | N/A | GLSL fragment shader source code (GLSL ES 3.00 / WebGL 2.0 compatible). Default: A basic shader that outputs the first input image. |
| `size_mode` | COMBO | Yes | `"from_input"`<br>`"custom"` | Output size: 'from_input' uses first input image dimensions, 'custom' allows manual size. |
| `width` | INT | No | 1 to 16384 | The width of the output image when `size_mode` is set to `"custom"`. Default: 512. |
| `height` | INT | No | 1 to 16384 | The height of the output image when `size_mode` is set to `"custom"`. Default: 512. |
| `images` | IMAGE | Yes | 1 to 5 images | Input images to be processed by the shader. Images are available as `u_image0` to `u_image4` (sampler2D) in the shader code. |
| `floats` | FLOAT | No | 0 to 20 floats | Floating-point uniform values for the shader. Floats are available as `u_float0` to `u_float19` in the shader code. Default: 0.0. |
| `ints` | INT | No | 0 to 20 integers | Integer uniform values for the shader. Ints are available as `u_int0` to `u_int19` in the shader code. Default: 0. |
| `bools` | BOOLEAN | No | 0 to 10 booleans | Boolean uniform values for the shader. Booleans are available as `u_bool0` to `u_bool9` (bool) in the shader code. Default: False. |
| `curves` | CURVE | No | 0 to 4 curves | Curve uniform values for the shader. Curves are available as `u_curve0` to `u_curve3` (sampler2D, 1D LUT) in the shader code. Sample with `texture(u_curve0, vec2(x, 0.5)).r`. |

**Notes:**

* The `width` and `height` parameters are only required and visible when `size_mode` is set to `"custom"`.
* At least one input image is required.
* The shader code always has access to a `u_resolution` (vec2) uniform containing the output dimensions.
* A maximum of 5 input images, 20 float uniforms, 20 integer uniforms, 10 boolean uniforms, and 4 curve uniforms can be provided.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `IMAGE0` | IMAGE | The first output image from the shader. Available via `layout(location = 0) out vec4 fragColor0` in the shader code. |
| `IMAGE1` | IMAGE | The second output image from the shader. Available via `layout(location = 1) out vec4 fragColor1` in the shader code. |
| `IMAGE2` | IMAGE | The third output image from the shader. Available via `layout(location = 2) out vec4 fragColor2` in the shader code. |
| `IMAGE3` | IMAGE | The fourth output image from the shader. Available via `layout(location = 3) out vec4 fragColor3` in the shader code. |

---
**Source fingerprint (SHA-256):** `ded589d5b0cb5413ecc42c7177e3076427ceac1d3218a20cfec6f2e005fe7e27`
