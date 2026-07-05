# 切向阻尼 CFG

TCFG（切向阻尼 CFG）在取樣過程中優化無條件（負面）預測，使其更符合條件（正面）預測。此技術基於研究論文 2503.18137，透過對無條件引導應用切向阻尼來提升輸出品質。該節點透過調整無分類器引導期間無條件預測的處理方式，來修改模型的取樣行為。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用切向阻尼 CFG 的模型 | MODEL | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `修補後模型` | 已套用切向阻尼 CFG 的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/zh-TW.md)

---
**Source fingerprint (SHA-256):** `de6b4deb8a42f05dff90e393bff1e0b4b8ed58887586ca81c236e1a780be5776`
