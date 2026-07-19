# 空白 Qwen 圖像分層 Latent

## 概述

Empty Qwen Image Layered Latent 節點會建立一個空白的多層潛在表示，用於 Qwen 影像模型。它會產生一個填充為零的張量，結構中包含指定的層數、批次大小和空間維度。這個空的潛在表示可作為後續影像生成或處理工作流程的起點。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 要建立的潛在影像寬度。此值必須能被 16 整除。（預設值：640） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 要建立的潛在影像高度。此值必須能被 16 整除。（預設值：640） | INT | 是 | 16 至 MAX_RESOLUTION |
| `圖層數` | 要添加到潛在結構中的額外層數。這定義了潛在表示的深度。（預設值：3） | INT | 是 | 0 至 MAX_RESOLUTION |
| `批次大小` | 批次中要生成的潛在樣本數量。（預設值：1） | INT | 否 | 1 至 4096 |

**注意：** `width` 和 `height` 參數在內部會除以 8，以決定輸出潛在張量的空間維度。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 一個填充為零的潛在張量。其形狀為 `[batch_size, 16, layers + 1, height // 8, width // 8]`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `99497e3e4a67bf7b3f650573e7b8eb2d7fad6be5819b7ebbbb8736291dc44e0c`
