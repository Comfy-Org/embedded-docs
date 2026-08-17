# SamplerLCMUpscale

SamplerLCMUpscale 節點提供了一種特殊的取樣方法，結合了潛在一致性模型（LCM）取樣與影像放大功能。它讓您能在取樣過程中，使用各種插值方法放大影像，有助於在維持影像品質的同時產生更高解析度的輸出。放大會在取樣步驟中逐步進行，直到達到目標的 `scale_ratio` 為止。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `scale_ratio` | 放大過程中要套用的縮放比例（預設：1.0） | FLOAT | 否 | 0.1 - 20.0 |
| `scale_steps` | 用於放大過程的步數。使用 -1 進行自動計算（預設：-1） | INT | 否 | -1 - 1000 |
| `upscale_method` | 用於放大影像的插值方法（預設：bislerp） | COMBO | 是 | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

注意：當 `scale_steps` 設定為正值時，有效的放大步數會受限於取樣器的總取樣步數。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 傳回一個已配置的取樣器物件，可用於取樣流程中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
