# Hunyuan3Dv2Conditioning

Hunyuan3Dv2Conditioning 節點處理 CLIP 視覺輸出，以生成 3D 模型的條件數據。它從視覺輸出中提取最後的隱藏狀態嵌入，並建立正條件與負條件配對。正條件使用實際的嵌入，而負條件則使用形狀相同的零值嵌入。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision_output` | 來自 CLIP 視覺模型的輸出，包含視覺嵌入 | CLIP_VISION_OUTPUT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 包含 CLIP 視覺嵌入的正條件數據 | CONDITIONING |
| `negative` | 包含與正條件嵌入形狀匹配的零值嵌入的負條件數據 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3a32967d62a0645b0c375b17ab96e20805c2e0005e585dddf5a3a77d35994fec`
