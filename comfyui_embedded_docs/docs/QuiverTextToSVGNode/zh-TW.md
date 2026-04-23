> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/zh-TW.md)

Quiver Text to SVG 節點使用 Quiver AI 的模型，根據文字描述生成可縮放向量圖形（SVG）影像。您可以選擇性地提供參考影像和風格指示來引導生成過程。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 期望 SVG 輸出的文字描述。這是生成內容的主要指示。 |
| `instructions` | STRING | 否 | N/A | 額外的風格或格式指引。這是一個可選的高級參數。 |
| `reference_images` | IMAGE | 否 | N/A | 最多 4 張用於引導生成的參考影像。此為可選輸入。 |
| `model` | COMBO | 是 | 提供多個選項 | 用於 SVG 生成的模型。可用選項由 Quiver API 決定。 |
| `seed` | INT | 是 | 0 至 2147483647 | 決定節點是否應重新執行的種子值；無論種子為何，實際結果均為非確定性。預設值：0。 |

**注意：** `reference_images` 輸入最多接受 4 張影像。如果提供更多，節點將引發錯誤。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `SVG` | SVG | 生成的可縮放向量圖形（SVG）影像。 |