# 潛空間 Reinhard 色調映射

此節點會建立一個 latent 操作，對潛在向量套用 Reinhard 色調映射。它會正規化每個潛在向量，測量整體量值分佈（平均值與標準差），然後使用 Reinhard 曲線壓縮極端量值，整體強度由 `multiplier` 控制。此節點標記為實驗性（也可用「hdr latent」搜尋）。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 範圍 |
| --- | --- | --- | --- | --- |
| `乘數` | 控制色調映射效果的強度（預設：1.0） | FLOAT | 是 | 0.0 至 100.0 （步進值：0.01） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `operation` | 傳回可套用至潛在向量的色調映射操作 | LATENT_OPERATION |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
