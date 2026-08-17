# 儲存影片

SaveVideo 節點會將輸入的影片儲存至您的 ComfyUI 輸出目錄。您可以選擇檔案名稱前綴、影片格式和編解碼器，節點會自動加入計數器來建立唯一的檔案名稱。預設情況下，此節點也會將工作流程中繼資料儲存在儲存的影片中。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `codec` | 用於影片的編解碼器。選擇 `h264` 會顯示額外的編碼選項（預設："auto"）。 | DYNAMIC_COMBO | 是 | "auto"<br>"h264" |
| `video` | 要儲存的影片。 | VIDEO | 是 | - |
| `filename_prefix` | 儲存檔案的名稱前綴。此欄位可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以從節點取得數值（預設："video/ComfyUI"）。 | STRING | 是 | - |
| `format` | 影片儲存的格式。這會決定儲存影片的副檔名（預設："auto"）。 | COMBO | 是 | "auto"<br>"mp4"<br>"webm"<br>"mkv"<br>"gif" |

### h264 輸入

當 `codec` 設為 `h264` 時，會顯示這些輸入。

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `encoding` | H.264 的編碼模式。`auto`（自動）模式會保留相容的 H.264 串流。`re-encode`（重新編碼）模式會套用自訂的 CRF（預設："auto"）。 | DYNAMIC_COMBO | 否 | "auto"<br>"re-encode" |
| `crf` | 數值越低，品質越高，檔案越大。僅在 `encoding` 設為 `re-encode` 時可用（預設：23.0）。 | FLOAT | 是（僅當 `encoding` 為 `re-encode` 時） | 0.0 to 51.0 (step: 1.0) |

注意：如果 `filename_prefix` 包含資料夾，例如 `video/ComfyUI`，影片會儲存在輸出目錄的該子資料夾中。檔案名稱會由前綴加上計數器組成，例如 `ComfyUI_00001_.mp4`，因此不會覆寫既有檔案。

注意：啟用中繼資料時，此節點會將工作流程提示詞與額外中繼資料嵌入儲存的影片中。您可以透過使用 `--disable-metadata` 參數啟動 ComfyUI 來停用中繼資料。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `video` | 已儲存的影片，直接從輸入傳遞而來。 | VIDEO |
| `ui` | 已儲存影片檔案的預覽，包含用於在使用者介面中顯示的檔案路徑與子資料夾資訊。 | PREVIEW_VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c1fd5ac1043f0811951136b2d09cd59840b0c542079da9ed04c17cca7c02562b`
