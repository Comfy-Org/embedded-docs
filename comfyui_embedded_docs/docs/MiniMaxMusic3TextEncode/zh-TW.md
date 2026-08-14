# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode 使用 MiniMax Music3 CLIP 模型，將文字描述和歌詞轉換成用於產生音樂的聲學條件序列。此節點會傳回轉換後的 CONDITIONING 資料，以及根據輸入時長計算出的實際音訊秒數。

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip` | MiniMax Music3 CLIP 模型，用於文字編碼和條件序列生成。 | CLIP | 是 | - |
| `caption` | 描述要產生音樂的文字內容。支援多行文字和動態提示。 | STRING | 是 | - |
| `lyrics` | 要用於產生音樂的歌詞文字。支援多行文字和動態提示。 | STRING | 是 | - |
| `seed` | 用於生成過程的可重現隨機種子。預設值：0。 | INT | 是 | 0 到 18446744073709551615（0xffffffffffffffff） |
| `max_duration` | 產生音樂的最大時長（秒），模型可能提前結束歌曲。預設值：120.0。 | FLOAT | 是 | 0.04 到模型最大音訊時長（MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND），步長 0.04 |
| `cfg_scale` | 分類器自由引導縮放係數。預設值：模型常數 CFG_SCALE。進階參數。 | FLOAT | 是 | 0.0 到 100.0，步長 0.1（保留 2 位小數） |
| `top_k` | 用於聲學 token 選擇的 top-k 取樣值。預設值：模型常數 CFG_TOP_K。進階參數。 | INT | 是 | 1 到模型詞彙表大小（C0_VOCAB_SIZE） |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `conditioning` | 生成的聲學條件序列，用於指導後續音樂生成。 | CONDITIONING |
| `seconds` | 條件序列對應的實際時長，以秒為單位。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
