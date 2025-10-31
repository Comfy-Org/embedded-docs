> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/zh-TW.md)

ModelMergeAuraflow 節點允許您透過調整各種模型組件的特定混合權重，將兩個不同的模型融合在一起。它提供了對模型從初始層到最終輸出的不同部分如何合併的細粒度控制。此節點特別適用於創建自定義模型組合，並對合併過程進行精確控制。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `模型 1` | MODEL | 是 | - | 要合併的第一個模型 |
| `模型 2` | MODEL | 是 | - | 要合併的第二個模型 |
| `init_x_linear.` | FLOAT | 是 | 0.0 - 1.0 | 初始線性轉換的混合權重（預設值：1.0） |
| `positional_encoding` | FLOAT | 是 | 0.0 - 1.0 | 位置編碼組件的混合權重（預設值：1.0） |
| `cond_seq_linear.` | FLOAT | 是 | 0.0 - 1.0 | 條件序列線性層的混合權重（預設值：1.0） |
| `register_tokens` | FLOAT | 是 | 0.0 - 1.0 | 令牌註冊組件的混合權重（預設值：1.0） |
| `t_embedder.` | FLOAT | 是 | 0.0 - 1.0 | 時間嵌入組件的混合權重（預設值：1.0） |
| `double_layers.0.` | FLOAT | 是 | 0.0 - 1.0 | 雙層群組 0 的混合權重（預設值：1.0） |
| `double_layers.1.` | FLOAT | 是 | 0.0 - 1.0 | 雙層群組 1 的混合權重（預設值：1.0） |
| `double_layers.2.` | FLOAT | 是 | 0.0 - 1.0 | 雙層群組 2 的混合權重（預設值：1.0） |
| `double_layers.3.` | FLOAT | 是 | 0.0 - 1.0 | 雙層群組 3 的混合權重（預設值：1.0） |
| `single_layers.0.` | FLOAT | 是 | 0.0 - 1.0 | 單層 0 的混合權重（預設值：1.0） |
| `single_layers.1.` | FLOAT | 是 | 0.0 - 1.0 | 單層 1 的混合權重（預設值：1.0） |
| `single_layers.2.` | FLOAT | 是 | 0.0 - 1.0 | 單層 2 的混合權重（預設值：1.0） |
| `single_layers.3.` | FLOAT | 是 | 0.0 - 1.0 | 單層 3 的混合權重（預設值：1.0） |
| `single_layers.4.` | FLOAT | 是 | 0.0 - 1.0 | 單層 4 的混合權重（預設值：1.0） |
| `single_layers.5.` | FLOAT | 是 | 0.0 - 1.0 | 單層 5 的混合權重（預設值：1.0） |
| `single_layers.6.` | FLOAT | 是 | 0.0 - 1.0 | 單層 6 的混合權重（預設值：1.0） |
| `single_layers.7.` | FLOAT | 是 | 0.0 - 1.0 | 單層 7 的混合權重（預設值：1.0） |
| `single_layers.8.` | FLOAT | 是 | 0.0 - 1.0 | 單層 8 的混合權重（預設值：1.0） |
| `single_layers.9.` | FLOAT | 是 | 0.0 - 1.0 | 單層 9 的混合權重（預設值：1.0） |
| `single_layers.10.` | FLOAT | 是 | 0.0 - 1.0 | 單層 10 的混合權重（預設值：1.0） |
| `single_layers.11.` | FLOAT | 是 | 0.0 - 1.0 | 單層 11 的混合權重（預設值：1.0） |
| `single_layers.12.` | FLOAT | 是 | 0.0 - 1.0 | 單層 12 的混合權重（預設值：1.0） |
| `single_layers.13.` | FLOAT | 是 | 0.0 - 1.0 | 單層 13 的混合權重（預設值：1.0） |
| `single_layers.14.` | FLOAT | 是 | 0.0 - 1.0 | 單層 14 的混合權重（預設值：1.0） |
| `single_layers.15.` | FLOAT | 是 | 0.0 - 1.0 | 單層 15 的混合權重（預設值：1.0） |
| `single_layers.16.` | FLOAT | 是 | 0.0 - 1.0 | 單層 16 的混合權重（預設值：1.0） |
| `single_layers.17.` | FLOAT | 是 | 0.0 - 1.0 | 單層 17 的混合權重（預設值：1.0） |
| `single_layers.18.` | FLOAT | 是 | 0.0 - 1.0 | 單層 18 的混合權重（預設值：1.0） |
| `single_layers.19.` | FLOAT | 是 | 0.0 - 1.0 | 單層 19 的混合權重（預設值：1.0） |
| `single_layers.20.` | FLOAT | 是 | 0.0 - 1.0 | 單層 20 的混合權重（預設值：1.0） |
| `single_layers.21.` | FLOAT | 是 | 0.0 - 1.0 | 單層 21 的混合權重（預設值：1.0） |
| `single_layers.22.` | FLOAT | 是 | 0.0 - 1.0 | 單層 22 的混合權重（預設值：1.0） |
| `single_layers.23.` | FLOAT | 是 | 0.0 - 1.0 | 單層 23 的混合權重（預設值：1.0） |
| `single_layers.24.` | FLOAT | 是 | 0.0 - 1.0 | 單層 24 的混合權重（預設值：1.0） |
| `single_layers.25.` | FLOAT | 是 | 0.0 - 1.0 | 單層 25 的混合權重（預設值：1.0） |
| `single_layers.26.` | FLOAT | 是 | 0.0 - 1.0 | 單層 26 的混合權重（預設值：1.0） |
| `single_layers.27.` | FLOAT | 是 | 0.0 - 1.0 | 單層 27 的混合權重（預設值：1.0） |
| `single_layers.28.` | FLOAT | 是 | 0.0 - 1.0 | 單層 28 的混合權重（預設值：1.0） |
| `single_layers.29.` | FLOAT | 是 | 0.0 - 1.0 | 單層 29 的混合權重（預設值：1.0） |
| `single_layers.30.` | FLOAT | 是 | 0.0 - 1.0 | 單層 30 的混合權重（預設值：1.0） |
| `single_layers.31.` | FLOAT | 是 | 0.0 - 1.0 | 單層 31 的混合權重（預設值：1.0） |
| `modF.` | FLOAT | 是 | 0.0 - 1.0 | modF 組件的混合權重（預設值：1.0） |
| `final_linear.` | FLOAT | 是 | 0.0 - 1.0 | 最終線性轉換的混合權重（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 根據指定的混合權重合併兩個輸入模型特徵後的融合模型 |