> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/zh-TW.md)

LTXV 參考音訊節點用於音訊生成中的說話者身份轉移。它將參考音訊片段編碼到模型的條件輸入中，使生成的音訊能夠採用說話者的聲音特徵。它還可以應用身份引導，執行額外的處理步驟以增強說話者身份效果。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 將套用身份引導修補的模型。 |
| `positive` | CONDITIONING | 是 | - | 正向條件輸入。 |
| `negative` | CONDITIONING | 是 | - | 負向條件輸入。 |
| `reference_audio` | AUDIO | 是 | - | 用於轉移說話者身份的參考音訊片段。建議約 5 秒（訓練時長）。較短或較長的片段可能會降低聲音身份轉移的品質。 |
| `audio_vae` | VAE | 是 | - | 用於編碼參考音訊的 LTXV 音訊 VAE。 |
| `identity_guidance_scale` | FLOAT | 否 | 0.0 - 100.0 | 身份引導的強度。每個步驟會執行一次不含參考的額外前向傳遞，以增強說話者身份。設為 0 以停用（無額外傳遞）。(預設值: 3.0) |
| `start_percent` | FLOAT | 否 | 0.0 - 1.0 | 身份引導生效的 sigma 範圍起始點。(預設值: 0.0) |
| `end_percent` | FLOAT | 否 | 0.0 - 1.0 | 身份引導生效的 sigma 範圍結束點。(預設值: 1.0) |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用身份引導函數修補的模型。 |
| `positive` | CONDITIONING | 正向條件，現在包含編碼後的參考音訊資料。 |
| `negative` | CONDITIONING | 負向條件，現在包含編碼後的參考音訊資料。 |