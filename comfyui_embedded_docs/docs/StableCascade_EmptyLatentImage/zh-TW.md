> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/zh-TW.md)

## 概述

StableCascade_EmptyLatentImage 節點會為 Stable Cascade 模型建立空的潛在張量。它會根據輸入解析度與壓縮設定，生成兩個獨立的潛在表示——一個用於階段 C，另一個用於階段 B。此節點為 Stable Cascade 生成管線提供了起點。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | 256 至 MAX_RESOLUTION | 輸出影像的寬度（像素）（預設值：1024，步進：8） |
| `height` | INT | 是 | 256 至 MAX_RESOLUTION | 輸出影像的高度（像素）（預設值：1024，步進：8） |
| `compression` | INT | 是 | 4 至 128 | 決定階段 C 潛在維度的壓縮因子（預設值：42，步進：1） |
| `batch_size` | INT | 否 | 1 至 4096 | 批次中要生成的潛在樣本數量（預設值：1） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `stage_c` | LATENT | 階段 C 的潛在張量，維度為 [batch_size, 16, height//compression, width//compression] |
| `stage_b` | LATENT | 階段 B 的潛在張量，維度為 [batch_size, 4, height//4, width//4] |

---
**Source fingerprint (SHA-256):** `ba5347f522b661993e540bc5775737cae88bd5f7a87c1b91715f8c1858e8e81a`
