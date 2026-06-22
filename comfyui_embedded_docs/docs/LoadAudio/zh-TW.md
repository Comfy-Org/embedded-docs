# 載入音訊

## 概述

LoadAudio 節點可從輸入目錄載入音訊檔案，並將其轉換為 ComfyUI 中其他音訊節點可處理的格式。此節點會讀取音訊檔案，並擷取波形資料與取樣率，供後續音訊處理任務使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `音訊` | 從輸入目錄載入的音訊檔案 | AUDIO | 是 | 輸入目錄中所有支援的音訊與視訊檔案 |

**注意：** 此節點僅接受存在於 ComfyUI 輸入目錄中的音訊與視訊檔案。檔案必須存在且可存取，才能成功載入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `AUDIO` | 包含波形與取樣率資訊的音訊資料 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a7fe63cbbb3a854359189e8685936a2b8b855e22c3c282fc77affacf640af010`
