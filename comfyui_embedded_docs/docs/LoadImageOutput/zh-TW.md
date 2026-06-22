# 載入圖片（來自輸出）

## 概述

LoadImageOutput 節點可從輸出資料夾載入圖片。當您點擊重新整理按鈕時，它會更新可用圖片清單並自動選取第一張圖片，讓您能輕鬆瀏覽已生成的圖片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 從輸出資料夾載入圖片。包含上傳選項及重新整理按鈕，可更新圖片清單。點擊重新整理按鈕後，節點會更新圖片清單並自動選取第一張圖片，方便您快速迭代瀏覽。 | COMBO | 是 | 多個可用選項 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 從輸出資料夾載入的圖片 | IMAGE |
| `mask` | 與載入圖片相關聯的遮罩 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d1de0140765c9d5dd393715faa84dc5c3f0e49117391b8823a51b176bcb568d8`
