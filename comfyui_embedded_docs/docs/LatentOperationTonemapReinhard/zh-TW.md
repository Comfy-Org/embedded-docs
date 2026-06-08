## 概述

LatentOperationTonemapReinhard 節點將 Reinhard 色調映射應用於潛在向量。此技術透過基於平均值和標準差的統計方法來正規化潛在向量並調整其幅度，其強度由乘數參數控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `乘數` | 控制色調映射效果的強度（預設值：1.0） | FLOAT | 否 | 0.0 至 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `operation` | 回傳一個可應用於潛在向量的色調映射操作 | LATENT_OPERATION |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/zh-TW.md)

---
**Source fingerprint (SHA-256):** `70c04eaef06b749392a0c65f3d1267e52484f7cf956f87173d10ad935afcf98c`
