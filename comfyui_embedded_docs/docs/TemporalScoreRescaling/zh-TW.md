# TSR - 時間分數重新縮放

此節點對擴散模型套用時間分數重新縮放（Temporal Score Rescaling, TSR）。它透過在去噪過程中重新縮放預測的雜訊或分數來修改模型的取樣行為，從而可以控制生成輸出的多樣性。此功能作為 CFG（分類器自由引導）後函數實現。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 TSR 函數的擴散模型。 | MODEL | 是 | - |
| `tsr_k` | 控制重新縮放的強度。較低的 k 值在圖像生成中產生更詳細的結果；較高的 k 值產生更平滑的結果。設定 k = 1 可停用重新縮放。（預設值：0.95） | FLOAT | 否 | 0.01 - 100.0 |
| `tsr_sigma` | 控制重新縮放生效的時機。數值越大越早生效。（預設值：1.0） | FLOAT | 否 | 0.01 - 100.0 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `patched_model` | 輸入模型，現在已套用時間分數重新縮放函數至其取樣過程。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
