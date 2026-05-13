> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/zh-TW.md)

## 概述

Kling 文字轉影片節點可將文字描述轉換為影片內容。它接收文字提示，並根據指定的配置設定生成對應的影片序列。此節點支援不同的畫面比例和生成模式，以產生不同長度和品質的影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 正向文字提示 |
| `負向提示詞` | STRING | 是 | - | 負向文字提示 |
| `cfg_scale` | FLOAT | 否 | 0.0 至 1.0 | 配置縮放值（預設值：1.0） |
| `aspect_ratio` | COMBO | 否 | 選項來自 KlingVideoGenAspectRatio | 影片畫面比例設定（預設值："16:9"） |
| `mode` | COMBO | 否 | 提供多個選項 | 用於影片生成的配置，格式為：模式 / 時長 / 模型名稱。（預設值：modes[8]） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video_id` | VIDEO | 生成的影片輸出 |
| `時長` | STRING | 生成影片的唯一識別碼 |
| `duration` | STRING | 生成影片的時長資訊 |

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`
