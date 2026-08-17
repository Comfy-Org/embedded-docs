# TextEncodeAceStepAudio1.5

TextEncodeAceStepAudio1.5 节点准备用于 AceStepAudio 1.5 模型的文本和音频相关元数据。它接收描述性标签、歌词和音乐参数，然后使用 CLIP 模型将其转换为适合音频生成的条件格式。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于对输入文本进行分词和编码的 CLIP 模型。 | CLIP | 是 | N/A |
| `tags` | 用于描述音频的标签，如流派、情绪或乐器。支持多行输入和动态提示词。 | STRING | 是 | N/A |
| `lyrics` | 音频曲目的歌词。支持多行输入和动态提示词。 | STRING | 是 | N/A |
| `seed` | 用于可重现生成的随机种子值。带有 control_after_generate 控件。默认值：0。 | INT | 否 | 0 to 18446744073709551615 |
| `bpm` | 生成音频的每分钟节拍数（BPM）。默认值：120。 | INT | 否 | 10 to 300 |
| `duration` | 音频的期望时长（秒）。默认值：120.0。 | FLOAT | 否 | 0.0 to 2000.0 |
| `timesignature` | 音乐拍号。 | COMBO | 否 | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | 输入文本的语言。默认值："en"。 | COMBO | 否 | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | 音乐调性与音阶（大调或小调）。 | COMBO | 否 | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | 启用生成音频编码的 LLM。这可能较慢，但会提高生成音频的质量。如果向模型提供音频参考，请关闭此选项。默认值：True。 | BOOLEAN | 否 | N/A |
| `cfg_scale` | 无分类器引导尺度。数值越高，输出越贴近提示词。默认值：2.0。 | FLOAT | 否 | 0.0 to 100.0 |
| `temperature` | 采样温度。数值越低，输出越具有确定性。默认值：0.85。 | FLOAT | 否 | 0.0 to 2.0 |
| `top_p` | 核采样概率（top-p）。默认值：0.9。 | FLOAT | 否 | 0.0 to 2000.0 |
| `top_k` | 要考虑的最高概率 token 数量（top-k）。默认值：0。 | INT | 否 | 0 to 100 |
| `min_p` | token 采样的最小概率阈值（min-p）。默认值：0.000。 | FLOAT | 否 | 0.0 to 1.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 条件数据，其中包含供 AceStepAudio 1.5 模型使用的编码文本和音频参数。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/zh.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
