# TextEncodeJoyImageEdit

## 概述
此節點將文字提示和可選圖像編碼為條件數據，供 JoyImage 模型使用。它結合了 CLIP 文字編碼器與可選的圖像輸入，以創建豐富的條件數據，從而引導圖像生成或編輯任務。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於編碼文字提示的 CLIP 模型 | CLIP | 是 | - |
| `提示詞` | 要編碼的文字提示，支援多行輸入和動態提示 | STRING | 是 | - |
| `vae` | 用於將圖像編碼為潛在空間的 VAE 模型 | VAE | 否 | - |
| `影像` | 可選的圖像，包含在條件數據中，最多 6 張。每張圖像作為獨立輸入連接（image_0 到 image_5） | IMAGE | 否 | 0 到 6 張圖像 |

`images` 輸入是一個自動增長組，接受 0 到 6 張圖像。當未連接任何圖像時，條件數據僅基於文字提示。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 結合文字提示和任何提供的圖像所編碼的條件數據 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`
