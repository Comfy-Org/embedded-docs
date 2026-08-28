# SamplerCustomAdvanced

## 概述

SamplerCustomAdvanced 節點使用自訂雜訊、引導和取樣配置執行進階潛在空間取樣。它透過帶有可自訂雜訊生成和 sigma 排程的引導取樣過程來處理潛在影像，並在可用時產生最終的取樣輸出與去噪版本。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `雜訊` | 提供取樣過程初始雜訊模式和種子的雜訊生成器 | NOISE | 是 | - |
| `引導器` | 引導模型，將取樣過程導向所需的輸出 | GUIDER | 是 | - |
| `取樣器` | 定義生成期間潛在空間遍歷方式的取樣演算法 | SAMPLER | 是 | - |
| `Sigma 值` | 控制整個取樣步驟中雜訊等級的 sigma 排程 | SIGMAS | 是 | - |
| `latent 影像` | 作為取樣起點的初始潛在表示。支援可選的 `noise_mask` 以進行選擇性去噪，以及可選的 `downscale_ratio_spacial` 和 `downscale_ratio_temporal` 鍵以實現進階潛在處理 | LATENT | 是 | - |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `輸出` | 完成取樣過程後的最終取樣潛在表示。輸入潛在中的任何 `downscale_ratio_spacial` 或 `downscale_ratio_temporal` 鍵都會從此輸出中移除 | LATENT |
| `去雜訊輸出` | 當取樣過程產生中間乾淨預測（x0）時輸出的去噪版本，否則與 `output` 相同。可用時，此輸出代表模型在每個步驟中對乾淨潛在的最佳估計 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
