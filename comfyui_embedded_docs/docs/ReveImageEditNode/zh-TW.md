> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/zh-TW.md)

Reve Image Edit 節點讓您能夠根據文字描述修改現有圖像。它使用 Reve API 來解讀您的指令，並將要求的變更應用到您提供的圖像上。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要編輯的圖像。 |
| `edit_instruction` | STRING | 是 | - | 描述如何編輯圖像的文字說明。最多 2560 個字元。 |
| `model` | MODEL | 是 | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"`<br>`"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | 用於編輯的模型版本。選項包含特定的模型版本和長寬比設定。 |
| `upscale` | COMBO | 否 | `"disabled"`<br>`"enabled"` | 控制是否對生成的圖像進行放大。 |
| `upscale_factor` | FLOAT | 否 | - | 當啟用放大時，圖像的放大倍率。 |
| `remove_background` | BOOLEAN | 否 | - | 控制是否從生成的圖像中移除背景。 |
| `seed` | INT | 否 | 0 到 2147483647 | 種子值控制節點是否應重新執行；無論種子值為何，結果都是非確定性的。(預設值: 0) |

**注意：** 僅當 `upscale` 參數設定為 `"enabled"` 時，`upscale_factor` 參數才相關。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 根據指令生成的已編輯圖像。 |