`CLIP文本编码Flux` 是 ComfyUI 中专为 Flux 架构设计的高级文本编码节点。它采用双文本编码器（CLIP-L 与 T5XXL）协同机制，能够同时处理结构化关键词和详细自然语言描述，为 Flux 模型提供更精准、更丰富的文本理解能力，提升文本到图像的生成质量。

该节点基于双编码器协作机制：

1. `clip_l` 输入会被 CLIP-L 编码器处理，提取风格、主题等关键词特征，适合简洁描述。
2. `t5xxl` 输入由 T5XXL 编码器处理，擅长理解复杂、细致的自然语言场景描述。
3. 两路编码结果融合后，结合"引导"参数，生成统一的条件嵌入（CONDITIONING），用于下游的 Flux 采样器节点，控制生成内容与文本描述的契合度。

## 输入

| 参数名称 | 数据类型 | 输入方式 | 默认值 | 取值范围 | 功能说明 |
|---------|---------|----------|--------|----------|----------|
| `clip` | CLIP | 节点输入 | 无 | - | 必须是支持 Flux 架构的 CLIP 模型，包含 CLIP-L 和 T5XXL 两个编码器 |
| `clip_l` | STRING | 文本框 | 无 | 最多77个token | 适合输入简洁的关键词描述，如风格、主题等 |
| `t5xxl` | STRING | 文本框 | 无 | 近乎无限制 | 适合输入详细的自然语言描述，表达复杂场景和细节 |
| `引导` | FLOAT | 滑块 | 3.5 | 0.0 - 100.0 | 控制文本条件对生成过程的影响强度，数值越大越严格遵循文本描述 |

## 输出

| 输出名称 | 数据类型 | 说明 |
|---------|---------|------|
| `条件` | CONDITIONING | 包含双编码器处理后的条件嵌入和引导参数，用于条件图像生成 |

## 使用示例

### 提示词示例

- **clip_l 输入框**（关键词风格）：
  - 使用结构化、简洁的关键词组合
  - 示例：`masterpiece, best quality, portrait, oil painting, dramatic lighting`
  - 重点描述风格、质量、主题等核心元素

- **t5xxl 输入框**（自然语言描述）：
  - 使用完整、流畅的场景描述
  - 示例：`A highly detailed portrait in oil painting style, featuring dramatic chiaroscuro lighting that creates deep shadows and bright highlights, emphasizing the subject's features with renaissance-inspired composition.`
  - 重点描述场景细节、空间关系、光影效果

### 注意事项

1. 确保使用兼容的 Flux 架构 CLIP 模型
2. 建议同时填写 clip_l 和 t5xxl，以发挥双编码器优势
3. 注意 clip_l 的词元数量限制（77个token）
4. 根据生成效果调整"引导"参数
