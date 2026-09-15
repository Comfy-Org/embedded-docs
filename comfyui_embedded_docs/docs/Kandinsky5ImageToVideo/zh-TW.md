# Kandinsky5ImageToVideo

Kandinsky5ImageToVideo 節點會準備使用 Kandinsky 模型進行影片生成所需的條件與潛在資料。它會建立一個空的影片潛在表示，其大小符合所要求的寬度、高度、長度與批次大小，並且可選擇性地編碼起始影像，透過更新正向與負向條件來引導所生成影片的初始影格。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導影片生成的正向條件提示。 | CONDITIONING | 是 | N/A |
| `negative` | 用於引導影片生成遠離特定概念的負向條件提示。 | CONDITIONING | 是 | N/A |
| `vae` | 用於將可選起始影像編碼至潛在空間的 VAE 模型。 | VAE | 是 | N/A |
| `寬度` | 輸出影片的寬度，單位為像素（預設：768）。 | INT | 是 | 16 至 16384 （步進值：16） |
| `高度` | 輸出影片的高度，單位為像素（預設：512）。 | INT | 是 | 16 至 16384 （步進值：16） |
| `長度` | 影片的影格數（預設：121）。 | INT | 是 | 1 至 16384 （步進值：4） |
| `批次大小` | 同時生成的影片序列數量（預設：1）。 | INT | 是 | 1 至 4096 |
| `起始圖片` | 可選的起始影像或影格批次。若提供，會將其編碼並用於取代模型輸出潛在表示中帶雜訊的起始部分。 | IMAGE | 否 | N/A |

**注意：** 當提供 `start_image` 時，會使用雙線性插值將其自動調整大小以符合指定的 `width` 和 `height`。影像批次中僅前 `length` 個影格會用於編碼；任何額外的影格都會被忽略。若影像批次的影格數少於 `length`，則僅使用那些影格。僅會編碼影像的 RGB 通道。編碼後的潛在表示接著會注入到 `positive` 和 `negative` 條件中，以引導影片的初始外觀，而乾淨的編碼影格會取代模型輸出潛在表示中帶雜訊的起始部分。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向條件；當提供 `start_image` 時，會以編碼後的起始影像資料更新。 | CONDITIONING |
| `negative` | 修改後的負向條件；當提供 `start_image` 時，會以編碼後的起始影像資料更新。 | CONDITIONING |
| `latent` | 空的影片潛在表示。一個填滿零的潛在張量，其形狀符合指定的維度。 | LATENT |
| `cond_latent` | 乾淨的編碼起始影像，用於取代模型輸出潛在表示中帶雜訊的起始部分。未提供 `start_image` 時為空。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
