# MiniMax H3 文生影片

此節點使用 MiniMax H3 系列模型（MiniMax H3、MiniMax H3 Max 與 MiniMax H3 Max Turbo）從文字提示詞生成影片。您需要選擇模型、輸入文字提示詞，並調整解析度、長寬比與時長等設定。此節點會將請求傳送至 MiniMax API，等待生成任務完成，並回傳生成的影片。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片生成的模型（預設："MiniMax H3"）。選擇模型後也會顯示下方各節所述的模型專屬設定。 | DYNAMIC_COMBO | 是 | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `隨機種子` | 隨機種子。使用相同種子的相同請求會產生相似但不保證完全相同的結果（預設：42）。 | INT | 是 | 0 至 4294967295 |
| `浮水印` | 是否在影片中加入 AIGC 浮水印（預設：false）。啟用時僅支援 "MiniMax H3" 模型。 | BOOLEAN | 否 | true<br>false |

### MiniMax H3 輸入

這些設定會在選擇 "MiniMax H3" 模型時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。必須包含至少一個非空白字元。 | STRING | 是 | Any text |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "768P"<br>"2K" |
| `ratio` | 輸出影片的長寬比（預設："16:9"）。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的時長，以秒為單位（4-15）（預設：5）。 | INT | 是 | 4 至 15 |

### MiniMax H3 Max 與 MiniMax H3 Max Turbo 輸入

這些設定由 "MiniMax H3 Max" 與 "MiniMax H3 Max Turbo" 模型共用，並會在選擇任一個模型時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。必須包含至少一個非空白字元，長度最多可達 50,000 個字元。 | STRING | 是 | 最多 50000 個字元 |
| `resolution` | 輸出影片的解析度（預設："768P"）。 | COMBO | 是 | "480P"<br>"768P" |
| `ratio` | 輸出影片的長寬比（預設："16:9"）。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的時長，以秒為單位（5-15）（預設：5）。 | INT | 是 | 5 至 15 |
| `prompt_expansion_mode` | 生成前改寫提示詞所投入的處理程度（預設："balanced"）。 | COMBO | 是 | "balanced"<br>"quality" |

### 注意事項

- 對所有模型而言，提示詞都必須包含至少一個非空白字元。
- `watermark` 設定僅受 "MiniMax H3" 支援。在 "MiniMax H3 Max" 或 "MiniMax H3 Max Turbo" 上啟用會導致錯誤。
- "MiniMax H3 Max" 與 "MiniMax H3 Max Turbo" 模型將提示詞限制為 50,000 個字元。
- 解析度與時長限制取決於所選模型："MiniMax H3" 支援 "768P" 與 "2K" 解析度以及 4-15 秒的影片，而 "MiniMax H3 Max" 與 "MiniMax H3 Max Turbo" 支援 "480P" 與 "768P" 解析度以及 5-15 秒的影片。
- 此節點顯示的預估價格是根據所選模型、解析度與時長計算得出。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 根據所提供的文字提示詞生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4d3de190d18de4370aff878279755e881841d2ada28320a7c1d7c52061071c05`
