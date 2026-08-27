# Recraft 文字轉向量

根據文字提示詞和解析度同步生成 SVG 向量插圖。此節點會將您的提示詞傳送至 Recraft API，並回傳生成的 SVG 內容。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 影像生成的提示詞。（預設值：""，最多 1000 個字元） | STRING | 是 | - |
| `子風格` | 用於生成的特定向量插圖風格。 | COMBO | 是 | `"2d_character"`<br>`"2d_gradient"`<br>`"2d_illustration"`<br>`"2d_flat_character"`<br>`"2d_flat_illustration"`<br>`"2d_art"`<br>`"2d_art_character"`<br>`"2d_pattern"`<br>`"2d_pixel_art"`<br>`"2d_cyberpunk"`<br>`"2d_engraving"`<br>`"2d_black_and_white"`<br>`"2d_ink"`<br>`"2d_sketch"`<br>`"2d_watercolor"`<br>`"2d_animation"`<br>`"2d_comic"`<br>`"2d_children_illustration"`<br>`"2d_vintage"`<br>`"2d_retro"`<br>`"2d_hand_drawn"`<br>`"2d_psychedelic"`<br>`"2d_graffiti"`<br>`"2d_ukiyo_e"`<br>`"2d_woodcut"`<br>`"2d_art_deco"`<br>`"2d_art_nouveau"`<br>`"2d_bauhaus"`<br>`"2d_constructivism"`<br>`"2d_cubism"`<br>`"2d_futurism"`<br>`"2d_glitch"`<br>`"2d_impressionism"`<br>`"2d_naive"`<br>`"2d_pointillism"`<br>`"2d_pop_art"`<br>`"2d_realism"`<br>`"2d_renaissance"`<br>`"2d_rococo"`<br>`"2d_romanticism"`<br>`"2d_surrealism"`<br>`"2d_suprematism"`<br>`"2d_symbolism"`<br>`"2d_expressionism"`<br>`"2d_abstract"`<br>`"2d_minimalism"`<br>`"2d_contemporary"`<br>`"2d_modern"`<br>`"2d_brutalism"`<br>`"2d_metaphysical"`<br>`"2d_mannerism"`<br>`"2d_baroque"`<br>`"2d_neoclassicism"`<br>`"2d_orientalism"`<br>`"2d_primitivism"`<br>`"2d_fauvism"`<br>`"2d_rayonism"`<br>`"2d_orphism"`<br>`"2d_vorticism"`<br>`"2d_dadaism"`<br>`"2d_neo_expressionism"`<br>`"2d_transavantgarde"`<br>`"2d_new_wild"`<br>`"2d_graffiti_classic"`<br>`"2d_graffiti_modern"`<br>`"2d_graffiti_wildstyle"`<br>`"2d_graffiti_bubble"`<br>`"2d_graffiti_throwup"`<br>`"2d_graffiti_tag"`<br>`"2d_graffiti_blockbuster"`<br>`"2d_graffiti_mural"`<br>`"2d_graffiti_stencil"`<br>`"2d_graffiti_3d"`<br>`"2d_graffiti_character"`<br>`"2d_graffiti_abstract"`<br>`"2d_graffiti_urban"`<br>`"2d_graffiti_neo_muralism"`<br>`"2d_graffiti_post_graffiti"`<br>`"2d_graffiti_street_art"` |
| `尺寸` | 生成影像的大小。（預設值："1024x1024"） | COMBO | 是 | `"1024x1024"`<br>`"1024x2048"`<br>`"2048x1024"`<br>`"2048x2048"`<br>`"512x512"`<br>`"512x1024"`<br>`"1024x512"`<br>`"2048x512"`<br>`"512x2048"` |
| `數量` | 要生成的影像數量。（預設值：1，最小值：1，最大值：6） | INT | 是 | 1-6 |
| `種子` | 決定節點是否應重新執行的種子；無論種子為何，實際結果都是非確定性的。（預設值：0，最小值：0，最大值：18446744073709551615） | INT | 是 | 0-18446744073709551615 |
| `負向提示詞` | 影像上不需要元素的可選文字描述。（預設值：""，為空時不使用負面提示詞） | STRING | 否 | - |
| `Recraft 控制` | 可選的額外生成控制項，透過 Recraft Controls 節點提供。 | CONTROLS | 否 | - |

**注意：** `seed` 參數僅控制節點重新執行的時機，並不會使生成結果具有確定性。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `SVG` | 以 SVG 格式生成的向量插圖 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aec7e96e339047e75dfe419d94d23a613595bc22e7f187895c52b143780fcbf3`
