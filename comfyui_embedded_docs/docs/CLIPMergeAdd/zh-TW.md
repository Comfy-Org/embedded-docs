# CLIPMergeAdd

CLIPMergeAdd 節點透過將第二個 CLIP 模型中的補丁新增至第一個模型，來組合兩個 CLIP 模型。它會建立第一個 CLIP 模型的副本，並選擇性地納入第二個模型的關鍵補丁，排除位置 ID 與 logit scale 參數。這可讓您在保留基礎模型結構的前提下，合併 CLIP 模型元件。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip1` | 作為合併基礎的基底 CLIP 模型，會先被複製 | CLIP | 是 | - |
| `clip2` | 提供要新增至基礎模型之關鍵補丁的第二個 CLIP 模型 | CLIP | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CLIP` | 包含基礎模型結構並加入第二個模型之補丁的合併 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
