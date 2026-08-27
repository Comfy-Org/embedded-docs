# 最佳步數排程器

OptimalStepsScheduler 節點會建立一個噪聲調度（一系列 sigma 值），用於擴散採樣過程。它會根據所選的模型類型選擇基礎噪聲級別，在部分套用去噪時調整調度，並對級別進行內插，使傳回的 sigma 值符合要求的步數。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_type` | 用於噪聲級別計算的擴散模型類型。 | COMBO | 是 | "FLUX"<br>"Wan"<br>"Chroma" |
| `步驟數` | 要計算的總採樣步數（預設：20）。 | INT | 是 | 3 至 1000 |
| `去雜訊強度` | 控制去噪強度，用於調整有效步數（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步長：0.01） |

**注意：** 當 `denoise` 小於 1.0 時，節點使用 `round(steps * denoise)` 作為有效步數的總數。如果 `denoise` 為 0.0，節點將傳回空張量。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 一系列 sigma 值，代表擴散採樣過程中的噪聲調度。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
