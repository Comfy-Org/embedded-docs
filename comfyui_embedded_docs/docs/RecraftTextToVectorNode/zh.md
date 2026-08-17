# Recraft 文本转矢量

使用 Recraft V3 模型根据文本提示同步生成 SVG 矢量插图。该节点将提示词及任何可选设置发送到 Recraft API，并返回以 SVG 数据形式生成的矢量插图。

## 输入

| 参数 | 说明 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 图像生成提示词。（默认：""，最大长度：1000 个字符） | STRING | 是 | - |
| `substyle` | 用于生成的特定矢量插图风格。 | COMBO | 是 | `"2d_character"`<br>`"2d_gradient"`<br>`"2d_illustration"`<br>`"2d_flat_character"`<br>`"2d_flat_illustration"`<br>`"2d_art"`<br>`"2d_art_character"`<br>`"2d_pattern"`<br>`"2d_pixel_art"`<br>`"2d_cyberpunk"`<br>`"2d_engraving"`<br>`"2d_black_and_white"`<br>`"2d_ink"`<br>`"2d_sketch"`<br>`"2d_watercolor"`<br>`"2d_animation"`<br>`"2d_comic"`<br>`"2d_children_illustration"`<br>`"2d_vintage"`<br>`"2d_retro"`<br>`"2d_hand_drawn"`<br>`"2d_psychedelic"`<br>`"2d_graffiti"`<br>`"2d_ukiyo_e"`<br>`"2d_woodcut"`<br>`"2d_art_deco"`<br>`"2d_art_nouveau"`<br>`"2d_bauhaus"`<br>`"2d_constructivism"`<br>`"2d_cubism"`<br>`"2d_futurism"`<br>`"2d_glitch"`<br>`"2d_impressionism"`<br>`"2d_naive"`<br>`"2d_pointillism"`<br>`"2d_pop_art"`<br>`"2d_realism"`<br>`"2d_renaissance"`<br>`"2d_rococo"`<br>`"2d_romanticism"`<br>`"2d_surrealism"`<br>`"2d_suprematism"`<br>`"2d_symbolism"`<br>`"2d_expressionism"`<br>`"2d_abstract"`<br>`"2d_minimalism"`<br>`"2d_contemporary"`<br>`"2d_modern"`<br>`"2d_brutalism"`<br>`"2d_metaphysical"`<br>`"2d_mannerism"`<br>`"2d_baroque"`<br>`"2d_neoclassicism"`<br>`"2d_orientalism"`<br>`"2d_primitivism"`<br>`"2d_fauvism"`<br>`"2d_rayonism"`<br>`"2d_orphism"`<br>`"2d_vorticism"`<br>`"2d_dadaism"`<br>`"2d_neo_expressionism"`<br>`"2d_transavantgarde"`<br>`"2d_new_wild"`<br>`"2d_graffiti_classic"`<br>`"2d_graffiti_modern"`<br>`"2d_graffiti_wildstyle"`<br>`"2d_graffiti_bubble"`<br>`"2d_graffiti_throwup"`<br>`"2d_graffiti_tag"`<br>`"2d_graffiti_blockbuster"`<br>`"2d_graffiti_mural"`<br>`"2d_graffiti_stencil"`<br>`"2d_graffiti_3d"`<br>`"2d_graffiti_character"`<br>`"2d_graffiti_abstract"`<br>`"2d_graffiti_urban"`<br>`"2d_graffiti_neo_muralism"`<br>`"2d_graffiti_post_graffiti"`<br>`"2d_graffiti_street_art"` |
| `size` | 生成图像的尺寸。（默认："1024x1024"） | COMBO | 是 | `"1024x1024"`<br>`"1024x2048"`<br>`"2048x1024"`<br>`"2048x2048"`<br>`"512x512"`<br>`"512x1024"`<br>`"1024x512"`<br>`"2048x512"`<br>`"512x2048"` |
| `n` | 要生成的图像数量。（默认：1，最小：1，最大：6） | INT | 是 | 1-6 |
| `seed` | 用于确定节点是否应重新运行的种子；无论种子如何，实际结果都是不确定的。（默认：0，最小：0，最大：18446744073709551615） | INT | 是 | 0-18446744073709551615 |
| `negative_prompt` | 关于图像中不需要元素的可选文本描述。（默认：""） | STRING | 否 | - |
| `recraft_controls` | 通过 Recraft Controls 节点对生成过程进行的可选附加控制。 | CONTROLS | 否 | - |

**注意：**`prompt` 限制为最多 1000 个字符。空的 `negative_prompt` 被视为无负面提示词，并且不会发送到 API。`seed` 参数仅控制节点何时重新运行，并不会使生成结果具有确定性。

## 输出

| 输出名称 | 说明 | 数据类型 |
|-------------|-------------|-----------|
| `SVG` | 以 SVG 格式生成的矢量插图 | SVG |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/zh.md)

---
**Source fingerprint (SHA-256):** `aec7e96e339047e75dfe419d94d23a613595bc22e7f187895c52b143780fcbf3`
