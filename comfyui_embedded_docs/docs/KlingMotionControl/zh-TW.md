> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/zh-TW.md)

Kling Motion Control 節點透過將參考影片中的動作、表情和攝影機運動應用到由參考圖像和文字提示定義的角色上，從而生成影片。它允許您控制角色的最終朝向是來自參考影片還是參考圖像。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 期望影片的文字描述。最大長度為 2500 個字元。 |
| `reference_image` | IMAGE | 是 | N/A | 要進行動畫處理的角色圖像。最小尺寸為 340x340 像素。長寬比必須介於 1:2.5 到 2.5:1 之間。 |
| `reference_video` | VIDEO | 是 | N/A | 用於驅動角色動作和表情的動作參考影片。最小尺寸為 340x340 像素，最大尺寸為 3850x3850 像素。持續時間限制取決於 `character_orientation` 設定。 |
| `keep_original_sound` | BOOLEAN | 否 | N/A | 決定是否在輸出中保留參考影片的原始音訊。預設值為 `True`。 |
| `character_orientation` | COMBO | 否 | `"video"`<br>`"image"` | 控制角色的朝向/方向來源。`"video"`：動作、表情、攝影機移動和朝向都遵循動作參考影片。`"image"`：動作和表情遵循動作參考影片，但角色朝向與參考圖像匹配。 |
| `mode` | COMBO | 否 | `"pro"`<br>`"std"` | 要使用的生成模式。 |

**限制條件：**

* 當 `character_orientation` 設定為 `"video"` 時，`reference_video` 的持續時間必須介於 3 到 30 秒之間。
* 當 `character_orientation` 設定為 `"image"` 時，`reference_video` 的持續時間必須介於 3 到 10 秒之間。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片，其中角色執行了來自參考影片的動作。 |
