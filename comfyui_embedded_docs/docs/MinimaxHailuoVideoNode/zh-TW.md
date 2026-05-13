> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/zh-TW.md)

### 概述

使用 MiniMax Hailuo-02 模型從文字提示生成影片。您可以選擇性地提供一張起始圖片作為第一幀，以創建從該圖片延續的影片。

### 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | 是 | - | 用於引導影片生成的文字提示。 |
| `seed` | INT | 否 | 0 至 18446744073709551615 | 用於創建噪聲的隨機種子（預設值：0）。 |
| `first_frame_image` | IMAGE | 否 | - | 可選的圖片，用作生成影片的第一幀。 |
| `prompt_optimizer` | BOOLEAN | 否 | - | 在需要時最佳化提示以提升生成品質（預設值：True）。 |
| `duration` | COMBO | 否 | `6`<br>`10` | 輸出影片的長度，以秒為單位（預設值：6）。 |
| `resolution` | COMBO | 否 | `"768P"`<br>`"1080P"` | 影片顯示的尺寸。1080p 為 1920x1080，768p 為 1366x768（預設值："768P"）。 |

**注意：** 使用 MiniMax-Hailuo-02 模型搭配 1080P 解析度時，影片長度限制為 6 秒。

### 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `5466b9cda979a30158b818743de0e0cf30eb3e27015d431eb04a370029250a4c`
