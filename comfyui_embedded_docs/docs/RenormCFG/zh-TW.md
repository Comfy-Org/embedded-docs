# RenormCFG

RenormCFG 節點透過應用條件縮放和正規化，修改擴散模型中的無分類器引導（CFG）過程。它根據指定的時間步長閾值和重新正規化因子調整去噪過程，以控制在影像生成過程中條件預測與無條件預測的影響力。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要應用重新正規化 CFG 的擴散模型 | MODEL | 是 | - |
| `cfg_trunc` | 應用 CFG 縮放的時間步長閾值。當目前時間步長低於此值時，會應用 CFG 縮放；否則僅使用條件預測（預設值：100.0） | FLOAT | 否 | 0.0 - 100.0 |
| `renorm_cfg` | 重新正規化因子，限制 CFG 縮放預測相對於原始條件預測的最大範數。值為 0.0 時停用重新正規化（預設值：1.0） | FLOAT | 否 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已應用重新正規化 CFG 功能的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b59929606f7519574b7ad14a3caacee51e4f141dd6be3abb594217bcfdbc401e`
