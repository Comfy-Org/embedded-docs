> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/zh-TW.md)

{heading_overview}

LoadImageSetNode 從輸入目錄載入多張影像，用於批次處理和訓練目的。它支援多種影像格式，並可選擇使用不同方法調整影像尺寸。此節點將所有選取的影像作為批次處理，並以單一張量形式傳回。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | 多個影像檔案 | 從輸入目錄中選取多張影像。支援 PNG、JPG、JPEG、WEBP、BMP、GIF、JPE、APNG、TIF 和 TIFF 格式。允許批次選取影像。 |
| `resize_method` | STRING | 否 | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | 調整載入影像尺寸的選用方法（預設："None"）。選擇 "None" 保持原始尺寸，"Stretch" 強制調整尺寸，"Crop" 透過裁剪保持長寬比，或 "Pad" 透過添加邊框保持長寬比。 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 包含所有載入影像的張量，作為批次供後續處理使用。 |