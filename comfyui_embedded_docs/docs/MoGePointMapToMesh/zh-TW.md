# MoGe 點雲轉網格

此節點將 MoGe 點圖轉換為 3D 網格。它接收由 MoGe 深度估計節點產生的幾何資料，並將其三角化為帶有 UV 座標及可選紋理的網格。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 包含點圖、深度以及可選的來源影像的 MoGe 幾何資料。 | MOGE_GEOMETRY | 是 | N/A |
| `batch_index` | 選擇批次 MoGe 幾何資料中要進行網格化的影像。每張影像的頂點數不同，因此批次無法堆疊成單一 MESH（預設值：0）。 | INT | 是 | 0 至 4096 |
| `decimation` | 頂點步長；1 = 完整解析度（預設值：1）。 | INT | 是 | 1 至 8 |
| `discontinuity_threshold` | 丟棄 3x3 深度跨度超過此比例的像素。0 = 關閉（預設值：0.04）。 | FLOAT | 是 | 0.0 至 1.0 |
| `texture` | 將來源影像作為 baseColor 紋理傳遞（預設值：True）。 | BOOLEAN | 是 | True/False |

注意：`batch_index` 必須小於輸入 `moge_geometry` 的批次大小；選取超出範圍的索引會引發錯誤。如果三角化產生空網格，節點會引發錯誤；將 `discontinuity_threshold` 設為 0 可停用深度不連續濾波器。輸出網格會轉換為 glTF 座標：透視 MoGe 資料（X 向右、Y 向下、Z 向前）會翻轉以符合 glTF（Y 向上、Z 向後），全景資料則會相應旋轉。啟用 `texture` 時，會使用 `moge_geometry` 中的來源影像作為 baseColor 紋理。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MESH` | 具有頂點、面、UV 座標，以及來自來源影像的可選 baseColor 紋理的 3D 網格。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
