> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/zh-TW.md)

ModelMergeFlux1 節點透過使用加權插值混合其元件，來合併兩個擴散模型。它允許對模型不同部分的組合方式進行精細控制，包括影像處理區塊、時間嵌入層、引導機制、向量輸入、文字編碼器以及各種 Transformer 區塊。這使得能夠從兩個來源模型創建具有自訂特性的混合模型。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `模型 1` | MODEL | 是 | - | 要合併的第一個來源模型 |
| `模型 2` | MODEL | 是 | - | 要合併的第二個來源模型 |
| `img_in.` | FLOAT | 是 | 0.0 至 1.0 | 影像輸入插值權重（預設值：1.0） |
| `time_in.` | FLOAT | 是 | 0.0 至 1.0 | 時間嵌入插值權重（預設值：1.0） |
| `guidance_in` | FLOAT | 是 | 0.0 至 1.0 | 引導機制插值權重（預設值：1.0） |
| `vector_in.` | FLOAT | 是 | 0.0 至 1.0 | 向量輸入插值權重（預設值：1.0） |
| `txt_in.` | FLOAT | 是 | 0.0 至 1.0 | 文字編碼器插值權重（預設值：1.0） |
| `double_blocks.0.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 0 插值權重（預設值：1.0） |
| `double_blocks.1.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 1 插值權重（預設值：1.0） |
| `double_blocks.2.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 2 插值權重（預設值：1.0） |
| `double_blocks.3.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 3 插值權重（預設值：1.0） |
| `double_blocks.4.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 4 插值權重（預設值：1.0） |
| `double_blocks.5.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 5 插值權重（預設值：1.0） |
| `double_blocks.6.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 6 插值權重（預設值：1.0） |
| `double_blocks.7.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 7 插值權重（預設值：1.0） |
| `double_blocks.8.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 8 插值權重（預設值：1.0） |
| `double_blocks.9.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 9 插值權重（預設值：1.0） |
| `double_blocks.10.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 10 插值權重（預設值：1.0） |
| `double_blocks.11.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 11 插值權重（預設值：1.0） |
| `double_blocks.12.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 12 插值權重（預設值：1.0） |
| `double_blocks.13.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 13 插值權重（預設值：1.0） |
| `double_blocks.14.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 14 插值權重（預設值：1.0） |
| `double_blocks.15.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 15 插值權重（預設值：1.0） |
| `double_blocks.16.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 16 插值權重（預設值：1.0） |
| `double_blocks.17.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 17 插值權重（預設值：1.0） |
| `double_blocks.18.` | FLOAT | 是 | 0.0 至 1.0 | 雙區塊 18 插值權重（預設值：1.0） |
| `single_blocks.0.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 0 插值權重（預設值：1.0） |
| `single_blocks.1.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 1 插值權重（預設值：1.0） |
| `single_blocks.2.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 2 插值權重（預設值：1.0） |
| `single_blocks.3.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 3 插值權重（預設值：1.0） |
| `single_blocks.4.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 4 插值權重（預設值：1.0） |
| `single_blocks.5.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 5 插值權重（預設值：1.0） |
| `single_blocks.6.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 6 插值權重（預設值：1.0） |
| `single_blocks.7.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 7 插值權重（預設值：1.0） |
| `single_blocks.8.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 8 插值權重（預設值：1.0） |
| `single_blocks.9.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 9 插值權重（預設值：1.0） |
| `single_blocks.10.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 10 插值權重（預設值：1.0） |
| `single_blocks.11.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 11 插值權重（預設值：1.0） |
| `single_blocks.12.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 12 插值權重（預設值：1.0） |
| `single_blocks.13.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 13 插值權重（預設值：1.0） |
| `single_blocks.14.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 14 插值權重（預設值：1.0） |
| `single_blocks.15.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 15 插值權重（預設值：1.0） |
| `single_blocks.16.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 16 插值權重（預設值：1.0） |
| `single_blocks.17.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 17 插值權重（預設值：1.0） |
| `single_blocks.18.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 18 插值權重（預設值：1.0） |
| `single_blocks.19.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 19 插值權重（預設值：1.0） |
| `single_blocks.20.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 20 插值權重（預設值：1.0） |
| `single_blocks.21.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 21 插值權重（預設值：1.0） |
| `single_blocks.22.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 22 插值權重（預設值：1.0） |
| `single_blocks.23.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 23 插值權重（預設值：1.0） |
| `single_blocks.24.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 24 插值權重（預設值：1.0） |
| `single_blocks.25.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 25 插值權重（預設值：1.0） |
| `single_blocks.26.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 26 插值權重（預設值：1.0） |
| `single_blocks.27.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 27 插值權重（預設值：1.0） |
| `single_blocks.28.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 28 插值權重（預設值：1.0） |
| `single_blocks.29.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 29 插值權重（預設值：1.0） |
| `single_blocks.30.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 30 插值權重（預設值：1.0） |
| `single_blocks.31.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 31 插值權重（預設值：1.0） |
| `single_blocks.32.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 32 插值權重（預設值：1.0） |
| `single_blocks.33.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 33 插值權重（預設值：1.0） |
| `single_blocks.34.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 34 插值權重（預設值：1.0） |
| `single_blocks.35.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 35 插值權重（預設值：1.0） |
| `single_blocks.36.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 36 插值權重（預設值：1.0） |
| `single_blocks.37.` | FLOAT | 是 | 0.0 至 1.0 | 單區塊 37 插值權重（預設值：1.0） |
| `final_layer.` | FLOAT | 是 | 0.0 至 1.0 | 最終層插值權重（預設值：1.0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 合併後的模型，結合了兩個輸入模型的特性 |

---
**Source fingerprint (SHA-256):** `a632133b5d4bc7c5a4e1be5f6f779e424a491fffb8ef7702346adc4acf6f23bc`
