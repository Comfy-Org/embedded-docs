> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/zh-TW.md)

此節點儲存一張圖片及其權重值，供 Luma 生成圖片節點使用。它建立一個參考鏈，可傳遞給其他 Luma 節點以影響圖片生成。此節點可以啟動新的參考鏈，或將參考添加到現有參考鏈中。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `影像` | IMAGE | 是 | - | 用作參考的圖片。 |
| `權重` | FLOAT | 是 | 0.0 - 1.0 | 圖片參考的權重（預設值：1.0）。 |
| `luma_ref` | LUMA_REF | 否 | - | 可選的現有 Luma 參考鏈，用於添加參考。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `luma_ref` | LUMA_REF | 包含圖片及權重的 Luma 參考鏈。 |

---
**Source fingerprint (SHA-256):** `1ad653f0ad7c56702f607ebc3c3d117196295e4e3b044a2c6f1aa3db18869a40`
