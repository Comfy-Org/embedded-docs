> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/zh-TW.md)

此節點為 Kandinsky 5 模型準備文字提示。它接收兩個獨立的文字輸入，使用提供的 CLIP 模型對其進行標記化，並將它們組合成單一的條件輸出。此輸出用於引導圖像生成過程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | | 用於標記化和編碼文字提示的 CLIP 模型。 |
| `clip_l` | STRING | 是 | | 主要文字提示。此輸入支援多行文字和動態提示。 |
| `qwen25_7b` | STRING | 是 | | 次要文字提示。此輸入支援多行文字和動態提示。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 由兩個文字提示生成的組合條件資料，準備好輸入到 Kandinsky 5 模型以進行圖像生成。 |
