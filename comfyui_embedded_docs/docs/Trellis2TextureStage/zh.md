# Trellis2TextureStage

此节点为 Trellis2 生成设置纹理阶段采样过程。它从传入的 shape latent 中读取坐标布局和逐体素的形状潜变量，在相同的坐标布局下构建一个具有 32 个通道的空稀疏潜变量，并将所需的纹理阶段元数据附加到 conditioning 上。

## 输入

| 参数 | 说明 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 用于纹理生成阶段的正向条件。纹理阶段元数据将附加到其上。 | CONDITIONING | 是 | - |
| `negative` | 用于纹理生成阶段的负向条件。纹理阶段元数据将附加到其上。 | CONDITIONING | 是 | - |
| `shape_latent` | 由 Trellis2ShapeStage 或 Trellis2UpsampleStage 生成的潜变量字典。它必须包含 `coords`（坐标布局，形状为 [N, 4]）和 `samples`（逐体素的形状潜变量）；`coord_resolution` 和 `model_frame` 为可选。 | LATENT | 是 | - |

注意：
- `shape_latent` 必须是 Trellis2ShapeStage 或 Trellis2UpsampleStage 的输出；它提供纹理阶段使用的坐标布局和逐体素的形状潜变量。
- 坐标布局会经过验证：`coords` 第一列中的批次 ID 必须为非负且连续，总行数必须与坐标计数匹配。
- 当 `positive` 携带投影特征包（Pixal3D 条件）且 `shape_latent` 包含 `coord_resolution` 时，将计算 1024 纹理分辨率下的投影特征，并将其附加到条件上。
- 模型坐标系从 `shape_latent` 中读取；若不存在，则默认使用 `"y_up"`（当存在投影特征时）或 `"z_up"`（其他情况）。

## 输出

| 输出名称 | 说明 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 附加了纹理阶段元数据的正向条件（包括生成模式、坐标、坐标计数、形状潜变量、模型坐标系，以及适用时的投影特征）。 | CONDITIONING |
| `negative` | 附加了相同纹理阶段元数据的负向条件。 | CONDITIONING |
| `latent` | 一个与传入形状潜变量具有相同坐标布局、包含 32 个通道的新空稀疏潜变量。其字典包含 `samples`、`type`（"trellis2"）、`coords`、`coord_counts` 和 `model_frame`；当可用时还会包含 `coord_resolution`。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/zh.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
