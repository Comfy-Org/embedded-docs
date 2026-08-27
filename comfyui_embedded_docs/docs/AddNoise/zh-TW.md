# 新增雜訊

此節點使用指定的噪聲生成器和 sigma 值，向潛在圖像添加受控噪聲。它透過模型的採樣系統處理輸入，以套用適合給定 sigma 範圍的噪聲縮放，並傳回已套用噪聲的新潛在表示。此節點目前標記為實驗性。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 包含採樣參數和處理函數的模型 | MODEL | 是 | - |
| `noise` | 產生基礎噪聲圖案的噪聲生成器 | NOISE | 是 | - |
| `sigmas` | 控制噪聲縮放強度的 sigma 值。若為空白，節點會傳回未更改的原始潛在圖像。當提供多個 sigma 值時，噪聲縮放會計算為第一個與最後一個 sigma 值之間的絕對差。當僅提供一個 sigma 值時，該值會直接用作縮放值。 | SIGMAS | 是 | - |
| `latent 影像` | 要加入噪聲的輸入潛在表示。空的潛在圖像（僅包含零）在處理期間不會被移位。 | LATENT | 是 | - |

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 已加入噪聲的修改後潛在表示。輸出中的任何 NaN 或無限值都會轉換為零以保持穩定性。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`
