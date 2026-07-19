# LoadImageSetNode

## 概述

LoadImageSetNode 從輸入目錄載入多張圖片，以進行批次處理和訓練用途。它支援多種圖片格式，並可選擇使用不同方法調整圖片大小。此節點會將所有選取的圖片作為批次處理，並以單一張量形式回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 從輸入目錄選取多張圖片。支援 PNG、JPG、JPEG、WEBP、BMP、GIF、JPE、APNG、TIF 及 TIFF 格式。允許批次選取圖片。 | IMAGE | 是 | 多個圖片檔案 |
| `resize_method` | 可選的載入圖片調整大小方法（預設值："None"）。選擇 "None" 保留原始尺寸，"Stretch" 強制調整大小，"Crop" 透過裁切維持長寬比，或 "Pad" 透過添加邊框維持長寬比。 | STRING | 否 | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 包含所有載入圖片作為批次的張量，供後續處理使用。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`
