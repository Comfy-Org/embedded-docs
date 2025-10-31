> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAESave/zh-TW.md)

VAESave 節點專用於將 VAE 模型及其元資料（包括提示詞和額外的 PNG 資訊）儲存到指定的輸出目錄。它封裝了將模型狀態及相關資訊序列化至檔案的功能，便於訓練模型的保存與共享。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `vae`    | VAE      | 要儲存的 VAE 模型。此參數至關重要，代表需要被序列化並儲存狀態的模型。 |
| `檔名前綴` | STRING | 用於模型及其元資料儲存檔名的前綴。這有助於實現有序的儲存結構並方便模型檢索。 |

## 輸出結果

此節點沒有輸出類型。