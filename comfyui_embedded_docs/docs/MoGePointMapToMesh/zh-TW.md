# MoGe 點雲轉網格

## 概述

此節點將 MoGe 點圖轉換為 3D 網格。它接收 MoGe 深度估計節點產生的幾何數據，並將其三角化為帶有 UV 座標和可選紋理的網格。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 包含點圖、深度以及可選原始影像的 MoGe 幾何數據。 | MOGE_GEOMETRY | 是 | 不適用 |
| `batch_index` | 指定批次 MoGe 幾何數據中的哪一張影像要轉換為網格。每張影像的頂點數量不同，因此批次無法合併為單一 MESH（預設值：0）。 | INT | 是 | 0 至 4096 |
| `decimation` | 頂點步長；1 = 完整解析度（預設值：1）。 | INT | 是 | 1 至 8 |
| `discontinuity_threshold` | 丟棄 3x3 深度範圍超過此比例的像素。0 = 關閉（預設值：0.04）。 | FLOAT | 是 | 0.0 至 1.0 |
| `texture` | 將原始影像作為 baseColor 紋理傳遞（預設值：True）。 | BOOLEAN | 是 | True/False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MESH` | 一個包含頂點、面、UV 座標以及來自原始影像的可選紋理的 3D 網格。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `65c43d64050d1c63d9efbb6c2bb96123f94c6d356d6341f2975537ac24ace29f`
