# MoGe 推理

对单张图像运行 MoGe，以估计深度和几何信息。该节点通过 MoGe 模型处理输入图像，生成 3D 点云、深度图、相机内参、蒙版以及表面法线。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `moge_model` | 用于推理的 MoGe 模型。 | MOGE_MODEL | 是 | N/A |
| `image` | 用于深度和几何估计的输入图像。仅使用 RGB 通道；任何 alpha 通道都会被忽略。 | IMAGE | 是 | N/A |
| `resolution_level` | 控制处理分辨率。0 为最快，9 提供最多细节。（默认值：9） | INT | 是 | 0 到 9 |
| `fov_x_degrees` | （高级）源相机在水平方向上的视场角，单位为度。设置用于将深度图反投影到 3D 的焦距。设置为 0.0 可从预测点自动恢复视场角。（默认值：0.0） | FLOAT | 是 | 0.0 到 170.0 |
| `batch_size` | 每次推理调用时处理的图像数量。如果在处理长视频或大型图像集时内存不足，请降低此值。（默认值：4） | INT | 是 | 1 到 64 |
| `force_projection` | （高级）强制对预测点进行投影。（默认值：True） | BOOLEAN | 是 | True/False |
| `apply_mask` | （高级）启用后，会将蒙版覆盖（天空或无效）像素在点和深度输出中设置为无穷大。这有助于网格化工具忽略这些区域。禁用则保留所有位置的原始预测几何体；蒙版仍会单独返回。（默认值：True） | BOOLEAN | 是 | True/False |

注意：`image` 输入可以包含多张图像。该节点按 `batch_size` 分组处理这些图像，并将结果合并为单个输出。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `moge_geometry` | 包含估计几何信息的字典。它始终包含输入的 `image`（仅 RGB 通道），并且可能包含 `points`（3D 点云）、`depth`（深度图）、`intrinsics`（相机内参矩阵）、`mask`（标识有效像素的蒙版）和 `normal`（表面法线）。 | MOGE_GEOMETRY |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/zh.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
