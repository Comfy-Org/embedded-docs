> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh-TW.md)

此節點使用 Seedance 2.0 AI 模型，根據您的文字提示和提供的參考素材來創建、編輯或擴展影片。它可以使用圖像、影片和音訊作為參考來引導生成過程，支援影片編輯和擴展等任務。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | 要使用的 AI 模型。Seedance 2.0 用於最高品質，而 Seedance 2.0 Fast 則針對速度進行了優化。選擇模型後，會顯示 `prompt`、`resolution`、`duration`、`ratio`、`generate_audio` 等額外必填輸入，以及 `reference_images`、`reference_videos`、`reference_audios`、`reference_assets` 和 `auto_downscale` 等可選輸入。 |
| `seed` | INT | 否 | 0 至 2147483647 | 用於控制節點是否應重新執行的數字。無論種子值為何，結果都是非確定性的（預設值：0）。 |
| `watermark` | BOOLEAN | 否 | `True` / `False` | 是否在生成的影片中添加浮水印（預設值：False）。 |

**重要限制：**
*   節點需要至少一個參考圖像或影片（透過 `reference_images`、`reference_videos` 或 `reference_assets` 輸入提供）才能運作。
*   每個參考影片的長度必須至少為 1.8 秒。所有參考影片的總時長不能超過 15.1 秒。
*   每個參考音訊片段的長度必須至少為 1.8 秒。所有參考音訊的總時長不能超過 15.1 秒。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案。 |