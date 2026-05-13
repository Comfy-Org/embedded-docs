> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/zh-TW.md)

Hunyuan3Dv2ConditioningMultiView 節點處理多視角 CLIP 視覺嵌入，用於 3D 影片生成。它接收可選的前、左、後、右視角嵌入，並將其與位置編碼結合，為影片模型創建條件數據。該節點輸出包含組合嵌入的正向條件，以及包含零值的負向條件。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `front` | CLIP_VISION_OUTPUT | 否 | - | 前視角的 CLIP 視覺輸出 |
| `left` | CLIP_VISION_OUTPUT | 否 | - | 左視角的 CLIP 視覺輸出 |
| `back` | CLIP_VISION_OUTPUT | 否 | - | 後視角的 CLIP 視覺輸出 |
| `right` | CLIP_VISION_OUTPUT | 否 | - | 右視角的 CLIP 視覺輸出 |

**注意：** 節點運作時至少需要提供一個視角輸入。節點僅會處理包含有效 CLIP 視覺輸出數據的視角。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 包含帶有位置編碼的組合多視角嵌入的正向條件 |
| `negative` | CONDITIONING | 包含零值用於對比學習的負向條件 |

---
**Source fingerprint (SHA-256):** `01998ae9ba7d2ae9a2f6a0b5aee4c03168f935fb9769317cd80d93a7a4b96f13`
