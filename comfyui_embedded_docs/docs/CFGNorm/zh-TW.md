# CFG 正規化

CFGNorm 將歸一化技術應用於擴散模型中的無分類器引導（CFG）過程。它透過比較條件輸出與無條件輸出的範數來調整去噪預測的尺度，然後套用強度乘數來控制效果。這有助於透過防止引導縮放中的極端值來穩定生成過程。當啟用 `pre_cfg` 時，重新縮放改為在取樣器的 CFG 組合之前套用於組合雜訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 CFG 歸一化的擴散模型 | MODEL | 是 | - |
| `strength` | 控制套用於 CFG 縮放的歸一化效果強度（預設值：1.0） | FLOAT | 是 | 0.0 to 100.0 (step 0.01) |
| `pre_cfg` | 如果為 true，則在取樣器的 CFG 組合之前重新縮放組合雜訊，且不進行限制（可能放大）。這與 Lens 等模型所使用的範數縮放 CFG 相符。預設為 false 時，保持原始的 CFG 後 x0 空間僅衰減行為。（預設值：False） | BOOLEAN | 否 | True<br>False |

注意：在預設的 CFG 後模式下，重新縮放因子會被限制在 0.0 到 1.0 之間，因此只能衰減（縮小）預測尺度。當啟用 `pre_cfg` 時，不會套用限制，因此組合雜訊可以被放大。在該模式下，`strength` 值不等於 1.0 時，會將結果混合回標準線性 CFG。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `patched_model` | 傳回已修改的模型，其取樣過程已套用 CFG 歸一化 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/zh-TW.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
