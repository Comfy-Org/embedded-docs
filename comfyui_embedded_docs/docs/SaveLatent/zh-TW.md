> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/zh-TW.md)

{heading_overview}

SaveLatent 節點可將潛空間張量以檔案形式儲存至磁碟，供後續使用或分享。它接收潛空間樣本並將其儲存至輸出目錄，同時可選擇包含提示資訊等中繼資料。此節點會自動處理檔案命名與組織，並保留潛空間資料結構。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | 是 | - | 要儲存至磁碟的潛空間樣本 |
| `filename_prefix` | STRING | 否 | - | 輸出檔名的前綴詞（預設值："latents/ComfyUI"） |
| `prompt` | PROMPT | 否 | - | 要包含在中繼資料中的提示資訊（隱藏參數） |
| `extra_pnginfo` | EXTRA_PNGINFO | 否 | - | 要包含在中繼資料中的額外 PNG 資訊（隱藏參數） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `ui` | UI | 在 ComfyUI 介面中提供已儲存潛空間檔案的位址資訊 |