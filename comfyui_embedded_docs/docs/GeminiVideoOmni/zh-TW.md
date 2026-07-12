# Google Gemini Omni（影片）

使用 Google 的 Gemini Omni Flash 模型，從文字提示生成帶音訊的影片。可選擇提供參考圖像及／或影片以引導或編輯結果。請直接在提示中描述所需長度（3-10 秒）及長寬比（16:9 或 9:16）。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成影片的 Gemini 影片模型。 | MODEL | Yes | "Omni Flash" |
| `seed` | Seed 控制此節點是否重新執行；無論 seed 為何，結果皆為非決定性。 | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/zh-TW.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
