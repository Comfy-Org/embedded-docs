# 儲存影片

Save Video 節點會將輸入影片儲存到你的 ComfyUI 輸出目錄。你可以選擇檔案名稱前綴、容器格式、影片編解碼器，以及如品質等編碼選項。此節點會使用計數器自動產生唯一的檔案名稱，並可將工作流程中繼資料嵌入已儲存的檔案中。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要儲存的影片。 | VIDEO | 是 | - |
| `檔名前綴` | 要儲存檔案的前綴。可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以納入節點中的值（預設：`video/ComfyUI`）。 | STRING | 是 | - |
| `格式` | 輸出容器。Auto 會對 Auto/H.264 使用 MP4，並對 AV1 使用 WebM。MP4、MKV 和 WebM 會選擇特定容器。選擇格式也會決定哪些編解碼器選項可用（預設：`auto`）。 | DYNAMIC_COMBO | 是 | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `編碼器` | 輸出影片編解碼器。Auto 會保留相容的來源串流。H.264 與 AV1 重新編碼支援 SDR、HDR (HLG) 和 HDR PQ。此選取器巢狀於所選格式之下（預設：`auto`）。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"h264"`<br>`"av1"`（不適用於 `webm` 格式） |

### H.264 輸入

當 `codec` 為 `"h264"`，且使用 `auto`、`mp4` 和 `mkv` 格式時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `encoding` | 自動會保留相容的 H.264 串流。重新編碼會套用自訂編碼選項。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"re-encode"` |
| `crf` | 較低的值會產生更高品質與更大的檔案。當 `encoding` 為 `"re-encode"` 時顯示（預設：23.0）。 | FLOAT | 否 | 0.0 至 51.0 |

### AV1 輸入

當 `codec` 為 `"av1"`，且使用 `auto`、`mp4`、`mkv` 和 `webm` 格式時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `encoding` | 自動會保留相容的 AV1 串流。重新編碼會套用自訂編碼選項。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"re-encode"` |
| `crf` | 較低的值會產生更高品質與更大的檔案。當 `encoding` 為 `"re-encode"` 時顯示（預設：30.0）。 | FLOAT | 否 | 0.0 至 63.0 |

注意：當 `format` 為 `"auto"` 時，會自動選擇儲存的容器：`av1` 會產生 WebM，而 `auto` 和 `h264` 會產生 MP4。`webm` 格式僅允許 `auto` 和 `av1` 編解碼器。當 `codec` 為 `"auto"` 時，會保留來源影片串流，而不是重新編碼。儲存的檔案會使用計數器後綴，以避免覆寫現有檔案。副檔名由解析後的容器決定。除非啟動時停用中繼資料儲存，否則工作流程中繼資料（提示詞與額外節點資訊）會嵌入已儲存的檔案中。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 輸入影片，保持不變。 | VIDEO |
| `ui` | 已儲存影片檔案的預覽，包含檔案路徑與子資料夾資訊，以供在 UI 中顯示。 | PREVIEW_VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`
