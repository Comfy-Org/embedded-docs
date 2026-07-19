# Pikaswaps

## 概述

Pika Swaps 節點可將影片中的物件或區域替換為新的圖像。您可以使用遮罩定義要替換的區域，此節點會在整個影片序列中無縫地替換指定的內容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要替換其中物件的影片。 | VIDEO | 是 | - |
| `image` | 用於替換影片中遮罩物件的圖像。 | IMAGE | 是 | - |
| `mask` | 使用遮罩定義影片中要替換的區域。 | MASK | 是 | - |
| `prompt_text` | 描述所需替換內容的文字提示。 | STRING | 是 | - |
| `negative_prompt` | 描述替換時應避免內容的文字提示。 | STRING | 是 | - |
| `seed` | 用於產生一致結果的隨機種子值。 | INT | 是 | 0 至 4294967295 |

**注意：** 此節點需要提供所有輸入參數。`video`、`image` 和 `mask` 共同定義替換操作，其中遮罩指定影片中哪些區域將被提供的圖像所取代。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 已處理完成的影片，其中指定的物件或區域已被替換。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/zh-TW.md)

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`
