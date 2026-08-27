# RenormCFG

RenormCFG 節點透過套用條件縮放與正規化，修改擴散模型中的無分類器引導 (CFG) 流程。它會根據指定的時間步門檻與重新正規化因子調整去噪過程，以控制影像生成期間條件預測與非條件預測的影響。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用重新正規化 CFG 的擴散模型 | MODEL | 是 | - |
| `cfg_trunc` | 套用 CFG 縮放的時間步門檻。當目前時間步低於此值時，會套用 CFG 縮放；否則僅使用條件預測（預設值：100.0） | FLOAT | 否 | 0.0 - 100.0 |
| `renorm_cfg` | 重新正規化因子，用於限制 CFG 縮放預測相對於原始條件預測的最大範數。值為 0.0 時停用重新正規化（預設值：1.0） | FLOAT | 否 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 套用重新正規化 CFG 函式後的修改模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
