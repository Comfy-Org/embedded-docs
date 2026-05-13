> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/zh-TW.md)

# Moonvalley Marey 文字轉影片節點

Moonvalley Marey 文字轉影片節點使用 Moonvalley API 從文字描述生成影片內容。它接收文字提示詞，並將其轉換為具有可自訂解析度、品質和風格的影片。此節點處理從發送生成請求到下載最終影片輸出的整個過程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 要生成的影片內容的文字描述 |
| `negative_prompt` | STRING | 否 | - | 負面提示詞文字（預設：廣泛的排除元素列表，如合成、場景切換、偽影、雜訊等） |
| `resolution` | STRING | 否 | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" | 輸出影片的解析度（預設："16:9 (1920 x 1080)"） |
| `prompt_adherence` | FLOAT | 否 | 1.0-20.0 | 生成控制的引導尺度（預設：4.0） |
| `seed` | INT | 否 | 0-4294967295 | 隨機種子值（預設：9） |
| `steps` | INT | 否 | 1-100 | 推理步數（預設：33） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 根據文字提示詞生成的影片輸出 |

---
**Source fingerprint (SHA-256):** `3654043567d7aca3af741d706ee07a8d2e28dbeb4b5b8755514b790aa7c1bd41`
