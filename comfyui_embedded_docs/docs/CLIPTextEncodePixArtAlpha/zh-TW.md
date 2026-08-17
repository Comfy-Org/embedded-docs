# CLIPTextEncodePixArtAlpha

此節點對 PixArt Alpha 模型進行文字編碼，並設定解析度條件化。此節點處理文字輸入，並加入寬度與高度資訊，以建立專門用於 PixArt Alpha 模型的條件化資料。此節點不適用於 PixArt Sigma 模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 解析度條件化的寬度維度（預設值為 1024） | INT | 是 | 0 to MAX_RESOLUTION |
| `height` | 解析度條件化的高度維度（預設值為 1024） | INT | 是 | 0 to MAX_RESOLUTION |
| `text` | 要編碼的文字輸入，支援多行輸入與動態提示詞 | STRING | 是 | - |
| `clip` | 用於分詞與編碼的 CLIP 模型 | CLIP | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含文字 token 與解析度資訊的編碼條件化資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`
