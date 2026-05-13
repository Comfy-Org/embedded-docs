> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/zh.md)

# Kling 图像转视频摄像机控制节点

此节点可将静态图像转换为具有专业摄像机运镜的电影级视频。这款专门的图像转视频节点允许您控制虚拟摄像机动作，包括变焦、旋转、平移、俯仰和第一人称视角，同时保持对原始图像的关注。摄像机控制目前仅在专业模式下支持，使用 kling-v1-5 模型，时长为5秒。

## 输入

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 是 | - | 参考图像 - URL或Base64编码字符串，不能超过10MB，分辨率不低于300x300px，宽高比在1:2.5到2.5:1之间。Base64不应包含data:image前缀。 |
| `prompt` | STRING | 是 | - | 正向文本提示词，描述期望的视频内容 |
| `negative_prompt` | STRING | 是 | - | 负向文本提示词，描述生成视频中需要避免的内容 |
| `cfg_scale` | FLOAT | 否 | 0.0 到 1.0 | 控制文本引导的强度。数值越高，输出越严格遵循提示词（默认值：0.75） |
| `aspect_ratio` | COMBO | 否 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 生成视频的宽高比（默认值："16:9"） |
| `camera_control` | CAMERA_CONTROL | 是 | - | 可使用Kling摄像机控制节点创建。控制视频生成过程中的摄像机运动和运镜。 |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的视频输出 |
| `video_id` | STRING | 生成视频的唯一标识符 |
| `duration` | STRING | 生成视频的时长 |

---
**Source fingerprint (SHA-256):** `a2965975cd484768298f4c7e504423f782ea032dfb5ef304579715be9c27cb79`
