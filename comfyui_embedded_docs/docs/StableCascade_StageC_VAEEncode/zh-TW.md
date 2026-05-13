> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/zh-TW.md)

## 概述

StableCascade_StageC_VAEEncode 節點透過 VAE 編碼器處理影像，為 Stable Cascade 模型生成潛在空間表示。它接收輸入影像，使用指定的 VAE 模型進行壓縮，然後輸出兩個潛在空間表示：一個用於階段 C，另一個作為階段 B 的佔位符。壓縮參數控制編碼前影像縮小的程度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要編碼到潛在空間的輸入影像 |
| `vae` | VAE | 是 | - | 用於編碼影像的 VAE 模型 |
| `compression` | INT | 否 | 4-128 | 編碼前應用於影像的壓縮因子（預設值：42） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `stage_c` | LATENT | Stable Cascade 模型階段 C 的編碼潛在空間表示 |
| `stage_b` | LATENT | 階段 B 的佔位符潛在空間表示（目前回傳零值） |

---
**Source fingerprint (SHA-256):** `e7b9bd83d263903567ab06c00324575e01b79b50881fa807cd6f006955935c63`
