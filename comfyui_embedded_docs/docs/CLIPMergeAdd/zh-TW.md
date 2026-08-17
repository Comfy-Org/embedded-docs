# CLIPMergeAdd

CLIPMergeAdd 節點透過將第二個模型的補丁添加到第一個模型，來組合兩個 CLIP 模型。它會建立第一個 CLIP 模型的副本，並選擇性地納入第二個模型的關鍵補丁，排除位置 ID（position IDs）與 logit scale 參數。這讓您能在保留基礎模型結構的情況下，合併 CLIP 模型元件。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip1` | 將被複製並作為合併基礎的基礎 CLIP 模型 | CLIP | 是 | - |
| `clip2` | 提供要添加到基礎模型之關鍵補丁的第二個 CLIP 模型 | CLIP | 是 | - |

注意：來自 `clip2` 的關鍵補丁會以 1.0 的強度添加。結尾為 `.position_ids` 或 `.logit_scale` 的鍵值會從合併中排除。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CLIP` | 一個包含基礎模型結構，並添加了來自第二個模型之補丁的合併 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
