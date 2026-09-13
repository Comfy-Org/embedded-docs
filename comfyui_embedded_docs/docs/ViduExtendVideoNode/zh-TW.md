# Vidu 影片延伸

Vidu Video Extension 節點會產生額外影格，以延長現有影片的長度。它會使用指定的 AI 模型，根據來源影片與選用文字提示來產生接續內容。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片延伸的模型。選取模型後會顯示其特定的 `duration` 與 `resolution` 設定。 | DYNAMIC_COMBO | 是 | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `video` | 要延伸的來源影片。 | VIDEO | 是 | - |
| `prompt` | 延伸影片的選用文字提示（最多 2000 個字元；預設：空）。 | STRING | 是 | - |
| `seed` | 用於控制生成隨機性的種子值（預設：1）。 | INT | 是 | 0 至 2147483647 |
| `end_frame` | 選用影像，用作延伸的目標結束影格。 | IMAGE | 否 | - |

### viduq2-pro 與 viduq2-turbo 輸入

這些設定由兩個模型共用。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `duration` | 延伸影片的長度，以秒為單位（預設：4）。此設定會在選取模型後顯示。 | INT | 是 | 1 至 7 |
| `resolution` | 輸出影片的解析度。此設定會在選取模型後顯示。 | COMBO | 是 | `"720p"`<br>`"1080p"` |

**注意：** 來源 `video` 的長度必須介於 4 到 55 秒之間。若有提供 `end_frame`，其長寬比必須介於 1:4 到 4:1 之間，且寬度和高度都必須至少為 128 像素。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 新產生的影片檔案，包含延伸後的影片內容。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`
