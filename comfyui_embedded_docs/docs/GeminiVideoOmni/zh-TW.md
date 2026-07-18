# Google Gemini Omni（影片）

此節點使用 Google 的 Gemini Omni Flash 模型，根據文字提示生成附帶音訊的影片。您可以選擇性地提供參考圖片或影片來引導或編輯結果。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `model` | 用於生成影片的 Gemini 影片模型。 | COMBO | 是 | `"Omni Flash"` |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆非確定性。（預設值：42） | INT | 是 | 0 至 2147483647 |

**注意：** `model` 參數是一個動態下拉選單，當選擇「Omni Flash」時會展開以包含其他輸入。這些額外輸入包括：
- `prompt`（STRING，必要）：描述所需影片的文字提示。請直接在提示中描述所需的長度（3-10 秒）和長寬比（16:9 或 9:16）。
- `images`（IMAGE，選用）：用於引導影片生成的參考圖片。最多 14 張圖片。
- `videos`（VIDEO，選用）：用於引導影片生成的參考影片。最多 3 個影片，每個影片最長 10 秒。
- `temperature`（FLOAT，選用，預設值：1.0）：控制生成過程中的隨機性。
- `top_p`（FLOAT，選用，預設值：0.95）：控制核心採樣。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|----------|------|----------|
| `video` | 生成的附帶音訊的影片。 | VIDEO |
| `text` | 模型回傳的文字回應（如有）。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/zh-TW.md)

---
**Source fingerprint (SHA-256):** `948eb712ca0ad3b7d3c7b3a9e1576f2c52a3575c07d8d52bb727bd9df717caa6`
