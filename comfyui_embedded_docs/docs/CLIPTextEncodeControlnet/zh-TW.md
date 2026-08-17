# CLIPTextEncodeControlnet

CLIPTextEncodeControlnet 節點使用 CLIP 模型處理文字輸入，並將其與既有的 conditioning 資料結合，以建立增強的 conditioning 輸出，供 controlnet 應用程式使用。它會對輸入文字進行分詞，透過 CLIP 模型進行編碼，並將產生的 embeddings 作為交叉注意力 controlnet 參數新增到提供的 conditioning 資料中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於文字分詞和編碼的 CLIP 模型 | CLIP | 是 | - |
| `conditioning` | 既有的 conditioning 資料，將加入 controlnet 參數以進行增強 | CONDITIONING | 是 | - |
| `text` | 要由 CLIP 模型處理的文字輸入。支援多行文字和動態提示詞 | STRING | 是 | - |

**注意：** 此節點需要全部三個輸入（`clip`、`conditioning` 和 `text`）才能正常運作。`text` 輸入支援動態提示詞和多行文字，以提供靈活的文字處理。此節點標記為實驗性。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 增強的 conditioning 資料，包含從 CLIP 文字編碼衍生的 controlnet 交叉注意力參數（`cross_attn_controlnet` 和 `pooled_output_controlnet`） | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
