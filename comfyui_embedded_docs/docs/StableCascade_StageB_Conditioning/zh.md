> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/zh.md)

StableCascade_StageB_Conditioning 节点通过将现有条件信息与来自 Stage C 的先验潜在表示相结合，为 Stable Cascade Stage B 生成准备条件数据。该节点会修改条件数据以包含来自 Stage C 的潜在样本，使生成过程能够利用先验信息来获得更连贯的输出。

## 输入参数

| 参数名 | 数据类型 | 必需 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 待修改的条件数据，将加入 Stage C 先验信息 |
| `stage_c` | LATENT | 是 | - | 来自 Stage C 的潜在表示，包含用于条件处理的先验样本 |

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 已整合 Stage C 先验信息的修改后条件数据 |