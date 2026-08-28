# TSR - 時間分數重新縮放

此節點對擴散模型套用時間分數重新縮放（Temporal Score Rescaling, TSR）。它會透過在去噪過程中重新縮放預測的雜訊或分數來修改模型的採樣行為，進而引導生成輸出的多樣性。此功能以 post-CFG（無分類器引導）函數的形式實作。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用 TSR 函數修補的擴散模型。 | MODEL | 是 | - |
| `tsr_k` | 控制重新縮放的強度。k 值較低會在影像生成中產生更多細節；k 值較高則會產生更平滑的結果。設定 k = 1 會停用重新縮放。（預設值：0.95） | FLOAT | 是 | 0.01 - 100.0 |
| `tsr_sigma` | 控制重新縮放生效的時機。數值越大，越早生效。（預設值：1.0） | FLOAT | 是 | 0.01 - 100.0 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `修補後模型` | 輸入模型，現已在其採樣過程中套用時間分數重新縮放函數進行修補。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
