> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/zh-TW.md)

Ideogram V3 節點使用 Ideogram V3 模型生成影像。它支援基於文字提示的常規影像生成，以及在提供影像和遮罩時的影像編輯功能。該節點提供多種控制選項，包括長寬比、解析度、生成速度以及可選的角色參考影像。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 用於影像生成或編輯的提示文字 (預設: 空值) |
| `image` | IMAGE | 否 | - | 用於影像編輯的參考影像 (可選) |
| `mask` | MASK | 否 | - | 用於局部重繪的遮罩 (可選，白色區域將被替換) |
| `aspect_ratio` | COMBO | 否 | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | 影像生成的長寬比。如果解析度未設定為 Auto 則忽略此設定 (預設: "1:1") |
| `resolution` | COMBO | 否 | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | 影像生成的解析度。如果未設定為 Auto，將覆蓋 aspect_ratio 設定 (預設: "Auto") |
| `magic_prompt_option` | COMBO | 否 | "AUTO"<br>"ON"<br>"OFF" | 決定是否在生成過程中使用 MagicPrompt (預設: "AUTO") |
| `seed` | INT | 否 | 0-2147483647 | 生成隨機數的種子值 (預設: 0) |
| `num_images` | INT | 否 | 1-8 | 要生成的影像數量 (預設: 1) |
| `rendering_speed` | COMBO | 否 | "DEFAULT"<br>"TURBO"<br>"QUALITY" | 控制生成速度與品質之間的平衡 (預設: "DEFAULT") |
| `character_image` | IMAGE | 否 | - | 用作角色參考的影像 |
| `character_mask` | MASK | 否 | - | 角色參考影像的遮罩 (可選) |

**參數限制條件:**

- 當同時提供 `image` 和 `mask` 時，節點將切換到編輯模式
- 如果僅提供 `image` 或 `mask` 其中一項，將會發生錯誤
- `character_mask` 需要同時存在 `character_image`
- 當 `resolution` 未設定為 "Auto" 時，`aspect_ratio` 參數將被忽略
- 在局部重繪過程中，遮罩中的白色區域將被替換
- 角色遮罩和角色影像必須具有相同尺寸

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | IMAGE | 生成或編輯後的影像 |