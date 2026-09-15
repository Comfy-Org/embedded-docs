# SamplerCustomAdvanced

SamplerCustomAdvanced 節點使用自訂雜訊、引導與取樣設定，執行進階的潛在空間取樣。它會透過引導取樣流程，搭配可自訂的雜訊產生器與 sigma 排程來處理潛在影像，並產生最終取樣輸出，以及在可用時產生去雜訊版本。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `雜訊` | 提供取樣流程初始雜訊圖樣與種子的雜訊產生器 | NOISE | 是 | - |
| `引導器` | 引導模型，引導取樣流程朝向期望輸出 | GUIDER | 是 | - |
| `取樣器` | 取樣演算法，定義生成期間如何遍歷潛在空間 | SAMPLER | 是 | - |
| `Sigma 值` | sigma 排程，控制取樣步驟中的雜訊等級 | SIGMAS | 是 | - |
| `latent 影像` | 初始潛在表示，作為取樣的起點。支援選用的 `noise_mask` 鍵，用於選擇性去雜訊，以及選用的 `downscale_ratio_spacial` 和 `downscale_ratio_temporal` 鍵，用於進階潛在處理 | LATENT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 完成取樣流程後最終取樣出的潛在表示。輸入潛在中的任何 `downscale_ratio_spacial` 或 `downscale_ratio_temporal` 鍵都會從此輸出中移除 | LATENT |
| `denoised_output` | 當取樣流程產生中間乾淨預測 (x0) 時，輸出的去雜訊版本；否則回傳與 `output` 相同。當可用時，這代表模型對乾淨潛在的最佳估計 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
