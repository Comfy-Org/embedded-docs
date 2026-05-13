> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/zh-TW.md)

## 概述

SD_4XUpscale_Conditioning 節點用於準備使用擴散模型進行影像放大時的條件資料。它接收輸入影像與條件資料，然後套用縮放與雜訊增強，建立修改後的條件資料，以引導放大過程。此節點會輸出正向與負向條件資料，以及對應放大尺寸的潛在表示。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | - | 要放大的輸入影像 |
| `positive` | CONDITIONING | 是 | - | 引導生成朝向期望內容的正向條件資料 |
| `negative` | CONDITIONING | 是 | - | 引導生成遠離不必要內容的負向條件資料 |
| `scale_ratio` | FLOAT | 否 | 0.0 - 10.0 | 套用於輸入影像的縮放倍率（預設值：4.0） |
| `noise_augmentation` | FLOAT | 否 | 0.0 - 1.0 | 在放大過程中添加的雜訊量（預設值：0.0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已套用放大資訊的修改後正向條件資料 |
| `negative` | CONDITIONING | 已套用放大資訊的修改後負向條件資料 |
| `latent` | LATENT | 對應放大尺寸的空潛在表示 |

---
**Source fingerprint (SHA-256):** `ede1ea8f5a95e7f9e52070b5132a4ed3e87f92230d14a74b9d713f547c74d785`
