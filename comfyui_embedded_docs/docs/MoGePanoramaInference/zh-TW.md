# MoGe 全景推論

此節點對等距長方投影（equirectangular）全景影像執行深度估計。其運作方式是將全景分割為 12 個透視視圖，對每個視圖執行 MoGe 深度估計模型，然後將結果合併回原始全景的單一完整深度圖。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_model` | 用於推論的 MoGe 模型。 | MOGE_MODEL | 是 |  |
| `image` | 等距長方投影全景（任意長寬比）。僅接受單一影像。 | IMAGE | 是 |  |
| `resolution_level` | 每個視圖的細節程度（0 = 最快，9 = 最詳細）。預設值：9。 | INT | 是 | 0 至 9 |
| `split_resolution` | 每個透視分割的解析度。預設值：512。 | INT | 是 | 256 至 1024 |
| `merge_resolution` | 合併後等距距離圖的長邊解析度。預設值：1920。 | INT | 是 | 256 至 8192 |
| `batch_size` | 每個推論批次中的視圖數（共 12 個分割）。預設值：4。 | INT | 是 | 1 至 12 |

注意：此節點僅接受單一影像。傳入一批影像會引發錯誤。全景一律分割為 12 個透視視圖；`batch_size` 僅控制每個推論批次中處理多少個視圖。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `moge_geometry` | 包含估計幾何資訊的字典：`points`（3D 點雲）、`depth`（深度圖）、`mask`（有效區域遮罩）與 `image`（輸入影像）。 | MOGE_GEOMETRY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
