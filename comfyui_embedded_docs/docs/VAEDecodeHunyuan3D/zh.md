# VAE解码（Hunyuan3D）

VAEDecodeHunyuan3D 节点使用 VAE 解码器将潜在表示转换为 3D 体素数据。它通过 VAE 模型处理潜在样本，并具有可配置的分块和分辨率设置，以生成适用于 3D 应用的体积数据。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 要解码为 3D 体素数据的潜在表示 | LATENT | 是 | - |
| `vae` | 用于解码潜在样本的 VAE 模型 | VAE | 是 | - |
| `num_chunks` | 将处理过程拆分为多个块以进行内存管理的块数（默认值：8000） | INT | 是 | 1000-500000 |
| `octree_resolution` | 用于 3D 体素生成的八叉树结构的分辨率（默认值：256） | INT | 是 | 16-512 |

注意：`num_chunks` 和 `octree_resolution` 是高级参数。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `voxels` | 从解码后的潜在表示生成的 3D 体素数据 | VOXEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/zh.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
