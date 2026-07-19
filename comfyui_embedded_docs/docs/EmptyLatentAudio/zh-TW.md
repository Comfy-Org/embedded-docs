# 空白潛空間音訊

## 概述

EmptyLatentAudio 節點會建立一個用於音訊處理的空潛在張量。它會根據指定的音訊長度和批次大小，生成一個空白的音訊潛在表示，可作為音訊生成或處理工作流程的起點。此節點會根據音訊長度和取樣率自動計算適當的潛在維度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `秒數` | 音訊的持續時間（秒），預設值：47.6 | FLOAT | 是 | 1.0 - 1000.0 |
| `批次大小` | 批次中的潛在影像數量，預設值：1 | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 傳回一個用於音訊處理的空潛在張量，包含指定的持續時間和批次大小。該張量的形狀為 [batch_size, 64, length]，其中 length 是根據音訊持續時間和取樣率計算得出。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `004f730131b179fe5ac072afe81b2e01a3937fceca5a260b4ae66f92774e96d9`
