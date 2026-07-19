# TSR - 時間分數重新縮放

此節點對擴散模型應用時間分數重新縮放（Temporal Score Rescaling，TSR）。它透過在去噪過程中重新縮放預測的噪聲或分數來修改模型的採樣行為，從而可以引導生成輸出的多樣性。此功能是作為後 CFG（無分類器引導）函數實現的。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 將要套用 TSR 函數修補的擴散模型。 | MODEL | 是 | - |
| `tsr_k` | 控制重新縮放的強度。較低的 k 值會產生更詳細的結果；較高的 k 值在圖像生成中會產生更平滑的結果。設定 k = 1 會停用重新縮放。（預設值：0.95） | FLOAT | 否 | 0.01 - 100.0 |
| `tsr_sigma` | 控制重新縮放生效的時機。數值越大，生效時間越早。（預設值：1.0） | FLOAT | 否 | 0.01 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `修補後模型` | 輸入模型，現已套用時間分數重新縮放函數至其採樣過程。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2931b42ac93cf50e2c395bacf3128bb43dcc043ab5c8f86d7aabe4d35a44d20a`
