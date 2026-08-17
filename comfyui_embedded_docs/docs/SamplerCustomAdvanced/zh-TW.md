# SamplerCustomAdvanced

SamplerCustomAdvanced 節點使用自訂噪聲、引導和取樣配置執行進階潛在空間取樣。它透過引導式取樣過程處理潛在影像，並提供可自訂的噪聲生成與 sigma 排程，最終產生取樣結果，並在可用情況下輸出降噪版本。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `noise` | 提供取樣過程初始噪聲模式和種子的噪聲生成器 | NOISE | 是 | - |
| `guider` | 引導取樣過程朝向預期輸出方向的引導模型 | GUIDER | 是 | - |
| `sampler` | 定義生成期間潛在空間遍歷方式的取樣演算法 | SAMPLER | 是 | - |
| `sigmas` | 控制取樣步驟中噪聲等級的 sigma 排程 | SIGMAS | 是 | - |
| `latent_image` | 作為取樣起點的初始潛在表徵。支援選用的 `noise_mask` 以進行選擇性降噪，以及選用的 `downscale_ratio_spacial` 和 `downscale_ratio_temporal` 鍵以進行進階潛在處理 | LATENT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 完成取樣過程後最終取樣的潛在表徵。輸入潛在中的任何 `downscale_ratio_spacial` 或 `downscale_ratio_temporal` 鍵都會從此輸出中移除 | LATENT |
| `denoised_output` | 當取樣過程產生中間乾淨預測（x0）時，輸出的降噪版本；否則與輸出相同。在可用情況下，此輸出代表模型在每個步驟中對乾淨潛在的最佳估計 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
