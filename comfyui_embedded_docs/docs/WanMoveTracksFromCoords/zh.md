# WanMove坐标到轨道

WanMoveTracksFromCoords 节点根据 JSON 格式的坐标字符串创建运动轨迹。它将坐标数据转换为可供其他视频处理节点使用的张量格式，并可选择应用遮罩来控制轨迹随时间的可见性。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `track_coords` | 包含轨迹坐标数据的 JSON 格式字符串。默认值为空列表（`"[]"`）。 | STRING | 否 | N/A |
| `track_mask` | 可选的遮罩。当提供时，节点使用它来确定每个轨迹在每一帧的可见性。当未提供时，所有轨迹在所有帧中均视为可见。 | MASK | 否 | N/A |

**注意：** `track_coords` 输入需要特定的 JSON 结构。它应为轨迹列表，其中每条轨迹是帧列表，每个帧是包含 `x` 和 `y` 坐标的对象。所有轨迹的帧数必须一致。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `tracks` | 生成的轨迹数据，包含每条轨迹的路径坐标和可见性信息。 | TRACKS |
| `track_length` | 生成轨迹中的总帧数。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/zh.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
