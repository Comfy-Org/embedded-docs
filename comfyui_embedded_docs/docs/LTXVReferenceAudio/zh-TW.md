## 概述

LTXV 參考音訊節點用於音訊生成中的說話者身份轉移。它將參考音訊片段編碼為模型的條件輸入，使生成的音訊能夠採用該說話者的聲音特徵。它還可以應用身份引導，透過執行額外的處理步驟來增強說話者身份效果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將要套用身份引導修補的模型。 | MODEL | 是 | - |
| `positive` | 正向條件輸入。 | CONDITIONING | 是 | - |
| `negative` | 負向條件輸入。 | CONDITIONING | 是 | - |
| `reference_audio` | 要轉移說話者身份的參考音訊片段。建議長度約 5 秒（訓練時長）。較短或較長的片段可能會降低語音身份轉移效果。 | AUDIO | 是 | - |
| `audio_vae` | 用於編碼參考音訊的 LTXV 音訊 VAE。 | VAE | 是 | - |
| `identity_guidance_scale` | 身份引導的強度。在每個步驟中執行一次額外的正向傳遞（不含參考音訊），以增強說話者身份效果。設為 0 可停用此功能（不執行額外傳遞）。（預設值：3.0） | FLOAT | 否 | 0.0 - 100.0 |
| `start_percent` | 身份引導生效的 sigma 範圍起始點。（預設值：0.0） | FLOAT | 否 | 0.0 - 1.0 |
| `end_percent` | 身份引導生效的 sigma 範圍結束點。（預設值：1.0） | FLOAT | 否 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用身份引導功能的模型。 | MODEL |
| `positive` | 正向條件，現已包含編碼後的參考音訊資料。 | CONDITIONING |
| `negative` | 負向條件，現已包含編碼後的參考音訊資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b87fb135ba8e752f4114cb47152503b0ec548eefcaa03f99f1cbdda6664874c`
