# BakeNormalMapFromMesh

此节点将高多边形网格的表面细节烘焙到低多边形网格的 UV 布局上，生成切线空间法线贴图，捕捉减面过程中丢失的表面细节。连接已展开 UV 的低多边形网格及其来源的高多边形网格，节点将输出一张可直接用于 Apply Texture To Mesh 的 `normal_map` 输入的图像。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | 接收烘焙细节的已展开 UV 的低多边形网格。必须已有 UV 坐标；此节点从不执行展开操作。 | MESH | 是 | — |
| `high_poly` | 其表面细节被烘焙到低多边形 UV 布局中的高多边形网格。 | MESH | 是 | — |
| `resolution` | 方形输出法线贴图的边长（像素），默认值：1024。 | INT | 是 | 64 to 8192 (step 64) |
| `cage_distance` | 表面搜索范围，以包围盒对角线为比例。在强力减面导致贴片错误或缺失时可增大；若发生跨间隙捕获则减小。默认值：0.05。 | FLOAT | 是 | 0.001 to 0.5 (step 0.001) |
| `ignore_backfaces` | 跳过背离纹素的高多边形表面，使缝隙/封闭空间不会抓到对侧壁面。仅在高多边形绕序不一致时禁用。默认值：true。 | BOOLEAN | 是 | true / false |

注意：`low_poly` 必须具有 UV 坐标。若没有，节点将报错，因为烘焙依赖现有的 UV 布局，不会对网格进行展开。当 `low_poly` 为批次时，每个项目按顺序烘焙；若 `high_poly` 仅包含一个项目，则该项目会被重复用于批次中的每一项。批次中的空网格会被跳过并发出警告，同时生成纯中灰色（0.5）的法线贴图。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `normal_map` | 烘焙生成的切线空间法线贴图（glTF/OpenGL +Y 约定），为方形的 resolution × resolution RGB 图像，值域为 [0,1]。将其连接到 Apply Texture To Mesh 的 `normal_map` 输入。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/zh.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
