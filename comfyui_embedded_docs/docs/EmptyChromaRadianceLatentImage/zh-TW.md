> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/zh-TW.md)

## 概述

EmptyChromaRadianceLatentImage 節點會建立一個指定尺寸的空白潛在影像，用於色度輻射工作流程。它會產生一個填充為零的張量，作為潛在空間操作的起點。此節點允許您定義空白潛在影像的寬度、高度和批次大小。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 潛在影像的寬度（像素為單位，預設值：1024，必須能被 16 整除） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 潛在影像的高度（像素為單位，預設值：1024，必須能被 16 整除） |
| `batch_size` | INT | 否 | 1 至 4096 | 單一批次中要產生的潛在影像數量（預設值：1） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `samples` | LATENT | 產生的空白潛在影像張量，具有指定的尺寸 |

---
**Source fingerprint (SHA-256):** `f2bc90a236f91e0161142f5242647d15adc8a10c57c920d2eb97e87040ac99d4`
