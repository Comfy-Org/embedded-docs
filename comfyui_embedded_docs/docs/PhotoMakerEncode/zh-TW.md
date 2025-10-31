> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/zh-TW.md)

PhotoMakerEncode 節點處理影像和文字，為 AI 影像生成產生條件資料。它接收參考影像和文字提示，然後建立可用於根據參考影像的視覺特徵來引導影像生成的嵌入向量。此節點特別會在文字中尋找 "photomaker" 標記，以決定在何處應用基於影像的條件化。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `photomaker` | PHOTOMAKER | 是 | - | 用於處理影像和產生嵌入向量的 PhotoMaker 模型 |
| `影像` | IMAGE | 是 | - | 提供條件化視覺特徵的參考影像 |
| `clip` | CLIP | 是 | - | 用於文字標記化和編碼的 CLIP 模型 |
| `文字` | STRING | 是 | - | 用於產生條件化的文字提示（預設值："photograph of photomaker"） |

**注意：** 當文字中包含 "photomaker" 一詞時，節點會在提示詞的該位置應用基於影像的條件化。如果在文字中找不到 "photomaker"，節點將產生沒有影像影響的標準文字條件化。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含影像和文字嵌入向量的條件化資料，用於引導影像生成 |