> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/zh-TW.md)

## 概述

SamplerLCMUpscale 節點提供了一種專門的取樣方法，結合了潛在一致性模型（LCM）取樣與影像放大功能。它讓您能夠在取樣過程中，使用各種插值方法來放大影像，非常適合在維持影像品質的同時，生成更高解析度的輸出結果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `縮放比例` | FLOAT | 否 | 0.1 - 20.0 | 放大過程中應用的縮放比例（預設值：1.0） |
| `縮放步驟` | INT | 否 | -1 - 1000 | 用於放大過程的步驟數。設為 -1 則自動計算（預設值：-1） |
| `放大方法` | COMBO | 是 | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" | 用於放大影像的插值方法 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 返回一個已配置的取樣器物件，可用於取樣流程中 |

---
**Source fingerprint (SHA-256):** `fe0d4c8676454a9e8ecf4bb4e149c9b5e22083322447749116d624984d75e73c`
