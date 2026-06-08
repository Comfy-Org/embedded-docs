## 概述

此節點對等距柱狀投影全景影像執行深度估計。其運作方式是將全景圖分割為 12 個透視視圖，對每個視圖執行 MoGe 深度估計模型，然後將結果合併回原始全景圖的單一完整深度圖。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_model` | 用於推論的 MoGe 模型。 | MOGE_MODEL | 是 |  |
| `image` | 等距柱狀投影全景影像（任何長寬比）。 | IMAGE | 是 |  |
| `resolution_level` | 每個視圖的細節等級。數值越高，深度圖越精細（預設值：9）。 | INT | 是 | 0 至 9 |
| `split_resolution` | 分割全景圖後，每個透視視圖的解析度（預設值：512）。 | INT | 是 | 256 至 1024 |
| `merge_resolution` | 最終合併後等距柱狀投影深度圖的長邊解析度（預設值：1920）。 | INT | 是 | 256 至 8192 |
| `batch_size` | 每次推論批次中處理的透視視圖數量。視圖總數為 12（預設值：4）。 | INT | 是 | 1 至 12 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `moge_geometry` | 包含估計幾何資訊的字典：`points`（3D 點雲）、`depth`（深度圖）、`mask`（有效區域遮罩）和 `image`（輸入影像）。 | MOGE_GEOMETRY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3a701e3679bc35cd5fddc54868ac9c4bc9b4e23a5b97bbf61e46b7309e43600b`
