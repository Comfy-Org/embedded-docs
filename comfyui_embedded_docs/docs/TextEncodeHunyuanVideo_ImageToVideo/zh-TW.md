# 文字編碼 HunyuanVideo 影像轉影片

TextEncodeHunyuanVideo_ImageToVideo 節點透過將文字提示與參考影像的視覺資訊結合，建立用於影像轉影片生成的 conditioning 資料。它使用 CLIP 模型來處理文字和來自 CLIP 視覺輸出的影像嵌入，然後根據 `image_interleave` 設定產生將這兩種來源混合的 tokens。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於分詞和編碼的 CLIP 模型。 | CLIP | 是 | - |
| `clip_vision_output` | 來自 CLIP 視覺模型的視覺嵌入，為參考影像提供影像上下文。 | CLIP_VISION_OUTPUT | 是 | - |
| `提示詞` | 引導影片生成的文字描述。支援多行輸入和動態提示。提示會使用範本格式化，要求模型根據參考影像描述影片，涵蓋主要內容、物體細節、動作、背景和攝影角度等方面。 | STRING | 是 | - |
| `影像交錯` | 影像相對於文字提示的影響程度。數字越大表示文字提示的影響越大。（預設值：2） | INT | 是 | 1-512 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 結合文字和影像資訊以用於影片生成的 conditioning 資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
