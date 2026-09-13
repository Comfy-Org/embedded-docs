# YuE2 生成 ABC

此节点使用 YuE2 文本与歌词模型，根据风格描述和歌词为歌曲生成 ABC 记谱。生成的 `abc` 输出可以连接到 YuE2 Generate Music 节点以生成音频。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用于对风格和歌词进行分词并生成 ABC 记谱的 YuE2 模型。 | CLIP | 是 | - |
| `style` | 描述歌曲音乐风格的文本。 | STRING | 是 | - |
| `lyrics` | 包含歌曲歌词的文本。 | STRING | 是 | - |
| `种子` | 用于生成的随机种子。更改它会产生不同的结果。默认值：0。 | INT | 是 | 0 到 18446744073709551615 |
| `模式` | full：生成旋律与和弦；melody：仅生成旋律，推荐用于翻唱。 | COMBO | 是 | "full"<br>"melody" |
| `max_abc_tokens` | 为 ABC 记谱生成的最大 token 数量。默认值：8192。 | INT | 是 | 1 到 20000 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `abc` | 生成的歌曲 ABC 记谱，可以连接到 YuE2 Generate Music 节点。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/zh.md)

---
**Source fingerprint (SHA-256):** `3e06f980a53e90b750f4190a95199e0e5ed1bd8c54d4dbf8485602ff1af00102`
