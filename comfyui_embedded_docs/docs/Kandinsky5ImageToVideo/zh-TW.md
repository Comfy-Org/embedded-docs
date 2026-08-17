# Kandinsky5ImageToVideo

Kandinsky5ImageToVideo 節點使用 Kandinsky 模型為影片生成準備 conditioning 與潛在空間資料。它會建立一個空的影片潛在張量，並可選擇性地編碼起始影像，以引導生成影片的初始幀，同時相應地修改正向與負向 conditioning。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導影片生成的正向 conditioning 提示。 | CONDITIONING | 是 | N/A |
| `negative` | 用於使影片生成避開特定概念的負向 conditioning 提示。 | CONDITIONING | 是 | N/A |
| `vae` | 用於將可選起始影像編碼至潛在空間的 VAE 模型。 | VAE | 是 | N/A |
| `width` | 輸出影片的寬度（像素，預設值：768）。 | INT | 是 | 16 至 8192（步長 16） |
| `height` | 輸出影片的高度（像素，預設值：512）。 | INT | 是 | 16 至 8192（步長 16） |
| `length` | 影片的影格數（預設值：121）。 | INT | 是 | 1 至 8192（步長 4） |
| `batch_size` | 同時生成的影片序列數（預設值：1）。 | INT | 是 | 1 至 4096 |
| `start_image` | 可選的起始影像。若提供，則將其編碼並用於取代模型輸出潛在空間的雜訊起始部分。 | IMAGE | 否 | N/A |

**注意：** 當提供了 `start_image` 時，會使用雙線性插值將其調整為指定的 `width` 與 `height`。僅使用影像的前 `length` 個影格進行編碼。編碼後的潛在空間會連同標記起始影格的遮罩一起注入 `positive` 與 `negative` conditioning，使乾淨的編碼影像取代生成影片開頭的雜訊部分。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向 conditioning，可能已使用編碼的起始影像資料進行更新。 | CONDITIONING |
| `negative` | 修改後的負向 conditioning，可能已使用編碼的起始影像資料進行更新。 | CONDITIONING |
| `latent` | 以零填充的空影片潛在張量，形狀依指定的 `batch_size`、`length`、`height` 與 `width` 而定。 | LATENT |
| `cond_latent` | 所提供起始影像的乾淨編碼潛在表示。用於取代模型輸出潛在空間的雜訊起始部分。若未提供 `start_image`，則為空。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
