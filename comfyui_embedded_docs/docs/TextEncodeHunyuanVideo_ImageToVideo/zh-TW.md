> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/zh-TW.md)

## 概述

TextEncodeHunyuanVideo_ImageToVideo 節點透過將文字提示與圖像嵌入結合，為影片生成建立條件資料。它使用 CLIP 模型處理文字輸入以及來自 CLIP 視覺輸出的視覺資訊，然後根據指定的圖像交錯設定生成融合這兩種來源的令牌。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 用於分詞和編碼的 CLIP 模型 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 是 | - | 來自 CLIP 視覺模型的視覺嵌入，提供圖像上下文 |
| `prompt` | STRING | 是 | - | 引導影片生成過程的文字描述，支援多行輸入和動態提示詞 |
| `image_interleave` | INT | 是 | 1-512 | 控制圖像相對於文字提示的影響程度。數值越高表示文字提示的影響力越大。（預設值：2） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 結合文字與圖像資訊以用於影片生成的條件資料 |

---
**Source fingerprint (SHA-256):** `ee748bd1fb1733593eb4cb1187c5cc279171163cfbc389f039378d0e366fc231`
