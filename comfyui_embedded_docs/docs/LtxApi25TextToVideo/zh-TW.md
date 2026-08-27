# LtxApi25TextToVideo

LTX 2.5 Text To Video 是一個 API 節點，使用 LTX 2.5 模型從文字描述產生專業品質的影片。您提供提示詞，並選擇生成設定，例如模型等級、時長、解析度、幀率，以及是否包含音訊；該節點將任務提交至 LTX API，並傳回產生的影片。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片產生的 LTX 2.5 模型等級。 | STRING | 是 | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `時長` | 產生的影片長度。 | INT | 是 | Integer |
| `解析度` | 影片的輸出解析度。可用的選項取決於所選的 `model`。 | STRING | 是 | With "LTX-2.5 (Fast)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840"<br>With "LTX-2.5 (Pro)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920" |
| `幀率` | 產生的影片的幀率（預設：25）。 | INT | 否 | Integer |
| `生成音訊` | 是否在產生影片時同時產生音訊（預設：True）。 | BOOLEAN | 否 | True<br>False |
| `提示詞` | 要產生的影片的文字描述。需要非空白的提示詞，最多 10,000 個字元（預設：""）。 | STRING | 是 | 1 至 10000 characters |
| `種子` | 用於可重現生成的種子值（預設：42）。 | INT | 否 | Integer |

注意：可用的 `model.resolution` 選項取決於所選的 `model`。"LTX-2.5 (Fast)" 支援最高 2160x3840 的解析度，而 "LTX-2.5 (Pro)" 支援最高 1920x1080 的解析度。

## 輸出
| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 由 LTX API 傳回的已產生的影片，可直接在工作流程中進一步使用。如果已啟用音訊產生，影片將包含同步音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25TextToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02e131116fb0760cce2cea1e9bc49fa16dd7e4e296903fef5e44b7942b6e84c9`
