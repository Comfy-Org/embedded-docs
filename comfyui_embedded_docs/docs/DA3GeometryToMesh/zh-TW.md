# 將 DA3 幾何資料轉換為網格

此節點透過反投影深度圖並對產生的點雲進行三角化，將 DA3_GEOMETRY 資料包轉換為 3D 網格。它處理批次中的單一影像，並產生適合 3D 渲染的紋理或無紋理網格。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | 包含深度圖、可選置信度圖、可選天空圖及來源影像的 DA3_GEOMETRY 資料包 | DA3_GEOMETRY | 是 | - |
| `batch_index` | 要轉換的批次影像索引。每張影像的頂點數量不同，因此批次無法堆疊（預設值：0） | INT | 是 | 0 至 4096 |
| `decimation` | 頂點步長。1 = 完整解析度，2 = 一半解析度，以此類推（預設值：1） | INT | 是 | 1 至 8 |
| `discontinuity_threshold` | 丟棄 3x3 深度跨度超過此比例的三角形。0 = 關閉（預設值：0.04） | FLOAT | 是 | 0.0 至 1.0 |
| `confidence_threshold` | 排除每張影像正規化置信度低於此值的像素。0 = 保留全部，1 = 僅保留置信度最高的單一像素。當幾何資料包含置信度圖時使用（Small/Base 模型）（預設值：0.1） | FLOAT | 是 | 0.0 至 1.0 |
| `use_sky_mask` | 從網格中排除天空機率像素（天空 >= 0.5）。當幾何資料包含天空圖時使用（Mono/Metric 模型）（預設值：True） | BOOLEAN | 是 | True 或 False |
| `texture` | 使用來源影像作為基底顏色紋理（預設值：True） | BOOLEAN | 是 | True 或 False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MESH` | 包含頂點、面、UV 座標及可選紋理的三角化 3D 網格 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`
