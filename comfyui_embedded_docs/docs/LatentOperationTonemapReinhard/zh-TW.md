# 潛空間 Reinhard 色調映射

LatentOperationTonemapReinhard 將 Reinhard 色調映射應用於潛在向量。此技術基於幅度的平均值和標準差，使用統計方法正規化潛在向量並調整其幅度，強度由乘數參數控制。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `multiplier` | 控制色調映射效果的強度（預設值：1.0） | FLOAT | 是 | 0.0 至 100.0 |

## 输出

| 輸出名稱 | 描述 | 数据类型 |
| --- | --- | --- |
| `operation` | 返回可應用於潛在向量的色調映射操作 | LATENT_OPERATION |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
