> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/zh-TW.md)

此節點使用 Quiver AI 的向量化模型，將點陣圖像轉換為可縮放的向量圖形（SVG）。它會將圖像發送到外部 API 進行處理，並返回向量化的結果。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | N/A | 要進行向量化的輸入圖像。 |
| `auto_crop` | BOOLEAN | 否 | `True`<br>`False` | 自動裁剪至主要主體。這是一個進階參數（預設值：`False`）。 |
| `model` | DYNAMICCOMBO | 是 | 提供多個選項 | 用於 SVG 向量化的模型。選擇模型後，會顯示該模型特有的額外參數：`target_size`（正方形調整大小的目標像素，預設值：1024，範圍：128-4096）、`temperature`、`top_p` 和 `presence_penalty`。 |
| `seed` | INT | 否 | 0 至 2147483647 | 決定節點是否應重新執行的種子值；無論種子值為何，實際結果都是非確定性的。此參數具有「生成後控制」功能（預設值：0）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `SVG` | SVG | 向量化後的 SVG 輸出。 |