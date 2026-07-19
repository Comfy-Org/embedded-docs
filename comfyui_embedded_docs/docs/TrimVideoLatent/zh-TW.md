# 裁剪影片潛在空間

## 概述

TrimVideoLatent 節點會從影片潛在表示（latent representation）的開頭移除影格。它接收一個潛在影片樣本，並從起始處修剪掉指定數量的影格，然後傳回影片的其餘部分。這讓您可以透過移除開頭的影格來縮短影片序列。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 包含待修剪影格的輸入潛在影片表示 | LATENT | 是 | - |
| `裁剪量` | 要從影片開頭移除的影格數量（預設值：0） | INT | 是 | 0 至 99999 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 已從開頭移除指定數量影格的修剪後潛在影片表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7fd482533d1f63219565a3a25776173c77c419fbf5086015d42136f5bfdfbed2`
