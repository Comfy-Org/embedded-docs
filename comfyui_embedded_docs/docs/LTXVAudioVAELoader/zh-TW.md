# LTXV 音訊 VAE 載入器

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `ckpt_name` | 要載入的音訊 VAE 檢查點。這是一個下拉式清單，會填入您在 ComfyUI `checkpoints` 目錄中找到的所有檔案。 | COMBO | 是 | `checkpoints` 資料夾中的所有檔案（動態填入）。<br>範例：`"audio_vae.safetensors"` |

注意：如果找不到選取的檢查點檔案，或該檔案不包含有效的音訊 VAE，節點將會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `Audio VAE` | 已載入的音訊變分自編碼器模型，可連接到其他音訊處理節點。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
