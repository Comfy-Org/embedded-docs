> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/zh.md)

JsonExtractString 节点读取包含 JSON 数据的文本字符串，并提取与特定键关联的值。它将提取的值转换为字符串。如果 JSON 无效、未找到键或值为 null，节点将返回一个空字符串。

## 输入参数

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `json_string` | STRING | 是 | N/A | 包含待解析 JSON 数据的文本。 |
| `key` | STRING | 是 | N/A | 需要从 JSON 对象中提取其字符串值的特定键。 |

**注意：** 该节点仅从 JSON 对象（字典）中提取值。如果解析的 JSON 不是对象，或者指定的键在其中不存在，则输出将是一个空字符串。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | STRING | 从 JSON 中为指定键提取的字符串值，如果提取失败则为空字符串。 |