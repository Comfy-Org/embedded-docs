# 儲存影片

Save Video 節點會將輸入的影片儲存至您的 ComfyUI 輸出目錄。您可以選擇檔案名稱前置詞、容器格式、影片編解碼器，以及品質等編碼選項。此節點會使用計數器自動產生唯一的檔案名稱，並可將工作流程中繼資料嵌入所儲存的檔案中。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要儲存的影片。 | VIDEO | 是 | - |
| `檔名前綴` | 要儲存檔案的檔案名稱前置詞。可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以從節點取得數值（預設值：`video/ComfyUI`）。 | STRING | 是 | - |
| `格式` | 輸出容器。Auto 會為 Auto/H.264 使用 MP4，為 AV1 使用 WebM。MP4、MKV 與 WebM 則指定特定容器。選擇格式也會決定可用的編解碼器選項（預設值：`auto`）。 | DYNAMIC_COMBO | 是 | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `編碼器` | 輸出影片編解碼器。Auto 會保留相容的來源串流。H.264 與 AV1 重新編碼支援 SDR、HDR (HLG) 及 HDR PQ。選取格式後才會顯示（預設值：`auto`）。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"h264"`<br>`"av1"` |

### H.264 輸入

當 `codec` 為 `"h264"` 時會顯示這些輸入，且可用於 `auto`、`mp4` 與 `mkv` 格式。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `encoding` | Automatic 會保留相容的 H.264 串流。Re-encode 則套用自訂編碼選項。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"re-encode"` |
| `crf` | 數值愈低，品質愈高但檔案愈大。當 `encoding` 為 `"re-encode"` 時顯示（預設值：23.0）。 | FLOAT | 否 | 0.0 至 51.0 |

### AV1 輸入

當 `codec` 為 `"av1"` 時會顯示這些輸入，且可用於 `auto`、`mp4`、`mkv` 與 `webm` 格式。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `encoding` | Automatic 會保留相容的 AV1 串流。Re-encode 則套用自訂編碼選項。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"re-encode"` |
| `crf` | 數值愈低，品質愈高但檔案愈大。當 `encoding` 為 `"re-encode"` 時顯示（預設值：30.0）。 | FLOAT | 否 | 0.0 至 63.0 |

注意：當 `format` 為 `"auto"` 時，系統會自動選擇儲存容器：`av1` 產生 WebM，而 `auto` 與 `h264` 產生 MP4。`webm` 格式僅允許 `auto` 與 `av1` 編解碼器。當 `codec` 為 `"auto"` 時，來源影片串流會被保留，而非重新編碼。儲存的檔案會使用計數器後綴，以避免覆寫既有檔案。

## 輸出

| 輸出名 | 說明 | 資料型別 |
| --- | --- | --- |
| `video` | 輸入的影片，保持不變。 | VIDEO |
| `ui` | 所儲存影片檔案的預覽，包含檔案路徑與子資料夾資訊，供 UI 顯示。 | PREVIEW_VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`
