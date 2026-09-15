# Hunyuan3Dv2ConditioningMultiView

Hunyuan3Dv2ConditioningMultiView 節點會將最多四個視圖（`front`、`left`、`back`、`right`）的 CLIP vision 輸出合併為單一的多視圖條件。每個提供的視圖都會在其 CLIP vision 嵌入中加入位置編碼，然後將產生的嵌入串接起來。此節點會根據合併後的嵌入輸出正向條件，並輸出一個形狀相同、填滿零值的負向條件。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `前視圖` | 前視圖的 CLIP vision 輸出。可選的視圖輸入。 | CLIP_VISION_OUTPUT | 否 | - |
| `左視圖` | 左視圖的 CLIP vision 輸出。可選的視圖輸入。 | CLIP_VISION_OUTPUT | 否 | - |
| `後視圖` | 後視圖的 CLIP vision 輸出。可選的視圖輸入。 | CLIP_VISION_OUTPUT | 否 | - |
| `右視圖` | 右視圖的 CLIP vision 輸出。可選的視圖輸入。 | CLIP_VISION_OUTPUT | 否 | - |

**注意：** 至少必須提供一個視圖輸入，節點才能運作。節點只會處理包含有效 CLIP vision 輸出資料的視圖，並略過未連接的視圖。每個視圖會根據其插槽（`front`、`left`、`back`、`right`）接收固定的位置編碼，而所有已提供視圖的處理後嵌入會沿著序列維度串接在一起。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 包含結合後多視圖嵌入與位置編碼的正向條件。 | CONDITIONING |
| `negative` | 與正向條件形狀相符且值為零的負向條件。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
