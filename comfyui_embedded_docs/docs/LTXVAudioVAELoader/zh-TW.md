# LTXV 音訊 VAE 載入器

LTXV Audio VAE Loader 節點會從檢查點檔案載入預先訓練的音訊變分自編碼器（VAE）模型。它會讀取指定的檢查點、載入其權重與中繼資料，並準備好模型以供 ComfyUI 內部的音訊生成或處理工作流程使用。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `ckpt_name` | 要載入的音訊 VAE 檢查點。這是一個下拉式清單，會列出 ComfyUI `checkpoints` 目錄中找到的所有檔案。 | COMBO | 是 | `checkpoints` 資料夾中的所有檔案。清單在執行時生成。 |

所選檔案必須是有效的 LTXV 音訊 VAE 檢查點。節點只會保留檔案中的音訊 VAE 和聲碼器權重；如果載入的模型不是有效的 VAE，則會引發錯誤。

## 輸出

| 輸出名 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| Audio VAE | 已載入的音訊變分自編碼器模型，可連接到其他音訊處理節點。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
