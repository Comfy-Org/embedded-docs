# EmptyTrellis2LatentStructure

此節點為 Trellis2 模型建立一個空的潛在結構，其中所有值皆設為零。它會產生一個具有 32 個通道、解析度為 16×16×16 的空白 3D 潛在張量，其大小適用於批次中指定的項目數量。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `batch_size` | 批次中的潛在影像數量（預設值：1）。 | INT | 是 | 1 到 4096 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `LATENT` | 空的 Trellis2 潛在結構。樣本是一個以零填充的張量，形狀為 (batch_size, 32, 16, 16, 16)，潛在類型設定為 "trellis2"。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
