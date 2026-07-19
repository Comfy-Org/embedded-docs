# CLIPAdd

## 概述

CLIPAdd 節點透過合併兩個 CLIP 模型的關鍵修補程式（key patches）來組合它們。它會建立第一個 CLIP 模型的副本，然後從第二個模型中添加大部分關鍵修補程式，排除位置 ID（position IDs）和 logit 縮放參數（logit scale parameters）。這讓您能夠在保留第一個模型結構的同時，融合來自不同 CLIP 模型的特徵。

## 輸入

| 參數 | 描述 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `clip1` | 作為合併基礎的主要 CLIP 模型 | CLIP | 必要 | - | - |
| `clip2` | 提供要添加之額外修補程式的次要 CLIP 模型 | CLIP | 必要 | - | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CLIP` | 傳回一個合併後的 CLIP 模型，結合了兩個輸入模型的特徵 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/zh-TW.md)

---
**Source fingerprint (SHA-256):** `935d450d25d90dc623e3f2b39b251359a9066c9e1fdd2a70384982fb26a21864`
