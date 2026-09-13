# TSR - 時間分數重新縮放

此節點會對擴散模型套用時間分數重縮放（Temporal Score Rescaling，TSR）。它會修補模型，使得在取樣期間，預測的分數或雜訊會被重新縮放，以引導生成結果的多樣性。此功能是以 CFG（Classifier-Free Guidance，無分類器引導）後處理函式的方式實作。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用 TSR 函式修補的擴散模型。 | MODEL | 是 | - |
| `tsr_k` | 控制重縮放的強度。較低的 k 會產生更精細的結果；較高的 k 則會在影像生成中產生更平滑的結果。設定 k = 1 會停用重縮放。（預設值：0.95） | FLOAT | 是 | 0.01 - 100.0 |
| `tsr_sigma` | 控制重縮放多早開始生效。數值越大，生效時間越早。（預設值：1.0） | FLOAT | 是 | 0.01 - 100.0 |

注意：當 `tsr_k` 設為 1、sigma 值為 0，或訊噪比為 0 時，會略過重縮放。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `patched_model` | 輸入模型，現已套用 Temporal Score Rescaling 函式修補至其取樣流程。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
