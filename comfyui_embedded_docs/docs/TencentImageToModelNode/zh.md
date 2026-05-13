> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/zh.md)

此节点使用腾讯混元3D Pro API，根据一张或多张输入图像生成3D模型。它会处理图像、发送至API，并返回生成的GLB和OBJ格式3D模型文件，以及可选的纹理贴图。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"3.0"`<br>`"3.1"` | 要使用的混元3D模型版本。`3.1`模型不支持LowPoly选项。 |
| `image` | IMAGE | 是 | - | 用于生成3D模型的主要输入图像。分辨率至少为128x128像素。 |
| `image_left` | IMAGE | 否 | - | 物体左侧的可选图像，用于多视角生成。分辨率至少为128x128像素。 |
| `image_right` | IMAGE | 否 | - | 物体右侧的可选图像，用于多视角生成。分辨率至少为128x128像素。 |
| `image_back` | IMAGE | 否 | - | 物体背面的可选图像，用于多视角生成。分辨率至少为128x128像素。 |
| `face_count` | INT | 是 | 3000 - 1500000 | 生成3D模型的目标面数（默认值：500000）。 |
| `generate_type` | DYNAMICCOMBO | 是 | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | 要生成的3D模型类型。选择某个选项会显示额外的相关参数。 |
| `generate_type.pbr` | BOOLEAN | 否 | - | 启用基于物理渲染（PBR）材质生成。此参数仅在`generate_type`设置为"Normal"或"LowPoly"时可见（默认值：False）。 |
| `generate_type.polygon_type` | COMBO | 否 | `"triangle"`<br>`"quadrilateral"` | 网格使用的多边形类型。此参数仅在`generate_type`设置为"LowPoly"时可见。 |
| `seed` | INT | 是 | 0 - 2147483647 | 生成过程的种子值。种子控制节点是否应重新运行；无论种子如何，结果均非确定性（默认值：0）。 |

**注意：** 所有输入图像的最小宽度和高度必须为128像素。如果图像最长边超过4900像素，则会自动缩小。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `model_file` | STRING | 用于向后兼容的旧版输出。 |
| `GLB` | FILE3DGLB | 以GLB（二进制GL传输格式）文件格式生成的3D模型。 |
| `OBJ` | FILE3DOBJ | 以OBJ（Wavefront）文件格式生成的3D模型。 |
| `texture_image` | IMAGE | 生成3D模型的纹理图像。 |
| `optional_metallic` | IMAGE | PBR材质的金属度贴图。若不可用则返回黑色图像。 |
| `optional_normal` | IMAGE | PBR材质的法线贴图。若不可用则返回黑色图像。 |
| `optional_roughness` | IMAGE | PBR材质的粗糙度贴图。若不可用则返回黑色图像。 |

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
