> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/zh.md)

Flux KV Cache 节点为 Flux 系列模型应用键值（KV）缓存优化。此优化专门设计用于在使用参考图像时通过缓存特定计算来提升性能，从而加速生成过程。

## 输入参数

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | | 要应用 KV Cache 的模型。 |

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已启用 KV Cache 的修补后模型。 |