# 將 DA3 幾何轉換為網格

此節點會將 DA3_GEOMETRY 封包轉換為 3D 網格，方式是將深度圖反投影，並對產生的點雲進行三角化。它會處理批次中的單一影像，並產生適合 3D 渲染的帶紋理或無紋理網格。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | 包含深度圖、選填的信心圖、選填的天空圖以及來源影像的 DA3_GEOMETRY 封包 | DA3_GEOMETRY | 是 | - |
| `batch_index` | 要轉換批次中的哪一張影像。每張影像的頂點數量不同，因此批次無法堆疊（預設：0）。必須小於輸入幾何的批次大小，否則會引發錯誤 | INT | 是 | 0 至 4096 |
| `decimation` | 頂點步幅。1 = 完整解析度，2 = 一半，依此類推（預設：1） | INT | 是 | 1 至 8 |
| `discontinuity_threshold` | 捨棄 3x3 深度跨度超過此比例的三角形。0 = 關閉（預設：0.04） | FLOAT | 是 | 0.0 至 1.0 |
| `confidence_threshold` | 排除每張影像正規化信心低於此值的像素。0 = 保留全部，1 = 僅保留信心最高的單一像素。當幾何具有信心圖（Small/Base 模型）時使用（預設：0.1） | FLOAT | 是 | 0.0 至 1.0 |
| `use_sky_mask` | 從網格中排除天空機率像素（sky >= 0.5）。當幾何具有天空圖（Mono/Metric 模型）時使用（預設：True） | BOOLEAN | 是 | True or False |
| `texture` | 使用來源影像作為基礎顏色紋理（預設：True） | BOOLEAN | 是 | True or False |

具有非有限、零或負深度值的像素一律會從網格中排除。若產生的網格為空，則會引發錯誤；錯誤訊息會建議提高 `discontinuity_threshold`、降低 `confidence_threshold`，或停用 `use_sky_mask`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MESH` | 具有頂點、面、UV 座標以及選填紋理的三角化 3D 網格 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`
