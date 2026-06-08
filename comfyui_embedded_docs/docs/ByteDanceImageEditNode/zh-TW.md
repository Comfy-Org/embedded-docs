## 概述

ByteDance 圖片編輯節點可讓您透過 API 使用 ByteDance 的 AI 模型來修改圖片。您提供輸入圖片和描述所需變更的文字提示，節點會根據您的指示處理圖片。此節點會自動處理 API 通訊，並回傳編輯後的圖片。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `model` | 模型名稱 | MODEL | COMBO | seededit_3 | Image2ImageModelName 選項 |
| `image` | 要編輯的基礎圖片 | IMAGE | IMAGE | - | - |
| `prompt` | 編輯圖片的指示 | STRING | STRING | "" | - |
| `seed` | 用於生成的隨機種子 | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | 數值越高，圖片越貼近提示內容 | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | 是否在圖片上添加「AI 生成」浮水印 | BOOLEAN | BOOLEAN | True | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 從 ByteDance API 回傳的編輯後圖片 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
