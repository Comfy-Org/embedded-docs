# 新增雜訊

此節點使用指定的雜訊產生器和 sigma 值，為潛在影像（latent image）加入受控制的雜訊。它會透過模型的取樣系統處理輸入，以套用符合指定 sigma 範圍的雜訊縮放，並回傳已套用雜訊的新潛在表示。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 包含取樣參數和處理函式的模型。 | MODEL | 是 | - |
| `noise` | 產生基礎雜訊模式的雜訊產生器。 | NOISE | 是 | - |
| `sigmas` | 控制雜訊縮放強度的 sigma 值。若為空，節點會回傳未變更的原始潛在影像。當提供多個 sigma 值時，雜訊縮放比例會計算為第一個和最後一個 sigma 值之間的絕對差。當僅提供一個 sigma 值時，該值直接作為縮放比例。 | SIGMAS | 是 | - |
| `latent_image` | 將加入雜訊的輸入潛在表示。空的潛在影像（僅包含零）在處理過程中不會被偏移。 | LATENT | 是 | - |

## 輸出

| 輸出名 | 描述 | 資料型別 |
| --- | --- | --- |
| `LATENT` | 加入雜訊後修改過的潛在表示。輸出中的任何 NaN 或無限值都會轉換為零以保持穩定性。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`
