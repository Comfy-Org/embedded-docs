> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/zh-TW.md)

ModelMergeCosmos14B 節點使用基於區塊的方法合併兩個 AI 模型，該方法專為 Cosmos 14B 模型架構設計。它允許您透過調整每個模型區塊和嵌入層的權重值（範圍在 0.0 到 1.0 之間）來混合模型的不同組件。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `模型 1` | MODEL | 是 | - | 要合併的第一個模型 |
| `模型 2` | MODEL | 是 | - | 要合併的第二個模型 |
| `pos_embedder.` | FLOAT | 是 | 0.0 - 1.0 | 位置嵌入器權重（預設值：1.0） |
| `extra_pos_embedder.` | FLOAT | 是 | 0.0 - 1.0 | 額外位置嵌入器權重（預設值：1.0） |
| `x_embedder.` | FLOAT | 是 | 0.0 - 1.0 | X 嵌入器權重（預設值：1.0） |
| `t_embedder.` | FLOAT | 是 | 0.0 - 1.0 | T 嵌入器權重（預設值：1.0） |
| `affline_norm.` | FLOAT | 是 | 0.0 - 1.0 | 仿射歸一化權重（預設值：1.0） |
| `blocks.block0.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 0 權重（預設值：1.0） |
| `blocks.block1.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 1 權重（預設值：1.0） |
| `blocks.block2.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 2 權重（預設值：1.0） |
| `blocks.block3.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 3 權重（預設值：1.0） |
| `blocks.block4.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 4 權重（預設值：1.0） |
| `blocks.block5.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 5 權重（預設值：1.0） |
| `blocks.block6.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 6 權重（預設值：1.0） |
| `blocks.block7.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 7 權重（預設值：1.0） |
| `blocks.block8.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 8 權重（預設值：1.0） |
| `blocks.block9.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 9 權重（預設值：1.0） |
| `blocks.block10.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 10 權重（預設值：1.0） |
| `blocks.block11.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 11 權重（預設值：1.0） |
| `blocks.block12.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 12 權重（預設值：1.0） |
| `blocks.block13.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 13 權重（預設值：1.0） |
| `blocks.block14.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 14 權重（預設值：1.0） |
| `blocks.block15.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 15 權重（預設值：1.0） |
| `blocks.block16.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 16 權重（預設值：1.0） |
| `blocks.block17.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 17 權重（預設值：1.0） |
| `blocks.block18.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 18 權重（預設值：1.0） |
| `blocks.block19.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 19 權重（預設值：1.0） |
| `blocks.block20.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 20 權重（預設值：1.0） |
| `blocks.block21.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 21 權重（預設值：1.0） |
| `blocks.block22.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 22 權重（預設值：1.0） |
| `blocks.block23.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 23 權重（預設值：1.0） |
| `blocks.block24.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 24 權重（預設值：1.0） |
| `blocks.block25.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 25 權重（預設值：1.0） |
| `blocks.block26.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 26 權重（預設值：1.0） |
| `blocks.block27.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 27 權重（預設值：1.0） |
| `blocks.block28.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 28 權重（預設值：1.0） |
| `blocks.block29.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 29 權重（預設值：1.0） |
| `blocks.block30.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 30 權重（預設值：1.0） |
| `blocks.block31.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 31 權重（預設值：1.0） |
| `blocks.block32.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 32 權重（預設值：1.0） |
| `blocks.block33.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 33 權重（預設值：1.0） |
| `blocks.block34.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 34 權重（預設值：1.0） |
| `blocks.block35.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 35 權重（預設值：1.0） |
| `final_layer.` | FLOAT | 是 | 0.0 - 1.0 | 最終層權重（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 合併後的模型，結合了兩個輸入模型的特徵 |