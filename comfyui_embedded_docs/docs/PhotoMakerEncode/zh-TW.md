> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/zh-TW.md)

PhotoMakerEncode 節點處理影像與文字，以生成用於 AI 影像生成的條件數據。它接收一張參考影像與文字提示，然後建立嵌入向量，這些嵌入向量可根據參考影像的視覺特徵來引導影像生成。此節點會特別在文字中尋找「photomaker」標記，以決定在何處套用基於影像的條件設定。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `photomaker` | PHOTOMAKER | 是 | - | 用於處理影像並生成嵌入向量的 PhotoMaker 模型 |
| `image` | IMAGE | 是 | - | 提供視覺特徵以進行條件設定的參考影像 |
| `clip` | CLIP | 是 | - | 用於文字分詞與編碼的 CLIP 模型 |
| `text` | STRING | 是 | - | 用於條件生成的文字提示（預設值："photograph of photomaker"） |

**注意：** 當文字中包含「photomaker」一詞時，節點會在提示詞中的該位置套用基於影像的條件設定。若文字中未找到「photomaker」，則節點會生成不含影像影響的標準文字條件設定。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含影像與文字嵌入向量的條件數據，用於引導影像生成 |

---
**Source fingerprint (SHA-256):** `535fd3dbbe0e48205bebde030138ffca841dc94a18fd47db768a1066fe84bce4`
