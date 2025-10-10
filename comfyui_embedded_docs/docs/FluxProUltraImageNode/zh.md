> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/zh.md)

使用 Flux Pro 1.1 Ultra 通过 API 根据提示词和分辨率生成图像。此节点连接到外部服务，根据您的文本描述和指定尺寸创建图像。

## 输入参数

| 参数名称 | 数据类型 | 必填 | 取值范围 | 参数说明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 图像生成的提示词（默认：空字符串） |
| `prompt_upsampling` | BOOLEAN | 否 | - | 是否对提示词进行上采样处理。启用时，会自动修改提示词以获得更具创意的生成结果，但结果具有不确定性（相同种子不会产生完全相同的结果）。（默认：False） |
| `seed` | INT | 否 | 0 到 18446744073709551615 | 用于创建噪声的随机种子。（默认：0） |
| `aspect_ratio` | STRING | 否 | - | 图像宽高比；必须在 1:4 到 4:1 之间。（默认："16:9"） |
| `raw` | BOOLEAN | 否 | - | 为 True 时，生成较少处理、更自然外观的图像。（默认：False） |
| `image_prompt` | IMAGE | 否 | - | 可选参考图像，用于引导生成过程 |
| `image_prompt_strength` | FLOAT | 否 | 0.0 到 1.0 | 在提示词和图像提示之间的混合强度。（默认：0.1） |

**注意：** `aspect_ratio` 参数必须在 1:4 到 4:1 之间。当提供 `image_prompt` 时，`image_prompt_strength` 将变为活动状态，控制参考图像对最终输出的影响程度。

## 输出结果

| 输出名称 | 数据类型 | 输出说明 |
|-------------|-----------|-------------|
| `output_image` | IMAGE | 由 Flux Pro 1.1 Ultra 生成的图像 |