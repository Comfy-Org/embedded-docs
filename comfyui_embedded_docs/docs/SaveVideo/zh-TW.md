# 儲存影片

Save Video 節點會將輸入的影片儲存到您的 ComfyUI 輸出目錄。您可以選擇檔案名稱前置詞、容器格式、影片編解碼器，以及品質與色彩空間等編碼選項。此節點會自動以計數器遞增方式處理檔案命名，並可將工作流程中繼資料嵌入儲存的檔案中。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要儲存的影片。 | VIDEO | 是 | - |
| `檔名前綴` | 要儲存檔案的前置詞。可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以納入來自節點的值（預設："video/ComfyUI"）。 | STRING | 是 | - |
| `格式` | 輸出容器。Auto 會在可能時保留來源容器；MP4、MKV 和 WebM 則選取特定容器（預設："auto"）。 | DYNAMIC_COMBO | 是 | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `編碼器` | 輸出影片編解碼器。Auto 會保留相容的來源串流。H.264 與 AV1 重新編碼支援 SDR、HDR (HLG) 與 HDR PQ。當選取格式時出現（預設："auto"）。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"h264"`<br>`"av1"` |

### H.264 輸入

當 `codec` 為 `"h264"` 時，這些輸入會出現。此編解碼器可用於 `auto`、`mp4` 與 `mkv` 格式。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `encoding` | Automatic 會保留相容的 H.264 串流。Re-encode 則套用自訂編碼選項。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"re-encode"` |
| `crf` | 數值越低，品質越高且檔案越大。當 `encoding` 為 `"re-encode"` 時出現（預設：23.0）。 | FLOAT | 否 | 0.0 至 51.0 |
| `color_space` | Auto 會對從影像建立的影片使用 sRGB，並在載入的影片上保留可辨識的色彩。sRGB 寫入 SDR BT.709/sRGB。HDR 寫入 10-bit BT.2020/HLG；HDR PQ 寫入 BT.2020/PQ。其他輸入像素必須已使用選取的色彩空間。當 `encoding` 為 `"re-encode"` 時出現（預設："auto"）。 | COMBO | 否 | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

### AV1 輸入

當 `codec` 為 `"av1"` 時，這些輸入會出現。此編解碼器可用於 `auto`、`mp4`、`mkv` 與 `webm` 格式。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `encoding` | Automatic 會保留相容的 AV1 串流。Re-encode 則套用自訂編碼選項。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"re-encode"` |
| `crf` | 數值越低，品質越高且檔案越大。當 `encoding` 為 `"re-encode"` 時出現（預設：30.0）。 | FLOAT | 否 | 0.0 至 63.0 |
| `color_space` | Auto 會對從影像建立的影片使用 sRGB，並在載入的影片上保留可辨識的色彩。sRGB 寫入 SDR BT.709/sRGB。HDR 寫入 10-bit BT.2020/HLG；HDR PQ 寫入 BT.2020/PQ。其他輸入像素必須已使用選取的色彩空間。當 `encoding` 為 `"re-encode"` 時出現（預設："auto"）。 | COMBO | 否 | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

注意：`webm` 格式僅支援 `auto` 與 `av1` 編解碼器。當 `format` 為 `"auto"` 時，會盡可能保留來源容器。當 `color_space` 為 `"auto"` 時，不會套用明確的色彩空間，而是自動判斷色彩空間。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 輸入的影片，保持不變。 | VIDEO |
| `ui` | 已儲存影片檔案的預覽，包含檔案路徑與子資料夾資訊，供 UI 顯示。 | PREVIEW_VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `39b168eab2d6798adfec6ace3d4320f26217d893844ba54e62041cfdf0183e6f`
