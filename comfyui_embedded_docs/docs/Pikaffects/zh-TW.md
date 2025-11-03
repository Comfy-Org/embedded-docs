> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/zh-TW.md)

Pikaffects 節點可生成帶有各種視覺效果的影片，這些效果會套用至輸入圖像。它使用 Pika 的影片生成 API，將靜態圖像轉換為具有特定效果（如融化、爆炸或漂浮）的動態影片。該節點需要 API 金鑰和驗證令牌才能存取 Pika 服務。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要套用 Pikaffect 效果的參考圖像。 |
| `pikaffect` | COMBO | 是 | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | 要套用至圖像的特定視覺效果（預設值："Cake-ify"）。 |
| `prompt_text` | STRING | 是 | - | 引導影片生成的文字描述。 |
| `negative_prompt` | STRING | 是 | - | 描述在生成影片中應避免內容的文字。 |
| `seed` | INT | 是 | 0 至 4294967295 | 用於可重現結果的隨機種子值。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 套用了 Pikaffect 效果後生成的影片。 |