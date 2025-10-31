> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/zh-TW.md)

此節點保存一個影像和權重值，供 Luma Generate Image 節點使用。它建立一個參考鏈，可以傳遞給其他 Luma 節點以影響影像生成。該節點可以開始一個新的參考鏈，也可以添加到現有的參考鏈中。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `影像` | IMAGE | 是 | - | 用作參考的影像。 |
| `權重` | FLOAT | 是 | 0.0 - 1.0 | 影像參考的權重（預設值：1.0）。 |
| `luma_ref` | LUMA_REF | 否 | - | 可選的現有 Luma 參考鏈，用於添加至此鏈。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `luma_ref` | LUMA_REF | 包含影像和權重的 Luma 參考鏈。 |