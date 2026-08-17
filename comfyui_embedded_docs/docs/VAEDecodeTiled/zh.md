# VAE解码（分块）

VAEDecodeTiled 节点使用分块方法将潜在表示解码为图像，从而高效处理大尺寸图像。它通过将输入分割为较小的图块来处理，以在保持图像质量的同时管理内存使用。该节点还支持视频 VAE，通过分块处理带有重叠的时间帧，实现平滑过渡。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 要解码为图像的潜在表示 | LATENT | 是 | - |
| `vae` | 用于解码潜在样本的 VAE 模型 | VAE | 是 | - |
| `tile_size` | 每个图块的处理大小（默认值：512） | INT | 是 | 64-4096（步长：32） |
| `overlap` | 相邻图块之间的重叠量（默认值：64） | INT | 是 | 0-4096（步长：32） |
| `temporal_size` | 仅用于视频 VAE：每次解码的帧数（默认值：64） | INT | 是 | 8-4096（步长：4） |
| `temporal_overlap` | 仅用于视频 VAE：重叠的帧数（默认值：8） | INT | 是 | 4-4096（步长：4） |

**注意：** 如果重叠值超出实际限制，节点会自动调整。如果 `tile_size` 小于 `overlap` 的 4 倍，则重叠会减少为图块大小的四分之一。同样，如果 `temporal_size` 小于 `temporal_overlap` 的 2 倍，则时间重叠会减半。节点还会在计算空间和时间维度的图块大小及重叠大小时，考虑 VAE 的内部压缩率。对于没有时间压缩的 VAE（非视频 VAE），`temporal_size` 和 `temporal_overlap` 参数将被忽略。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `IMAGE` | 从潜在表示解码生成的图像。解码视频潜在表示时，所有解码帧会合并为单个图像列表。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/zh.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
