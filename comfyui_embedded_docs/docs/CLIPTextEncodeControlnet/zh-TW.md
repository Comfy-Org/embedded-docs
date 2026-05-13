> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/zh-TW.md)

CLIPTextEncodeControlnet 節點使用 CLIP 模型處理文字輸入，並將其與現有的條件資料結合，為控制網路應用程式建立增強的條件輸出。它會將輸入文字進行分詞，透過 CLIP 模型進行編碼，並將產生的嵌入作為交叉注意力控制網路參數添加到提供的條件資料中。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 用於文字分詞和編碼的 CLIP 模型 |
| `conditioning` | CONDITIONING | 是 | - | 要透過控制網路參數增強的現有條件資料 |
| `text` | STRING | 是 | - | 由 CLIP 模型處理的文字輸入。支援多行文字和動態提示 |

**注意：** 此節點需要所有三個輸入（`clip`、`conditioning` 和 `text`）才能正常運作。`text` 輸入支援動態提示和多行文字，以實現靈活的文字處理。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 已增強的條件資料，其中包含從 CLIP 文字編碼衍生出的控制網路交叉注意力參數（`cross_attn_controlnet` 和 `pooled_output_controlnet`） |

---
**Source fingerprint (SHA-256):** `dd6f68d822cc38e27c826b634c938d62e07b075e18a0f46f80b462aecca0b70b`
