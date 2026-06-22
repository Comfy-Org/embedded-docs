# Stability AI 文字轉音訊

## 概述

根據文字描述生成高品質的音樂和音效。此節點使用 Stability AI 的音訊生成技術，根據您的文字提示來建立音訊內容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的音訊生成模型（預設值："stable-audio-2.5"） | COMBO | 是 | `"stable-audio-2.5"` |
| `提示詞` | 用於生成音訊內容的文字描述（預設值：空字串） | STRING | 是 | - |
| `持續時間` | 控制生成音訊的持續時間（以秒為單位）（預設值：190） | INT | 否 | 1-190 |
| `種子值` | 用於生成的隨機種子（預設值：0） | INT | 否 | 0-4294967294 |
| `採樣步數` | 控制取樣步數（預設值：8） | INT | 否 | 4-8 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `audio` | 根據文字提示生成的音訊檔案 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5185241ca7a9b4bc38dfa8bafdae63ec3c151a3038a26ffe8e35492c0550fa88`
