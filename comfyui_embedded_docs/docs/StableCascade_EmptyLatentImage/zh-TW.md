# StableCascade 空白潛在影像

## 概述

StableCascade_EmptyLatentImage 節點會為 Stable Cascade 模型建立空的潛在張量。它會根據輸入解析度與壓縮設定，生成兩個獨立的潛在表示——一個用於階段 C，另一個用於階段 B。此節點為 Stable Cascade 生成管線提供了起點。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 輸出影像的寬度（像素）（預設值：1024，步進：8） | INT | 是 | 256 至 MAX_RESOLUTION |
| `高度` | 輸出影像的高度（像素）（預設值：1024，步進：8） | INT | 是 | 256 至 MAX_RESOLUTION |
| `壓縮` | 決定階段 C 潛在維度的壓縮因子（預設值：42，步進：1） | INT | 是 | 4 至 128 |
| `批次大小` | 批次中要生成的潛在樣本數量（預設值：1） | INT | 否 | 1 至 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `stage_b` | 階段 C 的潛在張量，維度為 [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | 階段 B 的潛在張量，維度為 [batch_size, 4, height//4, width//4] | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ba5347f522b661993e540bc5775737cae88bd5f7a87c1b91715f8c1858e8e81a`
