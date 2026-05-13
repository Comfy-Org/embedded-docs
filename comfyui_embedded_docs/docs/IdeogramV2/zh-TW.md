> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/zh-TW.md)

# Ideogram V2 節點

此節點使用 Ideogram V2 AI 模型生成圖像。它接收文字提示和各種生成設定，透過 API 服務創建圖像。該節點支援不同的長寬比、解析度和樣式選項，以自訂輸出圖像。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `提示詞` | STRING | 是 | - | 圖像生成的提示詞（預設：空字串） |
| `加速模式` | BOOLEAN | 否 | - | 是否使用渦輪模式（生成速度更快，但品質可能較低）（預設：False） |
| `長寬比` | COMBO | 否 | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | 圖像生成的長寬比。若解析度未設為 AUTO，則此設定將被忽略。（預設："1:1"） |
| `解析度` | COMBO | 否 | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | 圖像生成的解析度。若未設為 AUTO，則此設定將覆蓋 aspect_ratio 設定。（預設："Auto"） |
| `MagicPrompt 選項` | COMBO | 否 | "AUTO"<br>"ON"<br>"OFF" | 決定生成時是否使用 MagicPrompt（預設："AUTO"） |
| `種子值` | INT | 否 | 0-2147483647 | 生成的隨機種子（預設：0） |
| `風格類型` | COMBO | 否 | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" | 生成的樣式類型（僅限 V2）（預設："NONE"） |
| `排除提示詞` | STRING | 否 | - | 描述要從圖像中排除的內容（預設：空字串） |
| `影像數量` | INT | 否 | 1-8 | 要生成的圖像數量（預設：1） |

**注意：** 當 `resolution` 未設為 "Auto" 時，它會覆蓋 `aspect_ratio` 設定。`num_images` 參數每次生成最多限制為 8 張圖像。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | IMAGE | 從 Ideogram V2 模型生成的圖像 |

---
**Source fingerprint (SHA-256):** `c0ba21cb62ad75212c960e2bf6730a39c6479c7389a58c50968c66cc8964f5e3`
