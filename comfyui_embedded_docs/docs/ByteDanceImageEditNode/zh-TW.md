> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/zh-TW.md)

## 概述

ByteDance 圖片編輯節點可讓您透過 API 使用 ByteDance 的 AI 模型來修改圖片。您提供輸入圖片和描述所需變更的文字提示，節點會根據您的指示處理圖片。此節點會自動處理 API 通訊，並回傳編輯後的圖片。

## 輸入

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 說明 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Image2ImageModelName 選項 | 模型名稱 |
| `image` | IMAGE | IMAGE | - | - | 要編輯的基礎圖片 |
| `prompt` | STRING | STRING | "" | - | 編輯圖片的指示 |
| `seed` | INT | INT | 0 | 0-2147483647 | 用於生成的隨機種子 |
| `guidance_scale` | FLOAT | FLOAT | 5.5 | 1.0-10.0 | 數值越高，圖片越貼近提示內容 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 是否在圖片上添加「AI 生成」浮水印 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 從 ByteDance API 回傳的編輯後圖片 |

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
