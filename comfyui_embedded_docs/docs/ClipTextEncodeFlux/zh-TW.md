# CLIPTextEncodeFlux

`CLIPTextEncodeFlux` 是一個專為 Flux 架構設計的文字編碼節點。它透過不同的編碼器（CLIP-L 與 T5XXL）處理兩組獨立的文字輸入，並結合引導尺度（guidance scale），產生統一的 conditioning 輸出，以用於影像生成。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 支援 Flux 架構的 CLIP 模型，包含 CLIP-L 與 T5XXL 編碼器。 | CLIP | 是 | - |
| `clip_l` | 由 CLIP-L 編碼器處理的文字輸入。適合簡潔的關鍵字描述，例如風格或主題。支援多行輸入與動態提示詞。 | STRING | 是 | - |
| `t5xxl` | 由 T5XXL 編碼器處理的文字輸入。適合詳細的自然語言描述，可表達複雜場景與細節。支援多行輸入與動態提示詞。 | STRING | 是 | - |
| `guidance` | 控制文字條件對生成過程的影響程度。數值越高表示對文字的遵循越嚴格。預設值：3.5。 | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含來自兩個編碼器的合併嵌入與引導值，用於條件式影像生成。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/zh-TW.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`
