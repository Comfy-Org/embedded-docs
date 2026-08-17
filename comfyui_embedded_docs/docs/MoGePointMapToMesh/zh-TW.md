# MoGe 點雲轉網格

此節點將 MoGe 點圖轉換為 3D 網格。它接收由 MoGe 深度估計節點產生的幾何數據，並從中將一張影像三角化為帶有 UV 坐標和可選紋理的網格。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 包含點圖、深度，以及可選的來源影像的 MoGe 幾何數據。 | MOGE_GEOMETRY | 是 | N/A |
| `batch_index` | 要轉換為網格的批次 MoGe 幾何中的哪一張影像。每張影像的頂點數量不同，因此批次無法堆疊成單一 MESH（預設：0）。 | INT | 是 | 0 to 4096 |
| `decimation` | 頂點步幅；1 = 完整解析度（預設：1）。 | INT | 是 | 1 to 8 |
| `discontinuity_threshold` | 丟棄 3x3 深度跨度超過此比例的像素。0 = 關閉（預設：0.04）。 | FLOAT | 是 | 0.0 to 1.0 |
| `texture` | 將來源影像作為 baseColor 紋理傳遞（預設：True）。 | BOOLEAN | 是 | True/False |

注意：`batch_index` 必須小於所提供的 `moge_geometry` 的批次大小。輸入的幾何必須包含點數據，如果生成的網格為空，節點會回傳錯誤，建議設定 `discontinuity_threshold = 0`。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| MESH | 一個包含頂點、面、UV 坐標，以及可選的來源影像紋理的 3D 網格。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
