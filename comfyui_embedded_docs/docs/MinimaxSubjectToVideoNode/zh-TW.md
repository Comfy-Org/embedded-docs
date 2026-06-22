# MinimaxSubjectToVideoNode

## 概述

使用 MiniMax 的 API，根據主體影像和文字提示同步生成影片。此節點接收主體影像和描述，根據提示建立動畫或呈現該主體的影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `subject` | 用於影片生成參考的主體影像 | IMAGE | 是 | - |
| `prompt_text` | 引導影片生成的文字提示（預設：空字串） | STRING | 是 | - |
| `model` | 用於影片生成的模型（預設："S2V-01"） | COMBO | 否 | "S2V-01" |
| `seed` | 用於建立雜訊的隨機種子（預設：0） | INT | 否 | 0 到 18446744073709551615 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 根據輸入主體影像和提示產生的影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
