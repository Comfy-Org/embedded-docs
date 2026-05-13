> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/zh-TW.md)

# SamplerCustomAdvanced（自訂進階取樣器）節點

SamplerCustomAdvanced（自訂進階取樣器）節點使用自訂雜訊、引導和取樣配置來執行進階潛在空間取樣。它透過可自訂的雜訊生成和 sigma 排程，對潛在影像進行引導式取樣處理，最終產生取樣結果，並在可用時提供去噪版本。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `noise` | NOISE | 是 | - | 提供取樣過程初始雜訊模式和種子（seed）的雜訊生成器 |
| `guider` | GUIDER | 是 | - | 引導取樣過程朝向預期輸出結果的引導模型 |
| `sampler` | SAMPLER | 是 | - | 定義生成過程中潛在空間遍歷方式的取樣演算法 |
| `sigmas` | SIGMAS | 是 | - | 控制整個取樣步驟中雜訊程度的 sigma 排程 |
| `latent_image` | LATENT | 是 | - | 作為取樣起始點的初始潛在表示 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | LATENT | 完成取樣過程後的最終取樣潛在表示 |
| `denoised_output` | LATENT | 可用時的輸出去噪版本，否則回傳與輸出相同的結果 |

---
**Source fingerprint (SHA-256):** `bf711ecc0684ad04babe5c63a246195f358204d203e836587a90feff742929a3`
