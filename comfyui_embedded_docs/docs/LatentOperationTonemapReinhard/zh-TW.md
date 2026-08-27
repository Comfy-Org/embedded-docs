# 潛空間 Reinhard 色調映射

LatentOperationTonemapReinhard 節點將 Reinhard 色調映射應用於潛在向量。此技術基於平均值和標準差的統計方法來正規化潛在向量並調整其幅度，強度由 `multiplier` 參數控制。此節點目前標記為實驗性。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `乘數` | 控制色調映射效果的強度（預設值：1.0） | FLOAT | 是 | 0.0 至 100.0 (step 0.01) |

## 輸出

| 輸出名 | 描述 | 資料型別 |
| --- | --- | --- |
| `operation` | 傳回可應用於潛在向量的色調映射操作 | LATENT_OPERATION |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
