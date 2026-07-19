# Luma 參考

此節點儲存一張圖片及其權重值，供 Luma 生成圖片節點使用。它建立一個參考鏈，可傳遞給其他 Luma 節點以影響圖片生成。此節點可以啟動新的參考鏈，或將參考添加到現有參考鏈中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 用作參考的圖片。 | IMAGE | 是 | - |
| `權重` | 圖片參考的權重（預設值：1.0）。 | FLOAT | 是 | 0.0 - 1.0 |
| `luma_ref` | 可選的現有 Luma 參考鏈，用於添加參考。 | LUMA_REF | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `luma_ref` | 包含圖片及權重的 Luma 參考鏈。 | LUMA_REF |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1ad653f0ad7c56702f607ebc3c3d117196295e4e3b044a2c6f1aa3db18869a40`
