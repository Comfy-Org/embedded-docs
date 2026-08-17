# Bria 移除影像背景

此節點使用 Bria RMBG 2.0 服務從影像中移除背景。它將影像傳送至外部 API 進行處理，並回傳移除背景後的結果。

## 輸入
當 `moderation` 設定為 `"true"` 時，選擇器會顯示額外的審核選項。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `moderation` | 審核設定。當設定為 `"true"` 時，會提供額外的審核選項。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |
| `image` | 要移除背景的輸入影像。 | IMAGE | 是 | - |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆非確定性。預設值：`0`。 | INT | 是 | 0 至 2147483647 |

### Moderation "true" 輸入

這些參數僅在 `moderation` 設定為 `"true"` 時顯示。`"false"` 選項不會新增額外輸入。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 在輸入影像上啟用視覺內容審核。預設值：`False`。 | BOOLEAN | 否 | - |
| `visual_output_moderation` | 在輸出影像上啟用視覺內容審核。預設值：`True`。 | BOOLEAN | 否 | - |

**注意：** `visual_input_moderation` 和 `visual_output_moderation` 參數依賴於 `moderation` 參數。它們僅在 `moderation` 設定為 `"true"` 時才生效。

## 輸出
| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 處理後且移除背景的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
