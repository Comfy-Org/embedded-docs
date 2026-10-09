# Load LoRA (Model)

在單一節點中將一疊 LoRA 應用到擴散模型。`loras` 的每一行包含一個 LoRA 檔案、其強度以及一個開/關切換，且這些行會由上而下套用，因此每一行都會修補其上一行的結果。當工作流程要對同一個模型套用一長串 LoRA 時，請使用此節點，而不是串聯多個單一 LoRA 載入器。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | LoRA 將套用到的擴散模型。 | MODEL | 是 | - |
| `loras` | 可增長的 LoRA 群組，會依行順序套用到模型（`loras.0`、`loras.1` 等等）。每個 LoRA 新增一行；每一行包含一個檔案、一個強度以及一個開/關切換。 | DYNAMIC_GROUP | 是 | 1 至 20 列 |

### `loras` 行欄位

每一行會重複以下欄位，且每個欄位在提交的行中皆為必填。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `lora_name` | 要套用的 LoRA 檔案名稱。 | COMBO | 是 | 多個選項可用 |
| `strength` | 套用此 LoRA 的強度。`0` 會將其關閉，而負值會反轉效果。（預設值：1.0） | FLOAT | 是 | -100 至 100 （步進值：0.01） |
| `enabled` | 關閉以跳過此 LoRA，而不變更其檔案或強度。（預設值：true） | BOOLEAN | 是 | false / true |

### 參數限制

- **行數：** 必須提交至少一行，且最多接受 20 行，因此最高行索引為 19。
- **跳過行：** 當行的檔案為空、`enabled` 為關閉，或 `strength` 為 `0` 時，該行會被跳過。負強度會直接傳遞，而不是被跳過。
- **行順序：** 行會依其出現的順序套用，且每一行都會從前一行傳回的模型開始。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 已套用每個啟用的 LoRA 行的擴散模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a656bba0248d2f6d4eb65e15e3a19f2e76edecd4b34710921a02f3ba5c598e1d`
