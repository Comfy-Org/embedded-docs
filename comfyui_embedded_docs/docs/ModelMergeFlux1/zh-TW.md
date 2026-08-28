# ModelMergeFlux1

ModelMergeFlux1 節點透過加權插值混合兩個擴散模型的組成部分，將它們合併。它允許精細控制模型不同部分的組合方式，包括影像處理區塊、時間嵌入層、引導機制、向量輸入、文字編碼器，以及各種 transformer 區塊。這使得能夠從兩個來源模型建立具有自訂特性的混合模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個來源模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個來源模型 | MODEL | 是 | - |
| `img_in.` | 影像輸入插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `time_in.` | 時間嵌入插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `guidance_in` | 引導機制插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `vector_in.` | 向量輸入插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `txt_in.` | 文字編碼器插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.0.` | 雙重塊 0 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.1.` | 雙重塊 1 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.2.` | 雙重塊 2 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.3.` | 雙重塊 3 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.4.` | 雙重塊 4 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.5.` | 雙重塊 5 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.6.` | 雙重塊 6 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.7.` | 雙重塊 7 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.8.` | 雙重塊 8 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.9.` | 雙重塊 9 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.10.` | 雙重塊 10 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.11.` | 雙重塊 11 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.12.` | 雙重塊 12 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.13.` | 雙重塊 13 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.14.` | 雙重塊 14 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.15.` | 雙重塊 15 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.16.` | 雙重塊 16 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.17.` | 雙重塊 17 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `double_blocks.18.` | 雙重塊 18 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.0.` | 單一區塊 0 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.1.` | 單一區塊 1 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.2.` | 單一區塊 2 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.3.` | 單一區塊 3 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.4.` | 單一區塊 4 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.5.` | 單一區塊 5 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.6.` | 單一區塊 6 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.7.` | 單一區塊 7 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.8.` | 單一區塊 8 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.9.` | 單一區塊 9 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.10.` | 單一區塊 10 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.11.` | 單一區塊 11 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.12.` | 單一區塊 12 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.13.` | 單一區塊 13 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.14.` | 單一區塊 14 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.15.` | 單一區塊 15 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.16.` | 單一區塊 16 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.17.` | 單一區塊 17 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.18.` | 單一區塊 18 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.19.` | 單一區塊 19 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.20.` | 單一區塊 20 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.21.` | 單一區塊 21 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.22.` | 單一區塊 22 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.23.` | 單一區塊 23 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.24.` | 單一區塊 24 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.25.` | 單一區塊 25 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.26.` | 單一區塊 26 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.27.` | 單一區塊 27 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.28.` | 單一區塊 28 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.29.` | 單一區塊 29 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.30.` | 單一區塊 30 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.31.` | 單一區塊 31 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.32.` | 單一區塊 32 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.33.` | 單一區塊 33 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.34.` | 單一區塊 34 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.35.` | 單一區塊 35 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.36.` | 單一區塊 36 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `single_blocks.37.` | 單一區塊 37 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `final_layer.` | 最終層插值權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 合併後的模型，結合了兩個輸入模型的特徵 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a1cc4dd2c253bbeb94144969e921af40a7f12a1ec23ed7c23da89107767dc26`
