# LTXV 時長預測器

此節點使用 LTX 2.4 時長頭預測提示詞的自然鏡頭時長。它使用提供的幀率和最小/最大時長限制，將預測的時長轉換為符合 VAE 幀網格的幀數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於預處理文字嵌入並執行時長頭的模型。 | MODEL | 是 | N/A |
| `positive` | 用於時長預測的條件，提供提示詞的文字嵌入和元數據。 | CONDITIONING | 是 | N/A |
| `duration_head` | 使用 ModelPatchLoader 載入的 LTX 2.4 時長頭。必須是 LTX 時長頭。 | MODEL_PATCH | 是 | N/A |
| `frame_rate` | 用於將秒轉換為幀的幀率（幀/秒）（預設：24.0）。 | FLOAT | 是 | 1.0 至 120.0 |
| `min_seconds` | 將預測轉換為幀數時使用的最小時長（秒）（預設：1.0）。 | FLOAT | 是 | 0.5 至 120.0 |
| `max_seconds` | 將預測轉換為幀數時使用的最大時長（秒）（預設：20.0）。 | FLOAT | 是 | 0.5 至 120.0 |

注意：`duration_head` 輸入必須是使用 ModelPatchLoader 載入的 LTX 2.4 時長頭。如果連接的模型補丁不是 LTX 時長頭，節點將引發 ValueError。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `num_frames` | 預測的時長轉換為幀數，並對齊到 VAE 的 8k+1 幀網格。 | INT |
| `seconds` | 原始（未裁剪）的預測時長。這是對齊到幀網格之前的值。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ebbf6a2601a955122ab9862142aa475524c1f38403f4ef8dc9ffee6456ee8ce5`
