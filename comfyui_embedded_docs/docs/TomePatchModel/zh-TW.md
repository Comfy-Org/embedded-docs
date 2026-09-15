# Tome 修補模型

TomePatchModel 會將 Token Merging（ToMe）套用至擴散模型，以降低推論期間的運算成本。其運作方式是合併模型注意力機制內相似的 token，因此模型只需處理較少的 token，同時大致維持輸出品質。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 token 合併的擴散模型 | MODEL | 是 | - |
| `比例` | 要合併的 token 比例（預設：0.3）。數值越高會合併越多 token，可帶來更大幅度的加速，但可能降低品質。 | FLOAT | 是 | 0.0 - 1.0 |

注意：如果注意力區塊中的 token 數量少到不需要進行降採樣，合併函式會被替換為無操作（no-op），該區塊的模型執行維持不變。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 token 合併的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
