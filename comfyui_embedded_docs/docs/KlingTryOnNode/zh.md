# Kling Virtual Try-On

使用 Kling 的虚拟试穿功能为人物穿上服装。连接一张人物照片和一张服装照片，节点会返回该人物穿着该服装的新图像。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `person_image` | 单人照片，最好是正面或四分之三视角。任一边超过 2048 像素的图像会先被缩小。 | IMAGE | 是 | N/A |
| `garment_image` | 要穿上的服装：产品图、平铺图、人台图或模特上身图。模特上身图可能会沿用该套装的其余部分。仅支持服装；不支持鞋子、包和配饰。 | IMAGE | 是 | N/A |
| `keep_pose` | 关闭后允许改变姿势，以获得更好的服装展示效果。高级参数（默认：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `seed` | `seed` 控制节点是否应重新运行；无论 `seed` 为何，结果都是非确定性的。此参数具有“生成后控制”功能（默认：42）。 | INT | 是 | 0 到 2147483647 |

**注意：** 结果尺寸与 `person_image` 相同，最长边限制为 2048 像素。两个输入都会上传到 Kling 的 API，这可能需要一些时间。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `IMAGE` | 穿着该服装的人物。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/zh.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`
