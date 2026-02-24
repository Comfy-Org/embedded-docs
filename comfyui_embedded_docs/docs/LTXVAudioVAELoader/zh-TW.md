> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/zh-TW.md)

此節點從檢查點檔案載入預先訓練的音訊變分自編碼器（VAE）模型。它會讀取指定的檢查點，載入其權重與元資料，並準備好模型以供在 ComfyUI 內的音訊生成或處理工作流程中使用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | 是 | `checkpoints` 資料夾中的所有檔案。<br>*範例：`"audio_vae.safetensors"`* | 要載入的音訊 VAE 檢查點。這是一個下拉式選單，會列出您 ComfyUI `checkpoints` 目錄中找到的所有檔案。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `Audio VAE` | VAE | 已載入的音訊變分自編碼器模型，可連接至其他音訊處理節點。 |
