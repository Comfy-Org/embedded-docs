> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/zh-TW.md)

ModelMergeSD35_Large 節點允許您透過調整不同模型組件的影響程度，將兩個 Stable Diffusion 3.5 Large 模型融合在一起。它提供了精確的控制，讓您可以調整第二個模型的每個部分（從嵌入層到聯合區塊和最終層）對最終合併模型的貢獻程度。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | 是 | - | 作為合併基礎的基準模型 |
| `model2` | MODEL | 是 | - | 其組件將被混入基準模型的次要模型 |
| `pos_embed.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的位置嵌入量（預設值：1.0） |
| `x_embedder.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的 x 嵌入器量（預設值：1.0） |
| `context_embedder.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的上下文嵌入器量（預設值：1.0） |
| `y_embedder.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的 y 嵌入器量（預設值：1.0） |
| `t_embedder.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的 t 嵌入器量（預設值：1.0） |
| `joint_blocks.0.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 0 量（預設值：1.0） |
| `joint_blocks.1.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 1 量（預設值：1.0） |
| `joint_blocks.2.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 2 量（預設值：1.0） |
| `joint_blocks.3.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 3 量（預設值：1.0） |
| `joint_blocks.4.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 4 量（預設值：1.0） |
| `joint_blocks.5.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 5 量（預設值：1.0） |
| `joint_blocks.6.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 6 量（預設值：1.0） |
| `joint_blocks.7.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 7 量（預設值：1.0） |
| `joint_blocks.8.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 8 量（預設值：1.0） |
| `joint_blocks.9.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 9 量（預設值：1.0） |
| `joint_blocks.10.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 10 量（預設值：1.0） |
| `joint_blocks.11.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 11 量（預設值：1.0） |
| `joint_blocks.12.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 12 量（預設值：1.0） |
| `joint_blocks.13.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 13 量（預設值：1.0） |
| `joint_blocks.14.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 14 量（預設值：1.0） |
| `joint_blocks.15.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 15 量（預設值：1.0） |
| `joint_blocks.16.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 16 量（預設值：1.0） |
| `joint_blocks.17.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 17 量（預設值：1.0） |
| `joint_blocks.18.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 18 量（預設值：1.0） |
| `joint_blocks.19.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 19 量（預設值：1.0） |
| `joint_blocks.20.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 20 量（預設值：1.0） |
| `joint_blocks.21.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 21 量（預設值：1.0） |
| `joint_blocks.22.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 22 量（預設值：1.0） |
| `joint_blocks.23.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 23 量（預設值：1.0） |
| `joint_blocks.24.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 24 量（預設值：1.0） |
| `joint_blocks.25.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 25 量（預設值：1.0） |
| `joint_blocks.26.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 26 量（預設值：1.0） |
| `joint_blocks.27.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 27 量（預設值：1.0） |
| `joint_blocks.28.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 28 量（預設值：1.0） |
| `joint_blocks.29.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 29 量（預設值：1.0） |
| `joint_blocks.30.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 30 量（預設值：1.0） |
| `joint_blocks.31.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 31 量（預設值：1.0） |
| `joint_blocks.32.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 32 量（預設值：1.0） |
| `joint_blocks.33.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 33 量（預設值：1.0） |
| `joint_blocks.34.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 34 量（預設值：1.0） |
| `joint_blocks.35.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 35 量（預設值：1.0） |
| `joint_blocks.36.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 36 量（預設值：1.0） |
| `joint_blocks.37.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的聯合區塊 37 量（預設值：1.0） |
| `final_layer.` | FLOAT | 是 | 0.0 至 1.0 | 控制從 model2 混入合併模型的最終層量（預設值：1.0） |

**注意：** 所有混合參數接受 0.0 到 1.0 的值，其中 0.0 表示該特定組件不從 model2 貢獻，1.0 表示該特定組件完全從 model2 貢獻。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 根據指定的混合參數，結合了兩個輸入模型特徵的最終合併模型 |