此節點使用指定的噪聲生成器和 sigma 值，對潛在影像添加受控噪聲。它透過模型的取樣系統處理輸入，以應用適合給定 sigma 範圍的噪聲縮放，並返回已添加噪聲的新潛在表示。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 包含取樣參數和處理函數的模型 | MODEL | 是 | - |
| `noise` | 產生基礎噪聲模式的噪聲生成器 | NOISE | 是 | - |
| `sigmas` | 控制噪聲縮放強度的 Sigma 值。若為空，節點將返回未經修改的原始潛在影像。當提供多個 sigma 值時，噪聲縮放計算為第一個與最後一個 sigma 值之間的絕對差值。當僅提供一個 sigma 值時，該值將直接用作縮放值。 | SIGMAS | 是 | - |
| `latent 影像` | 將添加噪聲的輸入潛在表示。空的潛在影像（僅包含零值）在處理過程中不會被偏移。 | LATENT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 已添加噪聲的修改後潛在表示。輸出中的任何 NaN 或無限值都會被轉換為零以確保穩定性。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8f387f95aeec2780d27bee5b954ad2c6cd6daa9242a1ea15697455b157bc80d5`
