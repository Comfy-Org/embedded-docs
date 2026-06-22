# CFGZeroStar

CFGZeroStar 節點對擴散模型應用了一種專門的引導縮放技術。它透過計算基於條件預測與無條件預測之間差異的最佳化縮放因子，來修改無分類器引導過程。此方法調整最終輸出，以在維持模型穩定性的同時，提供對生成過程更強的控制。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `model` | 將套用 CFGZeroStar 引導縮放技術進行修改的擴散模型 | MODEL | 必要 | - | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `patched_model` | 已套用 CFGZeroStar 引導縮放技術的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1f5fcd1377c64609e28d85e453aaaa0bcc8f3ac322b7b7240f34f71aa113562a`
