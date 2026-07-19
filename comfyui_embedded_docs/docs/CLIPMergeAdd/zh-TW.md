# CLIPMergeAdd

CLIPMergeAdd 節點透過將第二個 CLIP 模型的修補程式（patches）添加到第一個模型，來組合兩個 CLIP 模型。它會建立第一個 CLIP 模型的副本，並選擇性地納入第二個模型的關鍵修補程式，排除位置 ID（position IDs）與 logit 尺度參數（logit scale parameters）。這讓您能夠在保留基礎模型結構的同時，合併 CLIP 模型的元件。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip1` | 將被複製並作為合併基礎的基底 CLIP 模型 | CLIP | 是 | - |
| `clip2` | 提供要添加到基底模型之關鍵修補程式的次要 CLIP 模型 | CLIP | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CLIP` | 一個合併後的 CLIP 模型，包含基底模型的結構，並添加了來自次要模型的修補程式 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f212c2750f317ad51516a10a1a03a838b75bc878333381348d5eb388a2faf516`
