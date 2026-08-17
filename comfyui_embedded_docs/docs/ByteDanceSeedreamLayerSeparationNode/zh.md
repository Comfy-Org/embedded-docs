# ByteDance Seedream 5.0 Pro 图层分离

ByteDance Seedream 5.0 Pro Layer Separation 可将图像分解为一个背景底板及最多 16 个透明图层，每个图层都具有自己的堆叠顺序、边界框、名称和描述。它返回背景、带蒙版的逐层图像、放置框，以及一个可直接编辑的图层堆栈。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要分离的图像。必须为单张图像，至少 512x512 像素，宽高比在 1:16 到 16:1 之间。大于约 4MP 的输入会在上传前缩小。 | IMAGE | 是 | Single image |
| `prompt` | 指定如何分离图像。留空将自动检测并分离所有主要元素。可用自然语言描述元素以控制分离结果，也可使用 `<bbox>left top right bottom</bbox>` 标签精确指定区域（0-1000 千分比坐标）。默认：空字符串。 | STRING | 是 | Multiline text |
| `size` | 输出分辨率等级。"auto" 跟随输入图像大小（限制在 1K-2K 范围内）。默认："auto"。 | COMBO | 是 | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | 生成时使用的随机种子。默认：0。 | INT | 是 | 0 to 2147483647 |
| `prompt_optimization` | 提示词优化模式："standard" 质量更高，"fast" 生成时间更短。默认："standard"。 | COMBO | 否 | "standard"<br>"fast" |
| `watermark` | 是否在图像上添加 “AI generated” 水印。默认：false。 | BOOLEAN | 否 | false<br>true |
| `crop_layers` | layers/masks 批处理输出的几何形式（`layer_stack` 不受影响，始终为紧贴裁剪）。Full canvas：每个图层放在基底尺寸画布上其边界框位置——可直接使用 ImageCompositeMasked 重新合成。Minimal size：每个图层裁剪到其边界框（为批处理填充到最大图层尺寸）——张量小得多；使用 bboxes 输出，通过 Layers From Bounding Boxes 重建放置信息。默认：false (full canvas)。 | BOOLEAN | 否 | false (full canvas)<br>true (minimal size) |

注意：输入图像必须是单张图像，不支持批次。图像至少为 512x512 像素，宽高比在 1:16 到 16:1 之间。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `base_image` | 图层堆叠于其上的基底图像（背景底板）。 | IMAGE |
| `base_mask` | 基底图像的透明度（1 = 透明，LoadImage 约定）；当前始终为完全不透明。 | MASK |
| `layers` | 按从下到上顺序排列的透明图层。Full canvas 模式：放置在基底尺寸的黑色画布上其边界框位置。Minimal size 模式：裁剪到其边界框，左上角对齐，并填充到最大图层尺寸。 | IMAGE |
| `masks` | 每个图层的透明度，与 layers 批次索引对齐（1 = 透明，LoadImage 约定）。若要进行 ImageCompositeMasked 风格合成，请先添加 InvertMask。 | MASK |
| `bboxes` | 每个图层一个放置框，与 layers 批次索引对齐（将两者与 masks 一起输入 Layers From Bounding Boxes 以重建每个图层的放置信息）：`{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`。`content_rect = [left, top, width, height]` 是图层内容在其自身画框内的区域；它落在画布上的位置为框位置加上该偏移量。 | BOUNDING_BOX |
| `layer_stack` | 可供 Create Layered Image 使用的、可直接编辑的图层文档：包含基底底板，以及每个元素作为独立的、命名的、紧贴裁剪的图层，并保持其真实位置和堆叠顺序。可直接连接，或使用 Add Layer 扩展。 | LAYERS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/zh.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
