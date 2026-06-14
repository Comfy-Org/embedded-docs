# 執行 Depth Anything 3

此節點在影像上執行 Depth Anything 3 模型，以估算深度和幾何資訊。在多視圖模式下，多張影像會作為同一場景的不同視角一起處理，以產生幾何一致的深度圖和相機姿態。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `da3_model` | 用於推論的 Depth Anything 3 模型 | DA3_MODEL | 是 | - |
| `image` | 要處理的輸入影像或影像組 | IMAGE | 是 | - |
| `resolution` | 模型運行的解析度（最長邊，14 的倍數）。數值越低速度越快且使用較少 VRAM。數值越高可產生更多細節。輸出會上採樣回原始尺寸（預設值：504） | INT | 是 | 140 至 2520（步長：14） |
| `resize_method` | upper_bound_resize：縮放使最長邊等於解析度（節省記憶體，預設）。lower_bound_resize：縮放使最短邊等於解析度（在長/寬影像上保留更多細節，使用更多記憶體） | COMBO | 是 | `"upper_bound_resize"`<br>`"lower_bound_resize"` |
| `mode` | mono：單視圖影像處理（適用於任何模型變體）。multiview：所有影像一起處理以達到幾何一致性及相機姿態估算（僅適用於 Small 和 Base 模型） | COMBO | 是 | `"mono"`<br>`"multiview"` |
| `ref_view_strategy` | 在多視圖模式下哪個視圖作為幾何錨點。saddle_balanced：與所有其他視圖最平均的視圖（最佳通用選擇）。saddle_sim_range：與其他視圖視覺上最不同的視圖。first / middle：固定的位置選擇 | COMBO | 否（條件式） | `"saddle_balanced"`<br>`"saddle_sim_range"`<br>`"first"`<br>`"middle"` |
| `pose_method` | 如何估算相機視野（僅適用於 Small 和 Base 模型）。cam_dec：從影像特徵學習。ray_pose：從模型的 3D 射線輸出以幾何方式推導。影響 3D 輸出的透視正確性 | COMBO | 否（條件式） | `"cam_dec"`<br>`"ray_pose"` |

**關於參數限制的說明：**
- `ref_view_strategy` 和 `pose_method` 參數僅在 `mode` 設定為 `"multiview"` 時可用
- 多視圖模式需要 Small 或 Base 模型變體。具有其他頭部類型（如 Metric 或 Mono）的模型不支援跨視圖注意力或相機姿態估算
- 當 `pose_method` 設定為 `"cam_dec"` 時，模型必須具有相機解碼器。若設定為 `"ray_pose"`，模型必須具有 DualDPT 頭部
- 如果選取的 `pose_method` 與載入的模型不相容，將會引發錯誤

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `da3_geometry` | 非標準化張量的字典。始終包含鍵值：depth、image、mode。可選鍵值包括：sky（適用於 Mono/Metric 模型）、confidence（適用於 Small/Base 模型）、extrinsics 和 intrinsics（適用於多視圖模式） | DA3_GEOMETRY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Inference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e91dd47e6a01719cdd6b6ce8a9bcc45933cac72c5e147ac42906d2f83ab7c250`
