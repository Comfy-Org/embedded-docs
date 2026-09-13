# CLIPMergeAdd

CLIPMergeAdd 節點會將來自第二個模型的補丁加入第一個模型，從而合併兩個 CLIP 模型。它會建立第一個 CLIP 模型的副本，並選擇性地納入第二個模型的關鍵補丁，同時排除 position IDs 與 logit scale 參數。這讓您可以在合併 CLIP 模型元件的同時，保留基礎模型的結構。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip1` | 將被複製並用作合併基礎的基礎 CLIP 模型 | CLIP | 是 | - |
| `clip2` | 提供關鍵補丁以加入基礎模型的次要 CLIP 模型 | CLIP | 是 | - |

來自 `clip2` 且以 `.position_ids` 或 `.logit_scale` 結尾的鍵會被略過，因此這些參數會保留 `clip1` 的值。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CLIP` | 合併後的 CLIP 模型，包含基礎模型結構以及來自次要模型的新增補丁 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
