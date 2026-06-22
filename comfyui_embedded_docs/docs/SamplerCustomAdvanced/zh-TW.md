# SamplerCustomAdvanced

SamplerCustomAdvanced（自訂進階取樣器）節點使用自訂雜訊、引導和取樣配置來執行進階潛在空間取樣。它透過可自訂的雜訊生成和 sigma 排程，對潛在影像進行引導式取樣處理，最終產生取樣結果，並在可用時提供去噪版本。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `雜訊` | 提供取樣過程初始雜訊模式和種子（seed）的雜訊生成器 | NOISE | 是 | - |
| `引導器` | 引導取樣過程朝向預期輸出結果的引導模型 | GUIDER | 是 | - |
| `取樣器` | 定義生成過程中潛在空間遍歷方式的取樣演算法 | SAMPLER | 是 | - |
| `Sigma 值` | 控制整個取樣步驟中雜訊程度的 sigma 排程 | SIGMAS | 是 | - |
| `latent 影像` | 作為取樣起始點的初始潛在表示 | LATENT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `去雜訊輸出` | 完成取樣過程後的最終取樣潛在表示 | LATENT |
| `denoised_output` | 可用時的輸出去噪版本，否則回傳與輸出相同的結果 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bf711ecc0684ad04babe5c63a246195f358204d203e836587a90feff742929a3`
