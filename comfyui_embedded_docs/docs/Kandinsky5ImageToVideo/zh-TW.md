> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/zh-TW.md)

Kandinsky5ImageToVideo 節點使用 Kandinsky 模型為影片生成準備條件設定（conditioning）與潛在空間（latent space）資料。它會建立一個空的影片潛在張量，並可選擇性地對起始影像進行編碼，以引導生成影片的初始幀，並相應地修改正向與負向條件設定。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | 不適用 | 引導影片生成的正向條件提示。 |
| `negative` | CONDITIONING | 是 | 不適用 | 引導影片避開特定概念的正向條件提示。 |
| `vae` | VAE | 是 | 不適用 | 用於將可選起始影像編碼至潛在空間的 VAE 模型。 |
| `width` | INT | 否 | 16 至 8192（步長 16） | 輸出影片的寬度（像素），預設值：768。 |
| `height` | INT | 否 | 16 至 8192（步長 16） | 輸出影片的高度（像素），預設值：512。 |
| `length` | INT | 否 | 1 至 8192（步長 4） | 影片的幀數，預設值：121。 |
| `batch_size` | INT | 否 | 1 至 4096 | 同時生成的影片序列數量，預設值：1。 |
| `start_image` | IMAGE | 否 | 不適用 | 可選的起始影像。若提供，則會對其進行編碼，並用於取代模型輸出潛在空間中的雜訊起始部分。 |

**注意：** 當提供了 `start_image` 時，它會自動使用雙線性插值調整大小，以符合指定的 `width` 與 `height`。系統會使用影像批次中的前 `length` 幀進行編碼。編碼後的潛在空間會被注入到 `positive` 與 `negative` 條件設定中，以引導影片的初始外觀。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改後的正向條件設定，可能已更新編碼後的起始影像資料。 |
| `negative` | CONDITIONING | 修改後的負向條件設定，可能已更新編碼後的起始影像資料。 |
| `latent` | LATENT | 一個充滿零值的空影片潛在張量，其形狀符合指定的尺寸。 |
| `cond_latent` | LATENT | 所提供起始影像的乾淨編碼潛在表示。內部用於取代生成影片潛在空間中帶有雜訊的起始部分。 |

---
**Source fingerprint (SHA-256):** `19d3b60be18f5adcd659563329988bce2511a1b27b33fd0ab3a9d93e265557f2`
