# QwenImage21Cache

QwenImage21Cache 節點會設定 Qwen-Image 2.1 模型的 KV 前綴快取：快取的鍵與值儲存在何處，以及以何種精度儲存。文字與參考 token 只會計算一次，並在取樣步驟之間重複使用；編輯工作流程的大部分加速正是來自這裡，而此節點可讓你以記憶體換取速度，或完全排除快取。此節點標記為實驗性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要設定其前綴快取的 Qwen-Image 2.1 模型。 | MODEL | 是 | - |
| `device` | 快取的鍵與值儲存在何處。`"auto"`（預設）會優先使用剩餘的 VRAM，然後使用 RAM；`"gpu"` 會將快取儲存在 VRAM；`"cpu"` 會將其儲存在 RAM，並在運算進行時預取，幾乎不影響速度；`"off"` 會每個步驟都重新計算前綴，速度較慢，但這是完全排除快取的唯一方式。 | COMBO | 是 | `"auto"`<br>`"gpu"`<br>`"cpu"`<br>`"off"` |
| `dtype` | 快取的儲存精度。`"default"` 為無損；`"int8"` 將快取減半，精度約等同 bf16；`"int4"` 將快取縮至四分之一，但每步誤差大約增加一倍。 | COMBO | 是 | `"default"`<br>`"int8"`<br>`"int4"` |

當快取無法放入時，模型會重新計算前綴，而不是逐出另一個分支的槽位，因此設定過大只會降低速度，而不會讓執行失敗。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 已套用快取裝置與精度的模型，可供取樣。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImage21Cache/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0c10cdb465d1ee4063273ffbb4913def3830f7e329694cd0a2e292d6f3c37ae4`
