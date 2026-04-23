> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/zh-TW.md)

Reve Image Create 節點使用 Reve AI 模型，根據文字描述生成圖像。它會將文字提示發送到 Reve API 並返回生成的圖像。您可以控制圖像的長寬比，並應用可選的後處理效果，例如放大。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 期望圖像的文字描述。最多 2560 個字元。 |
| `model` | COMBO | 是 | `"reve-create@20250915"`<br>`"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | 用於生成的模型版本和長寬比。第一個選項選擇模型，後續選項定義圖像的長寬比。 |
| `upscale` | COMBO | 否 | `"disabled"`<br>`"enabled"` | 啟用或停用放大後處理步驟。啟用時，您還必須選擇一個放大倍率。 |
| `upscale_factor` | COMBO | 否 | `2`<br>`3`<br>`4` | 提高圖像解析度的倍率。此參數僅在 `upscale` 設置為 `"enabled"` 時生效。 |
| `remove_background` | BOOLEAN | 否 | N/A | 啟用時，對生成的圖像應用背景移除後處理步驟。 |
| `seed` | INT | 否 | 0 至 2147483647 | 控制節點是否應重新執行的種子值。注意：無論種子值為何，結果都是非確定性的。預設值：0。 |

**注意：** `upscale_factor` 參數依賴於 `upscale` 參數設置為 `"enabled"`。`seed` 參數不保證輸出是確定性的。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 由 Reve 模型根據輸入提示生成的圖像。 |