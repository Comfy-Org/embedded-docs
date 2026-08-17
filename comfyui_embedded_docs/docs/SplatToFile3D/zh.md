# 创建 3D 文件（由 Splat）

SplatToFile3D 将高斯溅射转换为 File3D 对象，该对象可用于 Save 或 Preview 3D 节点。您可以选择输出文件格式。该节点每批次仅支持一个项目；如果收到多个项目，则仅使用第一个并记录警告。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `splat` | 要序列化为文件的高斯溅射数据。每批次仅支持一个项目。如果提供了多个项目，则仅使用第一个。 | SPLAT | 是 | - |
| `format` | 3D 文件的输出文件格式。ply：标准 3D 高斯溅射，包含完整球谐函数。ksplat：mkkellogg SplatBuffer（级别 0，未压缩），仅基础颜色。spz：Niantic gzip 压缩（约小 10 倍），仅基础颜色（默认值："ply"） | COMBO | 是 | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_3d` | 包含所选格式的序列化高斯溅射数据的 File3D 对象，可用于保存或预览 | FILE3D |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/zh.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
