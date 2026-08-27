# SaveWEBM

SaveWEBM 節點將一系列影像儲存為 WEBM 視訊檔案。它接收多張輸入影像，並使用 VP9 或 AV1 編解碼器，搭配可設定的品質設定與幀率，將其編碼為視訊。產生的視訊檔案會連同包含提示資訊的中繼資料一起儲存到輸出目錄。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | RGBA 影像會將其 Alpha 通道儲存為透明度（僅限 vp9 編解碼器）。 | IMAGE | 是 | - |
| `檔名前綴` | 輸出檔案名稱的前綴（預設值："ComfyUI"）。 | STRING | 否 | - |
| `編碼器` | 用於編碼的視訊編解碼器。 | COMBO | 是 | "vp9"<br>"av1" |
| `每秒影格數` | 輸出視訊的幀率（預設值：24.0）。 | FLOAT | 否 | 0.01-1000.0 |
| `CRF` | 較高的 crf 表示較低的品質與較小的檔案大小，較低的 crf 表示較高的品質與較大的檔案大小（預設值：32.0）。 | FLOAT | 否 | 0-63.0 |

**關於 Alpha 通道的說明：** 只有使用 VP9 編解碼器時，RGBA 影像的 Alpha 通道才會被保留。使用 AV1 編解碼器時，Alpha 通道會被忽略，僅編碼 RGB 資料。

**關於檔案命名的說明：** 視訊會以 `{filename_prefix}_{counter:05}_.webm` 的形式儲存到輸出目錄，其中計數器會自動遞增，以避免覆寫現有檔案。

## 輸出
| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 輸入影像，在視訊儲存後原樣傳遞。 | IMAGE |
| UI preview | 顯示已儲存 WEBM 檔案的視訊預覽。 | PREVIEW |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
