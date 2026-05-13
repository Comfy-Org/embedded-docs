> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/zh-TW.md)

# Runway 影像轉影片（Gen4 Turbo）節點

Runway 影像轉影片（Gen4 Turbo）節點使用 Runway 的 Gen4 Turbo 模型，從單一起始影格生成影片。它接收文字提示和初始影像影格，然後根據提供的持續時間和長寬比設定建立影片序列。此節點負責將起始影格上傳至 Runway 的 API，並返回生成的影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `提示詞` | STRING | 是 | - | 用於生成的文字提示（預設：空字串） |
| `start_frame` | IMAGE | 是 | - | 用於影片的起始影格 |
| `duration` | COMBO | 是 | `"5"`<br>`"10"` | 影片持續時間（秒）（預設："5"） |
| `ratio` | COMBO | 是 | `"1024:1024"`<br>`"1280:720"`<br>`"720:1280"`<br>`"1920:1080"`<br>`"1080:1920"`<br>`"2048:1080"`<br>`"1080:2048"` | 生成影片的長寬比（預設："1024:1024"） |
| `seed` | INT | 否 | 0 至 4294967295 | 用於生成的隨機種子（預設：0） |

**參數限制：**

- `start_frame` 影像的尺寸不得超過 7999x7999 像素
- `start_frame` 影像的長寬比必須介於 0.5 至 2.0 之間
- `prompt` 必須包含至少一個字元

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據輸入影格和提示生成的影片 |

---
**Source fingerprint (SHA-256):** `ebb5f1cd5e6bf6e0fcfb4910c774c087980daf9a1987900ad966120608b924e7`
