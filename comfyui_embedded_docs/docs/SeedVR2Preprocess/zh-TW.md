# SeedVR2Preprocess

此節點會對調整大小後的影像進行填充，以準備供 SeedVR2 模型使用。在處理過程中會移除 Alpha 通道，後續由配套的「後處理 SeedVR2 輸出」節點使用原始調整大小後的影像來還原。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | 要處理的調整大小後影像。 | IMAGE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 已填充並準備好供 SeedVR2 處理的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b8135d0e27f75a673f52d080c6704de8cc86d15b5d16eca055d55e2d20837dc7`
