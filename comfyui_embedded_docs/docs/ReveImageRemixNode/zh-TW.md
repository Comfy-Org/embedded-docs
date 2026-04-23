> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/zh-TW.md)

Reve Image Remix 節點使用 Reve API 來生成新圖像。它將一個或多個參考圖像與文字提示結合，根據提供的描述創建一個新的、經過混搭的圖像。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `reference_images` | IMAGE | 是 | 1 到 6 張圖像 | 用作混搭基礎的一個或多個參考圖像。您可以添加 1 到 6 張圖像。 |
| `prompt` | STRING | 是 | 1 到 2560 個字元 | 對期望圖像的文字描述。您可以包含 XML `<img>` 標籤，透過索引來引用特定圖像（例如 `<img>0</img>`、`<img>1</img>`）。 |
| `model` | COMBO | 是 | `reve-remix@20250915`<br>`reve-remix-fast@20251030` | 用於混搭的模型版本。每個模型選項都包含可配置的長寬比和測試時縮放設定。 |
| `upscale` | COMBO | 否 | `"disabled"`<br>`"enabled"` | 控制是否對生成的圖像進行放大。啟用後，您可以選擇放大倍率。 |
| `remove_background` | BOOLEAN | 否 | `true`<br>`false` | 啟用時，會嘗試移除生成圖像的背景。 |
| `seed` | INT | 否 | 0 到 2147483647 | 種子值。更改此值將導致節點重新運行，但結果是非確定性的。（預設值：0） |

**注意：** `model` 參數是一個動態組合框，包含 `aspect_ratio`（例如 "auto"、"16:9"、"1:1"）和 `test_time_scaling` 的嵌套設定。當 `upscale` 參數設為 "enabled" 時，會顯示一個嵌套的 `upscale_factor` 設定。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 由 Reve 混搭流程生成的新圖像。 |