> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/zh-TW.md)

Moonvalley Marey 影片轉影片節點能根據文字描述將輸入影片轉換為新的影片。它使用 Moonvalley API 來生成符合您提示詞的影片，同時保留原始影片的動作或姿勢特徵。您可以透過文字提示詞和各種生成參數來控制輸出影片的風格和內容。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 描述要生成的影片（支援多行輸入） |
| `negative_prompt` | STRING | 否 | - | 負向提示詞文字（預設值：包含廣泛的負面描述詞列表） |
| `seed` | INT | 是 | 0-4294967295 | 隨機種子值（預設值：9） |
| `video` | VIDEO | 是 | - | 用於生成輸出影片的參考影片。長度必須至少為 5 秒。超過 5 秒的影片將被自動修剪。僅支援 MP4 格式。 |
| `control_type` | COMBO | 否 | "Motion Transfer"<br>"Pose Transfer" | 控制類型選擇（預設值："Motion Transfer"） |
| `motion_intensity` | INT | 否 | 0-100 | 僅在 control_type 為 'Motion Transfer' 時使用（預設值：100） |
| `steps` | INT | 是 | 1-100 | 推理步驟數（預設值：33） |

**注意：** `motion_intensity` 參數僅在 `control_type` 設定為 "Motion Transfer" 時生效。使用 "Pose Transfer" 時，此參數將被忽略。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片輸出 |