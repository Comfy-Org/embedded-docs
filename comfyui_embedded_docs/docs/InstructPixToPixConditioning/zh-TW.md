# 指令式像素轉像素條件設定

## 概述

InstructPixToPixConditioning 節點透過將正向與負向文字提示與影像資料結合，為 InstructPix2Pix 影像編輯準備條件化資料。它透過 VAE 編碼器處理輸入影像以建立潛在表示，並將這些潛在資料附加到正向與負向條件化資料中。該節點會自動處理影像尺寸，將其裁剪為 8 像素的倍數，以確保與 VAE 編碼過程相容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 包含文字提示與所需影像特徵設定的正向條件化資料 | CONDITIONING | 是 | - |
| `負向` | 包含文字提示與非所需影像特徵設定的負向條件化資料 | CONDITIONING | 是 | - |
| `vae` | 用於將輸入影像編碼為潛在表示的 VAE 模型 | VAE | 是 | - |
| `像素` | 待處理並編碼至潛在空間的輸入影像 | IMAGE | 是 | - |

**注意：** 輸入影像尺寸會自動調整，透過將寬度與高度裁剪至最接近的 8 像素倍數，以確保與 VAE 編碼過程相容。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 附加了潛在影像表示的正向條件化資料 | CONDITIONING |
| `潛在空間` | 附加了潛在影像表示的負向條件化資料 | CONDITIONING |
| `latent` | 與編碼影像具有相同維度的空潛在張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4b2383c9d64efdb558758359bf544fc5a1be65c12b23b54152e2df79a6dd8d79`
