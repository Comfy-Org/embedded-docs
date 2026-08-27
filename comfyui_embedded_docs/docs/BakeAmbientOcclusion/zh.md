# BakeAmbientOcclusion

将高多边形网格的环境光遮蔽贴图烘焙到低多边形网格的 UV 布局中。输出是灰度图像，其中白色纹素表示开放区域，深色纹素表示裂缝；此输出用于 Apply Texture To Mesh 节点的遮挡输入。连接已展开 UV 的低多边形网格以及从中减面得到的高多边形网格。

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | 要烘焙到的已展开 UV 的低多边形网格。必须具有 UV；如果缺少 UV，节点将报错。 | MESH | Yes | - |
| `high_poly` | 低多边形网格减面自的高多边形网格，用作遮挡的源几何体。 | MESH | Yes | - |
| `resolution` | 纹理分辨率（以像素为单位）；每个纹素都会得到一个遮挡值。默认值：1024。 | INT | Yes | 64 to 8192 (step 64) |
| `samples` | 每个纹素的射线数。更多射线 = 更平滑、更慢。如果颗粒感明显，请增大此值。默认值：64。 | INT | Yes | 4 to 1024 (step 4) |
| `max_distance` | 射线长度，以包围盒对角线长度的比例表示。较小值 = 更紧密、更局部的遮挡。默认值：0.5。 | FLOAT | Yes | 0.01 to 2.0 (step 0.01) |
| `strength` | 缩放遮挡强度。>1 变暗，<1 变亮。默认值：1.0。 | FLOAT | Yes | 0.0 to 2.0 (step 0.05) |
| `bias` | 射线起点抬离表面的距离，以包围盒对角线长度的比例表示。如果平坦表面出现暗斑/孔洞，请增大此值。默认值：0.01。 | FLOAT | Yes | 0.0001 to 0.2 (step 0.0005) |

注意：`low_poly` 必须具有 UV 坐标——此节点永远不会对网格进行 UV 展开。如果 `high_poly` 仅包含一个批次项，则它会为 `low_poly` 的每个批次项重用；对于没有面的 `low_poly` 批次项，将跳过，替换为全白图像，并记录一条警告。

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `occlusion` | 灰度环境光遮蔽图像，值在 [0,1] 范围内（白色 = 开放，深色 = 裂缝），`low_poly` 每个批次项对应一张图像。用于 Apply Texture To Mesh 节点的遮挡输入（打包到 ORM 贴图 / occlusionTexture 中）。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/zh.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
