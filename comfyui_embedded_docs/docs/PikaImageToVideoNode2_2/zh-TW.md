> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/zh-TW.md)

## 概述

Pika 圖片轉影片節點會將圖片和文字提示傳送至 Pika API 2.2 版本以產生影片。它會根據提供的描述和設定，將輸入的圖片轉換為影片格式。此節點負責處理 API 通訊，並將產生的影片作為輸出回傳。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要轉換為影片的圖片 |
| `prompt_text` | STRING | 是 | - | 引導影片生成的文字描述 |
| `negative_prompt` | STRING | 是 | - | 描述影片中應避免出現的內容的文字 |
| `seed` | INT | 是 | - | 用於可重現結果的隨機種子值 |
| `resolution` | STRING | 是 | - | 輸出影片的解析度設定 |
| `duration` | INT | 是 | - | 生成的影片長度（以秒為單位） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
