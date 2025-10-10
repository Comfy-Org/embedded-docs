> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/zh.md)

创建一个包含起始点和结束点之间插值强度值的钩子关键帧序列。该节点生成多个关键帧，在生成过程的指定百分比范围内平滑过渡强度参数，使用各种插值方法来控制过渡曲线。

## 输入参数

| 参数 | 数据类型 | 必需 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `strength_start` | FLOAT | 是 | 0.0 - 10.0 | 插值序列的起始强度值（默认：1.0） |
| `strength_end` | FLOAT | 是 | 0.0 - 10.0 | 插值序列的结束强度值（默认：1.0） |
| `interpolation` | COMBO | 是 | 多个选项可用 | 用于在强度值之间过渡的插值方法 |
| `start_percent` | FLOAT | 是 | 0.0 - 1.0 | 生成过程中的起始百分比位置（默认：0.0） |
| `end_percent` | FLOAT | 是 | 0.0 - 1.0 | 生成过程中的结束百分比位置（默认：1.0） |
| `keyframes_count` | INT | 是 | 2 - 100 | 插值序列中要生成的关键帧数量（默认：5） |
| `print_keyframes` | BOOLEAN | 是 | True/False | 是否将生成的关键帧信息打印到日志中（默认：False） |
| `prev_hook_kf` | HOOK_KEYFRAMES | 否 | - | 可选的先前钩子关键帧组，用于追加到其中 |

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | 包含插值序列的生成钩子关键帧组 |