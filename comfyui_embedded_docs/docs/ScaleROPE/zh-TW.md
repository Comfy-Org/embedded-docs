# 縮放ROPE

ScaleROPE 節點透過對模型的 X、Y 和 T（時間）分量套用各自獨立的縮放與平移因子，來修改模型的旋轉位置嵌入（ROPE）。這是一個用於調整模型位置編碼行為的高級實驗性節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要修改其 ROPE 參數的模型。 | MODEL | 是 | - |
| `scale_x` | 套用於 ROPE 的 X 分量的縮放因子（預設值：1.0）。 | FLOAT | 是 | 0.0 - 100.0 (step 0.1) |
| `shift_x` | 套用於 ROPE 的 X 分量的平移值（預設值：0.0）。 | FLOAT | 是 | -256.0 - 256.0 (step 0.1) |
| `scale_y` | 套用於 ROPE 的 Y 分量的縮放因子（預設值：1.0）。 | FLOAT | 是 | 0.0 - 100.0 (step 0.1) |
| `shift_y` | 套用於 ROPE 的 Y 分量的平移值（預設值：0.0）。 | FLOAT | 是 | -256.0 - 256.0 (step 0.1) |
| `scale_t` | 套用於 ROPE 的 T（時間）分量的縮放因子（預設值：1.0）。 | FLOAT | 是 | 0.0 - 100.0 (step 0.1) |
| `shift_t` | 套用於 ROPE 的 T（時間）分量的平移值（預設值：0.0）。 | FLOAT | 是 | -256.0 - 256.0 (step 0.1) |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用新的 ROPE 縮放與平移參數的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
