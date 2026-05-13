> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/zh-TW.md)

## 概述

SaveWEBM 節點可將一系列影像儲存為 WEBM 格式的影片檔案。它接收多個輸入影像，並使用 VP9 或 AV1 編解碼器，配合可設定的品質參數與影格率，將其編碼為影片。最終的影片檔案會連同提示資訊等中繼資料，一同儲存至輸出目錄。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | - | 要編碼為影片影格的輸入影像序列 |
| `filename_prefix` | STRING | 否 | - | 輸出檔案名稱的前綴（預設值："ComfyUI"） |
| `codec` | COMBO | 是 | "vp9"<br>"av1" | 用於編碼的影片編解碼器 |
| `fps` | FLOAT | 否 | 0.01-1000.0 | 輸出影片的影格率（預設值：24.0） |
| `crf` | FLOAT | 否 | 0-63.0 | 品質設定，數值越高表示品質越低、檔案越小；數值越低表示品質越高、檔案越大（預設值：32.0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `ui` | PREVIEW | 顯示已儲存 WEBM 檔案的影片預覽 |

---
**Source fingerprint (SHA-256):** `761ce5148c273ffe3789be75c2a00268241d3ec7ecebd5b10efd1b1cc98d85ea`
