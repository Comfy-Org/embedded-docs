# Trellis2ShapeStage

此节点用于设置 Trellis2 流水线中的第一个形状生成采样遍。它接收 `VaeDecodeStructureTrellis2` 生成的稠密结构体素，提取已填充体素的稀疏坐标，创建一个空的稀疏 latent，并将采样元数据附加到 conditioning 上，以便模型在采样期间读取这些元数据。对于上采样后的第二个形状遍，请改用 `Trellis2UpsampleStage`，它会结合级联与第二遍阶段设置。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 为形状阶段准备的正向 conditioning。可以是标准的 Trellis2 conditioning，也可以是提供投影特征包的 Pixal3D conditioning；当存在投影特征时，会为所选阶段计算这些特征并附加到输出 conditioning 上。 | CONDITIONING | 是 | 任意 Trellis2 或 Pixal3D conditioning |
| `negative` | 为形状阶段准备的负向 conditioning。与正向 conditioning 相同，形状阶段元数据也会附加到其上。 | CONDITIONING | 是 | 任意 Trellis2 或 Pixal3D conditioning |
| `voxel` | 来自 `VaeDecodeStructureTrellis2` 的稠密结构体素。 | VOXEL | 是 | 任意体素网格；网格分辨率（每轴体素数）选择流水线阶段 |

### 备注

- 体素网格分辨率会选择流水线阶段：分辨率小于或等于 32 时使用 `shape_generation_512` 模式及 `shape_512` 阶段；分辨率大于 32 时使用 `shape_generation` 模式及 `shape_1024` 阶段。
- 体素必须至少包含一个已填充体素；空体素会引发错误。从体素导出的批次索引必须为非负且连续。
- 当 `positive` conditioning 包含 `proj_feat_pack`（由 Pixal3D conditioning 提供）时，会为所选阶段计算投影特征，并将输出 latent 的模型坐标系设置为 `y_up`。否则，不附加投影特征，模型坐标系设置为 `z_up`。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 附加了形状阶段元数据的正向 conditioning：生成模式、稀疏坐标、每批次坐标数量，以及当源 conditioning 提供时的投影特征。 | CONDITIONING |
| `negative` | 附加了相同形状阶段元数据的负向 conditioning。 | CONDITIONING |
| `latent` | 一个空的稀疏 latent 张量（形状：批次大小、32、token 数量、1），以及提取出的稀疏坐标、每批次坐标数量、坐标分辨率、类型标记 `trellis2` 和模型坐标系方向。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/zh.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
