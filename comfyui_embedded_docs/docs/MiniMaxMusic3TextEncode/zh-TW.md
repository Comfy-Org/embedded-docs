# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode 使用 MiniMax Music3 CLIP 模型將文字標題和歌詞轉換為用於音樂生成的聲學條件序列。此節點會回傳產生的 CONDITIONING 資料，以及根據輸入的最大時長計算出的實際音訊秒數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於文字編碼和條件序列生成的 MiniMax Music3 CLIP 模型。 | CLIP | 是 | - |
| `caption` | 描述要生成之音樂的文字。支援多行文字與動態提示詞。 | STRING | 是 | - |
| `歌詞` | 用於生成音樂的歌詞文字。支援多行文字與動態提示詞。 | STRING | 是 | - |
| `種子` | 用於生成過程的可重現隨機種子。預設值：0。 | INT | 是 | 0 至 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | 最大時長（秒）；模型可以提前結束歌曲。預設值：120.0。 | FLOAT | 是 | 0.04 to the model's maximum audio duration (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04 |
| `cfg_scale` | 無分類器引導尺度。預設值：模型常數 CFG_SCALE。進階參數。 | FLOAT | 是 | 0.0 至 100.0, step 0.1 (keeps 2 decimal places) |
| `top_k` | 用於聲學 token 選擇的 Top-k 取樣值。預設值：模型常數 CFG_TOP_K。進階參數。 | INT | 是 | 1 to the model's vocabulary size (C0_VOCAB_SIZE) |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `conditioning` | 生成的聲學條件序列，用於引導後續的音樂生成。 | CONDITIONING |
| `秒` | 條件序列的實際持續時間（秒）。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
