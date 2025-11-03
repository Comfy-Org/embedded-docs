> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/zh-TW.md)

Kling 單圖影片特效節點基於單一參考圖像創建具有不同特殊效果的影片。它應用各種視覺效果和場景，將靜態圖像轉換為動態影片內容。該節點支援不同的特效場景、模型選項和影片時長，以實現所需的視覺效果。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 參考圖像。URL 或 Base64 編碼字串（無需 data:image 前綴）。檔案大小不得超過 10MB，解析度不低於 300*300px，長寬比介於 1:2.5 ~ 2.5:1 之間 |
| `effect_scene` | COMBO | 是 | 來自 KlingSingleImageEffectsScene 的選項 | 應用於影片生成的特殊效果場景類型 |
| `model_name` | COMBO | 是 | 來自 KlingSingleImageEffectModelName 的選項 | 用於生成影片特效的特定模型 |
| `duration` | COMBO | 是 | 來自 KlingVideoGenDuration 的選項 | 生成影片的長度 |

**注意：** `effect_scene`、`model_name` 和 `duration` 的具體選項由其對應枚舉類（KlingSingleImageEffectsScene、KlingSingleImageEffectModelName 和 KlingVideoGenDuration）中的可用值決定。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 應用特效後生成的影片 |
| `video_id` | STRING | 生成影片的唯一識別碼 |
| `duration` | STRING | 生成影片的時長 |