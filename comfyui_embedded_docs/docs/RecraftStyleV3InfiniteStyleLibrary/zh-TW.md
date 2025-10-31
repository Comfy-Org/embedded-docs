> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/zh-TW.md)

此節點允許您使用預先存在的 UUID 從 Recraft 的 Infinite Style Library 中選擇樣式。它會根據提供的樣式識別碼檢索樣式資訊，並返回以供其他 Recraft 節點使用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `style_id` | STRING | 是 | 任何有效的 UUID | Infinite Style Library 中樣式的 UUID。 |

**注意：** `style_id` 輸入不能為空。如果提供空字串，節點將引發異常。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | 從 Recraft 的 Infinite Style Library 中選擇的樣式物件 |