# MoGe 全景推論

## 概述

此節點對等距柱狀投影全景影像執行深度估測。它將全景影像分割為 12 個透視視圖，對每個視圖執行 MoGe 深度估測模型，再將各視圖的結果合併回覆蓋整個全景的單一深度圖。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `moge_model` | 用於推論的 MoGe 模型。 | MOGE_MODEL | 是 |  |
| `image` | 等距柱狀投影全景（任何長寬比）。此節點僅接受單一影像；傳入影像批次會引發錯誤。僅使用前 3 個顏色通道（RGB）。 | IMAGE | 是 |  |
| `resolution_level` | 每個視圖的細節（0 = 最快，9 = 最詳細）（預設值：9）。 | INT | 是 | 0 到 9 |
| `split_resolution` | 每個透視分割的解析度（預設值：512）。 | INT | 是 | 256 到 1024 |
| `merge_resolution` | 合併後的等距柱狀深度圖的長邊解析度（預設值：1920）。 | INT | 是 | 256 到 8192 |
| `batch_size` | 每個推論批次的視圖數（總共 12 個分割）（預設值：4）。 | INT | 是 | 1 到 12 |

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `moge_geometry` | 包含估計幾何資訊的字典：`points`（3D 點雲）、`depth`（深度圖）、`mask`（有效區域遮罩）以及 `image`（輸入影像）。 | MOGE_GEOMETRY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
