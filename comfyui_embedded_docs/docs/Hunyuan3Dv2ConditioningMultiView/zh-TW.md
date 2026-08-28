# Hunyuan3Dv2ConditioningMultiView

Hunyuan3Dv2ConditioningMultiView 節點將來自多達四個視圖（前、左、後、右）的 CLIP 視覺輸出組合成單一的多視圖條件化。每個提供的視圖都會在其 CLIP 視覺嵌入中加入位置編碼，然後將產生的嵌入串接起來。此節點輸出基於組合嵌入的正向條件化，以及與相同形狀的零填充的負向條件化。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `前視圖` | 前視圖的 CLIP 視覺輸出。可選的視圖輸入。 | CLIP_VISION_OUTPUT | 否 | - |
| `左視圖` | 左視圖的 CLIP 視覺輸出。可選的視圖輸入。 | CLIP_VISION_OUTPUT | 否 | - |
| `後視圖` | 後視圖的 CLIP 視覺輸出。可選的視圖輸入。 | CLIP_VISION_OUTPUT | 否 | - |
| `右視圖` | 右視圖的 CLIP 視覺輸出。可選的視圖輸入。 | CLIP_VISION_OUTPUT | 否 | - |

**注意：** 至少需要提供一個視圖輸入，此節點才能運作。此節點只處理包含有效 CLIP 視覺輸出資料的視圖，並跳過未連接的視圖。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `正向` | 包含帶有位置編碼的組合多視圖嵌入的正向條件化。 | CONDITIONING |
| `負向` | 具有與正向條件化形狀匹配的零值的負向條件化。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
