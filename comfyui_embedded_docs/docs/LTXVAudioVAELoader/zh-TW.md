## 概述

LTXV 音訊 VAE 載入器節點可從檢查點檔案載入預先訓練的音訊變分自編碼器（VAE）模型。它會讀取指定的檢查點，載入其權重與元數據，並準備好模型以供在 ComfyUI 中的音訊生成或處理工作流程中使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `ckpt_name` | 要載入的音訊 VAE 檢查點。這是一個下拉選單，會列出您 ComfyUI `checkpoints` 目錄中找到的所有檔案。 | STRING | 是 | `checkpoints` 資料夾中的所有檔案。<br>*範例：`"audio_vae.safetensors"`* |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| 音訊 VAE | 已載入的音訊變分自編碼器模型，可準備連接到其他音訊處理節點。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `44e79f694eed796a83f3ac25c56946baaa12b016568bd8824eb179bf79e50588`
