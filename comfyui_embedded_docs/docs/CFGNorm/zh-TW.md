# CFG 正規化

CFGNorm 在擴散模型中對分類器自由引導（CFG）過程應用歸一化技術。它透過比較條件輸出和無條件輸出的範數來調整去噪預測的尺度，然後應用強度乘數來控制效果。預設情況下，歸一化僅衰減引導輸出，但啟用 `pre_cfg` 會在取樣器的 CFG 合併之前重新縮放組合雜訊，且不進行截斷，這可能會放大數值。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用 CFG 歸一化的擴散模型 | MODEL | 是 | - |
| `強度` | 控制套用於 CFG 縮放的歸一化效果強度（預設值：1.0） | FLOAT | 是 | 0.0 至 100.0 |
| `pre_cfg` | 若為 true，在取樣器的 CFG 合併之前重新縮放組合雜訊，且不進行截斷（可放大）。與 Lens 等模型使用的範數縮放 CFG 相符。預設為 false 時保留原始的 CFG 後 x0 空間僅衰減行為。（預設值：False） | BOOLEAN | 否 | true / false |

注意：此節點被標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `修補模型` | 傳回已套用 CFG 歸一化至其取樣程序的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/zh-TW.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
