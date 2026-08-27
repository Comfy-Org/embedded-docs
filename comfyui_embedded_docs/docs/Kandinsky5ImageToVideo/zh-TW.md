# Kandinsky5ImageToVideo

Kandinsky5ImageToVideo 節點使用 Kandinsky 模型，為影片生成準備 conditioning（條件）與潛在空間（latent space）資料。它會建立一個空的影片潛在張量，並可選擇性地編碼起始影像，以引導生成影片的初始幀，同時相應地修改正向與負向 conditioning。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導影片生成的正向 conditioning 提示。 | CONDITIONING | 是 | N/A |
| `negative` | 用於引導影片生成遠離特定概念的負向 conditioning 提示。 | CONDITIONING | 是 | N/A |
| `vae` | 用於將可選的起始影像編碼到潛在空間的 VAE 模型。 | VAE | 是 | N/A |
| `寬度` | 輸出影片的寬度（以像素為單位，預設值：768）。 | INT | 是 | 16 至 16384 (step 16) |
| `高度` | 輸出影片的高度（以像素為單位，預設值：512）。 | INT | 是 | 16 至 16384 (step 16) |
| `長度` | 影片的幀數（預設值：121）。 | INT | 是 | 1 至 16384 (step 4) |
| `批次大小` | 同時生成的影片序列數量（預設值：1）。 | INT | 是 | 1 至 4096 |
| `起始圖片` | 可選的起始影像或幀批次。若提供，則會將其編碼，並用於取代模型輸出潛在張量的雜訊起始部分。 | IMAGE | 否 | N/A |

**注意：** 提供 `start_image` 時，系統會自動使用雙線性插值將其調整為指定的 `width` 與 `height`。僅使用影像批次中的前 `length` 幀進行編碼；其餘幀會被忽略。若影像批次的幀數少於 `length`，則僅使用這些幀。僅編碼影像的 RGB 通道。編碼後的潛在張量會被注入 `positive` 與 `negative` conditioning，以引導影片的初始外觀；同時，乾淨的編碼幀會取代模型輸出潛在張量的雜訊起始部分。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向 conditioning，可能已更新為帶有編碼起始影像的資料。 | CONDITIONING |
| `negative` | 修改後的負向 conditioning，可能已更新為帶有編碼起始影像的資料。 | CONDITIONING |
| `latent` | 空的影片潛在張量。一個填滿零的潛在張量，其形狀對應於指定的尺寸。 | LATENT |
| `cond_latent` | 乾淨的編碼起始影像，用於取代模型輸出潛在張量的雜訊起始部分。若未提供 `start_image`，則為空。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
