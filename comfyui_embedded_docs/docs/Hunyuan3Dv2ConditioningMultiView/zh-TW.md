# Hunyuan3Dv2ConditioningMultiView

Hunyuan3Dv2ConditioningMultiView 節點處理用於 3D 影片生成的多視圖 CLIP 視覺嵌入。它接受可選的前、左、後、右視圖嵌入，並在將它們合併成單一條件序列之前，為每個提供的視圖加入位置編碼。此節點同時輸出由合併後的嵌入產生的正向條件，以及具有零值的負向條件。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `front` | 前視圖的 CLIP 視覺輸出 | CLIP_VISION_OUTPUT | 否 | - |
| `left` | 左視圖的 CLIP 視覺輸出 | CLIP_VISION_OUTPUT | 否 | - |
| `back` | 後視圖的 CLIP 視覺輸出 | CLIP_VISION_OUTPUT | 否 | - |
| `right` | 右視圖的 CLIP 視覺輸出 | CLIP_VISION_OUTPUT | 否 | - |

**注意：** 至少必須提供一個視圖輸入，此節點才能運作。此節點僅處理包含有效 CLIP 視覺輸出資料的視圖。每個提供的視圖會根據其視圖位置（前、左、後、右）接收位置編碼，且編碼後的視圖會依相同順序串接。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 包含已加入位置編碼之合併多視圖嵌入的正向條件 | CONDITIONING |
| `negative` | 包含零值且形狀與正向條件相同的負向條件 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
