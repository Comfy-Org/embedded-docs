> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/zh-TW.md)

## 概述

FreeU 節點對模型的輸出區塊應用頻域修改，以提升影像生成品質。其運作方式是透過縮放不同的通道群組，並對特定特徵圖進行傅立葉濾波，從而在生成過程中實現對模型行為的精細控制。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用 FreeU 修改的模型 |
| `b1` | FLOAT | 是 | 0.0 - 10.0 | 用於 `model_channels` × 4 特徵的主幹縮放因子（預設值：1.1） |
| `b2` | FLOAT | 是 | 0.0 - 10.0 | 用於 `model_channels` × 2 特徵的主幹縮放因子（預設值：1.2） |
| `s1` | FLOAT | 是 | 0.0 - 10.0 | 用於 `model_channels` × 4 特徵的跳躍連接縮放因子（預設值：0.9） |
| `s2` | FLOAT | 是 | 0.0 - 10.0 | 用於 `model_channels` × 2 特徵的跳躍連接縮放因子（預設值：0.2） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用 FreeU 修補程式的修改後模型 |

---
**Source fingerprint (SHA-256):** `449a02a4bb5b42eb37fab394bcdc6375e08e369961d633618211ebc5f737ab51`
