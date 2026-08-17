# RenormCFG

RenormCFG 節點透過應用條件縮放與正規化，修改擴散模型中的分類器自由引導（CFG）過程。它根據指定的時間步長臨界值與重新正規化因子調整去噪過程，以控制在影像生成期間，條件預測與無條件預測之間的影響力。

## 輸入

| 參數 | 描述 | 資料類型 | 是否必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用重新正規化 CFG 的擴散模型 | MODEL | 是 | - |
| `cfg_trunc` | 套用 CFG 縮放的時間步長臨界值。當目前時間步長低於此值時，會套用 CFG 縮放；否則僅使用條件預測（預設值：100.0） | FLOAT | 否 | 0.0 - 100.0 |
| `renorm_cfg` | 重新正規化因子，限制經 CFG 縮放後的預測相對於原始條件預測的最大範數。值為 0.0 時停用重新正規化（預設值：1.0） | FLOAT | 否 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 套用重新正規化 CFG 函式後的修改模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
