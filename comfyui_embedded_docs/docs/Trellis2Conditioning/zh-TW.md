# Trellis2Conditioning

Trellis2Conditioning 將輸入圖像轉換為 TRELLIS.2 模型的條件資料。它使用 CLIP 視覺模型將圖像編碼為兩組特徵（512 和 1024 尺度），並將它們包裝為正向條件對，同時建立一個匹配的零填充負向條件對，作為空參考。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | 用於將圖像編碼為條件特徵的 CLIP 視覺模型。 | CLIP_VISION | 是 | 任何可用的 CLIP 視覺模型 |
| `image` | 來自 ImageCropToMask 的預處理圖像（TRELLIS.2 使用 pad_factor=1.0）。 | IMAGE | 是 | 任何圖像 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 包含 512 和 1024 尺度編碼圖像特徵的條件資料，用作 TRELLIS.2 模型的正向條件。 | CONDITIONING |
| `negative` | 與正向條件具有相同形狀的零填充條件資料，用作空的負向參考。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
