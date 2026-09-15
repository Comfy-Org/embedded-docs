# CFG 正規化

CFGNorm 透過比較條件預測與引導預測的大小（範數），並重新縮放結果，來調整無分類器引導（classifier-free guidance，CFG）在擴散模型中的套用方式。`strength` 值控制套用多少調整量。預設情況下，縮放只會衰減引導輸出；啟用 `pre_cfg` 時，會在取樣器的 CFG 合併之前重新縮放合併後的雜訊，且不進行鉗位，這可能會放大結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用 CFG 正規化的擴散模型 | MODEL | 是 | - |
| `強度` | 控制套用於 CFG 縮放的正規化效果強度（預設：1.0） | FLOAT | 是 | 0.0 至 100.0 （步進值：0.01） |
| `pre_cfg` | 若為 true，則在取樣器的 CFG 合併之前重新縮放合併後的雜訊，且不進行鉗位（可能放大）。這與 Lens 等模型使用的範數縮放 CFG 相符。預設 false 會保留原本 CFG 之後 x0 空間的僅衰減行為。（預設：False） | BOOLEAN | 否 | true / false |

備註：此節點標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `patched_model` | 傳回已修改的模型，其取樣流程已套用 CFG 正規化 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/zh-TW.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
