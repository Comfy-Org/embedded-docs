# PhotoMaker 編碼

PhotoMakerEncode 透過結合參考圖像與文字提示，為 AI 影像生成建立條件資料。它會在文字提示中搜尋「photomaker」這個詞，若找到，便使用 PhotoMaker 模型將參考圖像的視覺特徵套用於提示中的該位置。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `photomaker` | 用於處理參考圖像並產生基於影像的嵌入（embeddings）的 PhotoMaker 模型 | PHOTOMAKER | 是 | - |
| `image` | 提供視覺特徵以進行條件處理的參考圖像 | IMAGE | 是 | - |
| `clip` | 用於文字分詞與編碼的 CLIP 模型 | CLIP | 是 | - |
| `text` | 用於條件生成的文字提示。支援多行與動態提示（預設值："photograph of photomaker"） | STRING | 是 | - |

**注意：** 文字提示中必須將「photomaker」作為獨立單詞出現（比對區分大小寫），才會套用基於影像的條件處理。當存在時，影像的特徵會在提示中的該位置被注入。如果找不到「photomaker」，此節點會回傳標準的文字條件處理，而不受影像影響。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含用於引導影像生成的影像與文字嵌入的條件資料，以及來自 CLIP 文字編碼器的池化輸出 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
