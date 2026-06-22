# Bria 移除影像背景

此節點使用 Bria RMBG 2.0 服務從影像中移除背景。它將影像發送到外部 API 進行處理，並返回移除背景後的結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 將從中移除背景的輸入影像。 | IMAGE | 是 | - |
| `審核` | 審核設定。當設定為 `"true"` 時，將啟用其他審核選項。 | COMBO | 否 | `"false"`<br>`"true"` |
| `visual_input_moderation` | 對輸入影像啟用視覺內容審核。此參數僅在 `審核` 設定為 `"true"` 時可用。預設值：`False`。 | BOOLEAN | 否 | - |
| `visual_output_moderation` | 對輸出影像啟用視覺內容審核。此參數僅在 `審核` 設定為 `"true"` 時可用。預設值：`True`。 | BOOLEAN | 否 | - |
| `種子` | 控制節點是否應重新執行的種子值。無論種子值為何，結果都是非確定性的。預設值：`0`。 | INT | 否 | 0 到 2147483647 |

**注意：** `visual_input_moderation` 和 `visual_output_moderation` 參數依賴於 `moderation` 參數。它們僅在 `moderation` 設定為 `"true"` 時才處於啟用狀態且為必要參數。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `影像` | 已移除背景的處理後影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2b2dd3ca0d026af1a2bf3f7222165928527b05b65817073b50230ff18d39bc6c`
