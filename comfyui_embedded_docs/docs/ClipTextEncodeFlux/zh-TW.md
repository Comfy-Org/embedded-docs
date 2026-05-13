> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/zh-TW.md)

## 概述

`CLIPTextEncodeFlux` 是一個專為 Flux 架構設計的先進文字編碼節點。它透過不同的編碼器（CLIP-L 和 T5XXL）處理兩個獨立的文字輸入，並結合引導尺度（guidance scale）產生統一的條件化輸出，用於影像生成。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 支援 Flux 架構的 CLIP 模型，包含 CLIP-L 和 T5XXL 兩個編碼器。 |
| `clip_l` | STRING | 是 | - | 由 CLIP-L 編碼器處理的文字輸入。適合簡潔的關鍵字描述，例如風格或主題。支援多行輸入和動態提示詞。 |
| `t5xxl` | STRING | 是 | - | 由 T5XXL 編碼器處理的文字輸入。適合詳細的自然語言描述，表達複雜場景和細節。支援多行輸入和動態提示詞。 |
| `guidance` | FLOAT | 是 | 0.0 - 100.0 | 控制文字條件對生成過程的影響程度。數值越高表示越嚴格遵循文字描述。預設值：3.5。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含來自兩個編碼器的融合嵌入向量以及引導參數，用於條件化影像生成。 |

---
**Source fingerprint (SHA-256):** `f168610123410a44f9c5c5c18773603bd47bc7b44b21e65910a6026f86d7eb04`
