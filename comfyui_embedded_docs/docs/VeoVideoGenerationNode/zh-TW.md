## 概述

使用 Google 的 Veo 2 API 從文字提示生成影片。此節點可以根據文字描述和可選的圖片輸入來建立影片，並可控制長寬比、時長等參數。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 影片的文字描述（預設：空） | STRING | 是 | - |
| `長寬比` | 輸出影片的長寬比（預設："16:9"） | COMBO | 是 | "16:9"<br>"9:16" |
| `負向提示詞` | 負面文字提示，用於引導影片中應避免的內容（預設：空） | STRING | 否 | - |
| `持續秒數` | 輸出影片的時長（秒）（預設：5） | INT | 否 | 5-8 |
| `增強提示詞` | 是否使用 AI 輔助增強提示（預設：True）。這是一個進階參數。 | BOOLEAN | 否 | - |
| `生成人物` | 是否允許在影片中生成人物（預設："ALLOW"）。這是一個進階參數。 | COMBO | 否 | "ALLOW"<br>"BLOCK" |
| `種子` | 影片生成的隨機種子（0 表示隨機）（預設：0）。這是一個進階參數。 | INT | 否 | 0-4294967295 |
| `影像` | 可選的參考圖片，用於引導影片生成 | IMAGE | 否 | - |
| `model` | 用於影片生成的 Veo 2 模型（預設："veo-2.0-generate-001"） | COMBO | 否 | "veo-2.0-generate-001" |

**注意：** `generate_audio` 參數僅適用於 Veo 3.0 模型，並由節點根據所選模型自動處理。使用 Veo 3.0 模型時，`enhance_prompt` 參數將強制設為 True。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1a8b8ffe82fce32566815248f4a2434a1b865b5e5651935ccb3b92c7e38adee9`
