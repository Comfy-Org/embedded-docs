# Recraft 移除背景

此节点使用 Recraft API 服务从图像中移除背景。它处理输入批次中的每个图像，并返回具有透明背景的处理后图像，以及指示已移除背景区域的相应 alpha 遮罩。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要移除背景的输入图像 | IMAGE | 是 | - |

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 带有透明背景的处理后图像 | IMAGE |
| `mask` | 指示已移除背景区域的 alpha 通道遮罩 | MASK |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/zh.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
