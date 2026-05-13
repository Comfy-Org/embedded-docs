> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/zh.md)

GLSL 着色器节点可将自定义 GLSL ES 片段着色器代码应用于输入图像。它允许您编写着色器程序，处理多个图像并接受统一参数（浮点数、整数、布尔值和曲线），从而创建复杂的视觉效果。输出尺寸可由第一个输入图像决定，也可手动设置。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | 是 | 不适用 | GLSL 片段着色器源代码（兼容 GLSL ES 3.00 / WebGL 2.0）。默认值：输出第一个输入图像的基本着色器。 |
| `size_mode` | COMBO | 是 | `"from_input"`<br>`"custom"` | 输出尺寸：'from_input' 使用第一个输入图像的尺寸，'custom' 允许手动设置尺寸。 |
| `width` | INT | 否 | 1 至 16384 | 当 `size_mode` 设置为 `"custom"` 时，输出图像的宽度。默认值：512。 |
| `height` | INT | 否 | 1 至 16384 | 当 `size_mode` 设置为 `"custom"` 时，输出图像的高度。默认值：512。 |
| `images` | IMAGE | 是 | 1 至 8 张图像 | 由着色器处理的输入图像。在着色器代码中，图像可作为 `u_image0` 到 `u_image7`（sampler2D）使用。 |
| `floats` | FLOAT | 否 | 0 至 8 个浮点数 | 着色器的浮点统一值。在着色器代码中，浮点数可作为 `u_float0` 到 `u_float7` 使用。默认值：0.0。 |
| `ints` | INT | 否 | 0 至 8 个整数 | 着色器的整数统一值。在着色器代码中，整数可作为 `u_int0` 到 `u_int7` 使用。默认值：0。 |
| `布尔值` | BOOLEAN | 否 | 0 至 8 个布尔值 | 着色器的布尔统一值。在着色器代码中，布尔值可作为 `u_bool0` 到 `u_bool7`（bool）使用。默认值：False。 |
| `曲线` | CURVE | 否 | 0 至 8 条曲线 | 着色器的曲线统一值。在着色器代码中，曲线可作为 `u_curve0` 到 `u_curve7`（sampler2D，一维查找表）使用。使用 `texture(u_curve0, vec2(x, 0.5)).r` 进行采样。 |

**注意：**

* 仅当 `size_mode` 设置为 `"custom"` 时，`width` 和 `height` 参数才为必填项并可见。
* 至少需要一张输入图像。
* 着色器代码始终可以访问包含输出尺寸的 `u_resolution`（vec2）统一变量。
* 最多可提供 8 张输入图像、8 个浮点统一变量、8 个整数统一变量、8 个布尔统一变量和 8 个曲线统一变量。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE1` | IMAGE | 着色器的第一个输出图像。在着色器代码中通过 `layout(location = 0) out vec4 fragColor0` 使用。 |
| `IMAGE2` | IMAGE | 着色器的第二个输出图像。在着色器代码中通过 `layout(location = 1) out vec4 fragColor1` 使用。 |
| `IMAGE3` | IMAGE | 着色器的第三个输出图像。在着色器代码中通过 `layout(location = 2) out vec4 fragColor2` 使用。 |
| `IMAGE3` | IMAGE | 着色器的第四个输出图像。在着色器代码中通过 `layout(location = 3) out vec4 fragColor3` 使用。 |

---
**Source fingerprint (SHA-256):** `7830977409a5efab205b7c927eb83499a9e1e8299959b34643c9c3f1f586c058`
