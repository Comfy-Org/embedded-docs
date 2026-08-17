# Hunyuan3Dv2Conditioning

Hunyuan3Dv2Conditioning 節點處理 CLIP 視覺輸出，為 3D 模型產生 conditioning 資料。它從視覺輸出中提取最後的隱藏狀態嵌入，並建立正向與負向的 conditioning 配對。正向 conditioning 使用實際嵌入，而負向 conditioning 使用相同形狀的零值嵌入。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision_output` | 來自 CLIP 視覺模型的輸出，包含視覺嵌入 | CLIP_VISION_OUTPUT | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 包含 CLIP 視覺嵌入的正向條件資料 | CONDITIONING |
| `negative` | 包含零值嵌入的負向條件資料，其形狀與正向嵌入相同 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
