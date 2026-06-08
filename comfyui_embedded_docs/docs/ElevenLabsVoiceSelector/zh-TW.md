## 概述

ElevenLabs 語音選擇器節點可讓您從預先定義的 ElevenLabs 文字轉語音語音清單中選擇特定語音。它接收語音名稱作為輸入，並輸出音訊生成所需的對應語音識別碼。此節點簡化了選擇相容語音以與其他 ElevenLabs 音訊節點搭配使用的流程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `語音` | 從預先定義的 ElevenLabs 語音中選擇一個語音。 | STRING | 是 | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `語音` | 所選 ElevenLabs 語音的獨特識別碼，可傳遞給其他節點以進行文字轉語音生成。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b87f5b2b8accca87d0593ab1f4bcfccaa84b393ddb3fd9121758a87871592cee`
