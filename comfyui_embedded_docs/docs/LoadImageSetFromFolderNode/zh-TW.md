## 概述

LoadImageSetFromFolderNode 從指定的資料夾目錄載入多張圖片，以供訓練使用。它會自動偵測常見的圖片格式，並可選擇使用不同方法調整圖片大小，然後以批次形式回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `folder` | 要載入圖片的資料夾。 | STRING | 是 | 提供多個選項 |
| `resize_method` | 調整圖片大小的方法（預設值："None"）。 | STRING | 否 | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 以單一張量形式呈現的已載入圖片批次。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`
