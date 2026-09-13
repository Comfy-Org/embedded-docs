# CLIPTextEncodeControlnet

CLIP Text Encode (Controlnet) 節點會使用 CLIP 模型對文字提示進行編碼，並將產生的文字編碼加入既有的 conditioning 資料中。它會將文字嵌入儲存為每個 conditioning 項目內的 controlnet 跨注意力參數，因此回傳的 conditioning 會帶有這些額外的 controlnet 資訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於文字分詞與編碼的 CLIP 模型 | CLIP | 是 | - |
| `條件設定` | 要與 CLIP 文字編碼結合的既有 conditioning 資料 | CONDITIONING | 是 | - |
| `文字` | 要由 CLIP 模型處理的文字提示。支援多行文字與動態提示 | STRING | 是 | - |

**注意：** 此節點要能運作，三個輸入（`clip`、`conditioning` 與 `text`）皆為必填。`text` 輸入支援多行文字與動態提示，提供彈性的文字處理。此節點在原始程式碼中被標記為實驗性功能。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 增強的 conditioning 資料，加入了衍生自 CLIP 文字編碼的 controlnet 跨注意力參數（`cross_attn_controlnet` 與 `pooled_output_controlnet`） | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
