# SaveWEBM

SaveWEBM 節點將一系列影像儲存為 WEBM 影片檔案。它使用 VP9 或 AV1 編解碼器，以可設定的幀率和品質設定將輸入影像編碼為影片，並將檔案儲存到輸出目錄。若可用，提示詞和工作流程中繼資料會嵌入影片檔案中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要編碼至影片的影像序列。RGBA 影像會以其 Alpha 通道儲存為透明度（僅限 vp9 編解碼器）。 | IMAGE | 是 | - |
| `filename_prefix` | 輸出檔名的前綴；計數器和 .webm 副檔名會自動附加（預設值："ComfyUI"） | STRING | 否 | - |
| `codec` | 用於編碼的影片編解碼器 | COMBO | 是 | "vp9"<br>"av1" |
| `fps` | 輸出影片的幀率（預設值：24.0） | FLOAT | 否 | 0.01-1000.0 |
| `crf` | crf 值越高表示品質越低、檔案越小；crf 值越低表示品質越高、檔案越大（預設值：32.0） | FLOAT | 否 | 0-63.0 |

**Alpha 通道備註：** RGBA 影像的 Alpha 通道僅在使用 vp9 編解碼器時保留。使用 av1 編解碼器時，Alpha 通道會被忽略，僅編碼 RGB 資料。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 輸入影像序列，原封不動地傳遞 | IMAGE |
| `ui` | 顯示已儲存 WEBM 檔案的影片預覽 | PREVIEW |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
