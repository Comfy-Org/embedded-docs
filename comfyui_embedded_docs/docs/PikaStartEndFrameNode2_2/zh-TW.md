## 概述

PikaFrames v2.2 節點透過結合您的第一幀與最後一幀來生成影片。您上傳兩張圖片來定義起始點與結束點，AI 會在兩者之間建立流暢的過渡，從而產生完整的影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image_start` | 要結合的第一張圖片。 | IMAGE | 是 | - |
| `image_end` | 要結合的最後一張圖片。 | IMAGE | 是 | - |
| `prompt_text` | 描述所需影片內容的文字提示。 | STRING | 是 | - |
| `negative_prompt` | 描述影片中應避免內容的文字。 | STRING | 是 | - |
| `seed` | 用於生成一致性的隨機種子值。 | INT | 是 | - |
| `resolution` | 輸出影片解析度。 | STRING | 是 | - |
| `duration` | 生成影片的持續時間。 | INT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 透過 AI 過渡結合起始幀與結束幀所生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
