> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/zh.md)

Reve Image Remix 节点使用 Reve API 生成新图像。它将一个或多个参考图像与文本提示相结合，根据提供的描述创建出新的混合图像。

## 输入参数

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `reference_images` | IMAGE | 是 | 1 到 6 张图像 | 用作混合基础的一个或多个参考图像。可以添加 1 到 6 张图像。 |
| `prompt` | STRING | 是 | 1 到 2560 个字符 | 对期望图像的文本描述。可以包含 XML `<img>` 标签来按索引引用特定图像（例如 `<img>0</img>`、`<img>1</img>`）。 |
| `model` | COMBO | 是 | `reve-remix@20250915`<br>`reve-remix-fast@20251030` | 用于混合的模型版本。每个模型选项都包含可配置的宽高比和测试时间缩放。 |
| `upscale` | COMBO | 否 | `"disabled"`<br>`"enabled"` | 控制是否对生成的图像进行放大。启用后，可以选择放大倍数。 |
| `remove_background` | BOOLEAN | 否 | `true`<br>`false` | 启用后，会尝试移除生成图像的背景。 |
| `seed` | INT | 否 | 0 到 2147483647 | 种子值。更改此值将导致节点重新运行，但结果是非确定性的。（默认值：0） |

**注意：** `model` 参数是一个动态组合框，包含 `aspect_ratio`（例如 "auto"、"16:9"、"1:1"）和 `test_time_scaling` 的嵌套设置。当 `upscale` 参数设置为 "enabled" 时，会显示嵌套的 `upscale_factor` 设置。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 由 Reve 混合过程生成的新图像。 |