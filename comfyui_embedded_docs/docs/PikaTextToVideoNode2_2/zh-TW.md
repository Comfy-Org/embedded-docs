## 概述

Pika Text2Video v2.2 節點會將文字提示發送到 Pika API 2.2 版本以生成影片。它使用 Pika 的 AI 影片生成服務，將您的文字描述轉換為影片。此節點允許您自訂影片生成過程的各個方面，包括長寬比、持續時間和解析度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt_text` | 描述您希望在影片中生成內容的主要文字描述 | STRING | 是 | - |
| `negative_prompt` | 描述您不希望出現在生成影片中的文字 | STRING | 是 | - |
| `seed` | 控制生成隨機性的數值，用於產生可重現的結果 | INT | 是 | - |
| `resolution` | 輸出影片的解析度設定 | STRING | 是 | - |
| `duration` | 影片的長度（以秒為單位） | INT | 是 | - |
| `aspect_ratio` | 長寬比（寬度 / 高度）（預設值：1.7777777777777777） | FLOAT | 否 | 0.4 - 2.5 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 從 Pika API 返回的生成影片檔案 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`
