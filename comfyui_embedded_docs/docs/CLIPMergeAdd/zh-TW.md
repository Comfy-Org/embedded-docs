> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/zh-TW.md)

CLIPMergeAdd 節點透過將第二個 CLIP 模型中的修補程式添加到第一個模型來合併兩個 CLIP 模型。它會建立第一個 CLIP 模型的副本，並選擇性地整合第二個模型中的關鍵修補程式，排除位置 ID 和 logit 縮放參數。這讓您可以在保留基礎模型結構的同時合併 CLIP 模型元件。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | 是 | - | 將被克隆並作為合併基礎的 CLIP 基礎模型 |
| `clip2` | CLIP | 是 | - | 提供要添加到基礎模型中的關鍵修補程式的次要 CLIP 模型 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CLIP` | CLIP | 包含基礎模型結構並添加了次要模型修補程式的合併 CLIP 模型 |