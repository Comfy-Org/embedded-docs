> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/zh-TW.md)

為 PixArt Alpha 編碼文字並設定解析度條件。此節點處理文字輸入，並加入寬度與高度資訊，以建立專門用於 PixArt Alpha 模型的條件資料。不適用於 PixArt Sigma 模型。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | 0 至 MAX_RESOLUTION | 解析度條件的寬度尺寸（預設值：1024） |
| `height` | INT | 是 | 0 至 MAX_RESOLUTION | 解析度條件的高度尺寸（預設值：1024） |
| `text` | STRING | 是 | - | 要編碼的文字輸入，支援多行輸入與動態提示詞 |
| `clip` | CLIP | 是 | - | 用於分詞與編碼的 CLIP 模型 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含文字標記與解析度資訊的編碼條件資料 |

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`
