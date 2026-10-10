# Load LoRA (Text Encoder)

在單一節點中將一疊 LoRA 套用到 CLIP 文字編碼器。`loras` 的每一列會保存一個 LoRA 檔案、其強度與一個啟用/停用開關，且這些列會由上而下依序套用，因此每一列都會在上一列的結果上進行修補。會變更文字編碼器的 LoRA 檔案通常也會套用到模型上，因此此節點通常會搭配 Load LoRA (Model)，並使用相同的列。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 要套用 LoRA 的 CLIP 文字編碼器。 | CLIP | 是 | - |
| `loras` | 可增長的 LoRA 群組，會依列順序套用到文字編碼器（`loras.0`、`loras.1` 等）。每個 LoRA 新增一列；每一列包含一個檔案、一個強度與一個啟用/停用開關。 | DYNAMIC_GROUP | 是 | 1 到 20 列 |

### `loras` 列欄位

每一列都會重複以下欄位，且每個欄位在提交的列中皆為必填。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `lora_name` | 要套用的 LoRA 檔案名稱。 | COMBO | 是 | 有多個可用選項 |
| `strength` | 將此 LoRA 套用到文字編碼器的強度。`0` 會將其關閉，負值則會反轉效果。（預設值：1.0） | FLOAT | 是 | -100 到 100（步長 0.01） |
| `enabled` | 關閉以跳過此 LoRA，而不變更其檔案或強度。（預設值：true） | BOOLEAN | 是 | false / true |

### 參數限制

- **列數：** 至少必須提交一列，且最多接受 20 列，因此最高的列索引為 19。
- **略過的列：** 當某一列的檔案為空、`enabled` 為關閉，或 `strength` 為 `0` 時，該列會被略過。負強度會被傳遞下去，而不是被略過。
- **列順序：** 列會依其出現順序套用，且每一列都會從上一列傳回的文字編碼器開始。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CLIP` | 已套用所有未被略過的 LoRA 列後的 CLIP 文字編碼器。 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraTextEncoder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b290d2caddc3937e962e65c70a5c99cbd4cdb40ab6f86bba8f0c270e5cebf00`
