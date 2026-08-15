# Bria 移除影像背景

此節點使用 Bria RMBG 2.0 服務從影像中移除背景。它將影像傳送到外部 API 進行處理，並回傳已移除背景的結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 將從中移除背景的輸入影像。 | IMAGE | 是 | - |
| `審核` | 審核設定。當設為 `"true"` 時，將提供額外的審核選項。 | COMBO | 否 | `"false"`<br>`"true"` |
| `visual_input_moderation` | 對輸入影像啟用視覺內容審核。此參數僅在 `moderation` 設為 `"true"` 時可用。預設值：`False`。 | BOOLEAN | 否 | - |
| `visual_output_moderation` | 對輸出影像啟用視覺內容審核。此參數僅在 `moderation` 設為 `"true"` 時可用。預設值：`True`。 | BOOLEAN | 否 | - |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果皆非確定性。預設值：`0`。 | INT | 否 | 0 至 2147483647 |

**注意：** `visual_input_moderation` 和 `visual_output_moderation` 參數依賴於 `moderation` 參數。僅當 `moderation` 設為 `"true"` 時，這兩個參數才會生效。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 已移除背景的處理後影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
