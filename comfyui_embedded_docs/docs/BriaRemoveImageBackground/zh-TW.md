# Bria 移除影像背景

此節點使用 Bria RMBG 2.0 服務移除影像背景。它會將影像傳送至外部 API 進行處理，並回傳已移除背景的結果。

## 輸入

當 `moderation` 選擇器設為 `"true"` 時，會顯示額外的審核選項。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 將從中移除背景的輸入影像。 | IMAGE | 是 | - |
| `審核` | 審核設定。當設為 `"true"` 時，會提供額外的審核選項。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |
| `種子` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果皆非確定性。預設：`0`。 | INT | 是 | 0 至 2147483647 |

### Moderation "true" 輸入

這些參數僅在 `moderation` 設為 `"true"` 時出現。`"false"` 選項不會新增任何額外輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 啟用輸入影像的視覺內容審核。預設：`False`。 | BOOLEAN | 否 | - |
| `visual_output_moderation` | 啟用輸出影像的視覺內容審核。預設：`True`。 | BOOLEAN | 否 | - |

**注意：** `visual_input_moderation` 與 `visual_output_moderation` 參數相依於 `moderation` 參數。它們僅在 `moderation` 設為 `"true"` 時生效。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 已移除背景的處理後影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
