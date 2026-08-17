# ChromaRadiance选项

ChromaRadianceOptions 节点允许您为 Chroma Radiance 模型配置高级设置。它包装现有模型，并在去噪过程中基于 sigma 值应用特定选项，从而实现对 NeRF 瓦片大小和其他辐射相关参数的精细控制。

## 输入

| 参数 | 说明 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要应用 Chroma Radiance 选项的模型 | MODEL | 是 | - |
| `preserve_wrapper` | 启用后，将委托给现有的模型函数包装器（如果存在）。通常应保持启用状态。（默认值：True） | BOOLEAN | 否 | - |
| `start_sigma` | 这些选项生效的第一个 sigma 值。（默认值：1.0） | FLOAT | 否 | 0.0 to 1.0 |
| `end_sigma` | 这些选项生效的最后一个 sigma 值。（默认值：0.0） | FLOAT | 否 | 0.0 to 1.0 |
| `nerf_tile_size` | 允许覆盖默认的 NeRF 瓦片大小。设为 -1 表示使用默认值 (32)。设为 0 表示使用非平铺模式（可能需要大量 VRAM）。（默认值：-1） | INT | 否 | -1 and above |
| `force_sequential_txt_ids` | 强制使用顺序文本 token ID 而不是零。应应用于 2026-05-22 至 2026-06-01 期间以这种方式训练但不包含 `__sequential__` 键的检查点。（默认值：False） | BOOLEAN | 否 | - |

**注意：** Chroma Radiance 选项仅在当前 sigma 值介于 `end_sigma` 和 `start_sigma`（包含）之间时生效。`nerf_tile_size` 参数仅在设置为 0 或更高值时才应用。`force_sequential_txt_ids` 参数仅在设置为 True 时应用。

## 输出

| 输出名称 | 说明 | 数据类型 |
|-------------|-------------|-----------|
| `model` | 已应用 Chroma Radiance 选项的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/zh.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
