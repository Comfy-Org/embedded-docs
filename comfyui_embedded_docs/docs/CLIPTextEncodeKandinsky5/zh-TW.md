> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/zh-TW.md)

## 概述

CLIPTextEncodeKandinsky5 節點用於準備與 Kandinsky 5 模型搭配使用的文字提示。它接收兩個獨立的文字輸入，使用提供的 CLIP 模型進行標記化處理，並將其組合成單一的條件化輸出。此輸出將用於引導影像生成過程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | | 用於對文字提示進行標記化和編碼的 CLIP 模型。 |
| `clip_l` | STRING | 是 | | 主要文字提示。此輸入支援多行文字和動態提示。 |
| `qwen25_7b` | STRING | 是 | | 次要文字提示。此輸入支援多行文字和動態提示。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 從兩個文字提示生成的組合條件化資料，可直接饋入 Kandinsky 5 模型進行影像生成。 |

---
**Source fingerprint (SHA-256):** `80227cf87d46bfa42b07976ab29996ae9583a4c461b2f2408db4b7016d3e1a0c`
