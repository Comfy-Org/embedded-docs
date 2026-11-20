# Model Merge MiniMax H3

此节点按组件合并两个兼容的 MiniMax H3 模型，并可分别为架构中的每个部分设置独立的混合比例。提高某个比例会使该组件更多地取自 `model2`，因此你可以保留其中一个模型的 patch 投影和细化模块，同时用另一个模型替换 transformer 模块。

## 输入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model1` | 第一个 MiniMax H3 模型，作为基础模型，所有组件都取自它（在未使用 `model2` 的地方应用默认权重）。 | MODEL | 是 | - |
| `model2` | 第二个 MiniMax H3 模型，提供你要混入的组件。 | MODEL | 是 | - |
| `video_patch_proj.` | 视频 patch 投影取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `audio_patch_proj.` | 音频 patch 投影取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `condition_proj.` | 条件投影取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `time_embedder.` | 时间嵌入器取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `token_refiner.blocks.0.` | 第一个 token 细化块取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `token_refiner.blocks.1.` | 第二个 token 细化块取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `token_refiner.final_norm.` | token 细化器最终归一化取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `blocks.0.` 到 `blocks.49.` | 50 个 transformer 块中每个块取自 `model2` 的比例，每个块对应一个控件（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `final_layer.norm.` | 最终层归一化取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `final_layer.adaln_proj.` | 最终自适应归一化投影取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `final_layer.video_out.` | 视频输出层取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |
| `final_layer.audio_out.` | 音频输出层取自 `model2` 的比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |

比例为 0.0 时该组件完全取自 `model1`，为 1.0 时完全取自 `model2`；介于两者之间的数值会对两个模型进行混合。不带比例的张量（例如归一化统计量）始终来自 `model1`。两个输入必须都是架构相同的 MiniMax H3 模型，否则合并生成的模型将无法运行。

## 输出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `MODEL` | 合并后的 MiniMax H3 模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/zh.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
