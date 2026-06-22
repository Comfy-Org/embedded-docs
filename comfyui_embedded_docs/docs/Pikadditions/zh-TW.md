# Pikadditions

## 概述

Pikadditions 節點讓您可以將任何物體或圖片添加到您的影片中。您上傳一段影片並指定要添加的內容，即可創造出無縫整合的結果。此節點使用 Pika API 將圖片以自然融合的方式插入影片中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要添加圖片的目標影片。 | VIDEO | 是 | - |
| `image` | 要添加到影片中的圖片。 | IMAGE | 是 | - |
| `prompt_text` | 描述要添加到影片中的內容的文字。 | STRING | 是 | - |
| `negative_prompt` | 描述要在影片中避免出現的內容的文字。 | STRING | 是 | - |
| `seed` | 用於產生可重現結果的隨機種子值。 | INT | 是 | 0 到 4294967295 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 已插入圖片的處理後影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`
