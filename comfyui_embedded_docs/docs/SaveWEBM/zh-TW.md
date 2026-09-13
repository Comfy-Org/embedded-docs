# SaveWEBM

SaveWEBM 節點會將一系列影像儲存為 WEBM 影片檔案。它接受多個輸入影像，並使用 VP9 或 AV1 編解碼器，以可設定的品質設定與影格率將其編碼為影片。產生的影片檔案會連同包含提示詞資訊的中繼資料儲存至輸出目錄。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | RGBA 影像會將 alpha 通道作為透明度一併儲存（僅限 vp9 編解碼器）。 | IMAGE | 是 | - |
| `檔名前綴` | 輸出檔名的前綴（預設值："ComfyUI"）。 | STRING | 否 | - |
| `編碼器` | 用於編碼的影片編解碼器。 | COMBO | 是 | "vp9"<br>"av1" |
| `每秒影格數` | 輸出影片的影格率（預設值：24.0）。 | FLOAT | 否 | 0.01-1000.0 |
| `CRF` | `crf` 越高表示品質越低且檔案較小；`crf` 越低表示品質越高且檔案越大（預設值：32.0）。 | FLOAT | 否 | 0-63.0 |

**關於 alpha 通道的注意事項：** RGBA 影像的 alpha 通道僅在使用 VP9 編解碼器時會保留。使用 AV1 編解碼器時，alpha 通道會被忽略，且只會編碼 RGB 資料。

**關於檔案命名的注意事項：** 影片會以 `{filename_prefix}_{counter:05}_.webm` 儲存到輸出目錄，其中計數器會自動遞增，以避免覆寫現有檔案。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 輸入影像，在影片儲存後原樣傳遞。 | IMAGE |
| UI preview | 顯示已儲存 WEBM 檔案的影片預覽。 | PREVIEW |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
