> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/zh-TW.md)

# Moonvalley Marey 影片轉影片節點

Moonvalley Marey 影片轉影片節點可根據文字描述，將輸入影片轉換為新的影片。它使用 Moonvalley API 生成符合提示詞的影片，同時保留原始影片中的動作或姿態特徵。您可以透過文字提示詞和各種生成參數來控制輸出影片的風格和內容。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 描述要生成的影片（多行輸入） |
| `negative_prompt` | STRING | 否 | - | 負面提示詞文字（預設：廣泛的負面描述詞列表） |
| `seed` | INT | 是 | 0 至 4294967295 | 隨機種子值（預設：9） |
| `video` | VIDEO | 是 | - | 用於生成輸出影片的參考影片。長度必須至少 5 秒。超過 5 秒的影片將自動裁剪。僅支援 MP4 格式。 |
| `control_type` | COMBO | 否 | "Motion Transfer"<br>"Pose Transfer" | 控制類型選擇（預設："Motion Transfer"） |
| `motion_intensity` | INT | 否 | 0 至 100 | 僅在 control_type 為 "Motion Transfer" 時使用（預設：100） |
| `steps` | INT | 是 | 1 至 100 | 推論步數（預設：33） |

**注意：** `motion_intensity` 參數僅在 `control_type` 設定為 "Motion Transfer" 時生效。使用 "Pose Transfer" 時，此參數將被忽略。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片輸出 |

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
