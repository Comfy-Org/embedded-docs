# LTXVDurationPredictor

此節點使用 LTX 2.4 時長頭（duration head）為提示詞預測一個鏡頭的自然時長。它會根據提供的影格率（frame rate）以及最小/最大時長限制，將預測的時長轉換為符合 VAE 影格網格的影格數。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於預處理文字嵌入（text embeddings）並執行時長頭的模型。 | MODEL | 是 | N/A |
| `positive` | 提供提示詞文字嵌入及中繼資料以進行時長預測的 conditioning。 | CONDITIONING | 是 | N/A |
| `duration_head` | 使用 ModelPatchLoader 載入的 LTX 2.4 時長頭。必須是 LTX 時長頭。 | MODEL_PATCH | 是 | N/A |
| `frame_rate` | 以每秒影格數表示的影格率，用於將秒數轉換為影格數（預設值：24.0）。 | FLOAT | 是 | 1.0 至 120.0 |
| `min_seconds` | 將預測轉換為影格數時使用的最小時長（秒）（預設值：1.0）。 | FLOAT | 是 | 0.5 至 120.0 |
| `max_seconds` | 將預測轉換為影格數時使用的最大時長（秒）（預設值：20.0）。 | FLOAT | 是 | 0.5 至 120.0 |

注意：`duration_head` 輸入必須是使用 ModelPatchLoader 載入的 LTX 2.4 時長頭。如果連接的模型修補程式（model patch）不是 LTX 時長頭，節點會引發 ValueError。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `num_frames` | 預測的時長轉換為影格數，並對齊至 VAE 的 8k+1 影格網格。 | INT |
| `seconds` | 原始（未截斷）的預測時長。這是對齊至影格網格前的數值。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ebbf6a2601a955122ab9862142aa475524c1f38403f4ef8dc9ffee6456ee8ce5`
