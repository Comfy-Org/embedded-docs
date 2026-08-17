# CLIPTextEncodeHiDream

CLIPTextEncodeHiDream 節點使用不同的語言模型（CLIP-L、CLIP-G、T5-XXL 與 LLaMA）處理四個獨立的文字輸入，並將它們組合成單一條件化（conditioning）輸出。它使用對應的模型對每個文字輸入進行詞元化（tokenize），並透過排程編碼方法將它們一起編碼，藉由同時利用多個語言模型來實現更精密的文字條件化。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於詞元化和編碼的 CLIP 模型 | CLIP | 是 | - |
| `clip_l` | 供 CLIP-L 模型處理的文字輸入。支援多行文字與動態提示詞。 | STRING | 是 | - |
| `clip_g` | 供 CLIP-G 模型處理的文字輸入。支援多行文字與動態提示詞。 | STRING | 是 | - |
| `t5xxl` | 供 T5-XXL 模型處理的文字輸入。支援多行文字與動態提示詞。 | STRING | 是 | - |
| `llama` | 供 LLaMA 模型處理的文字輸入。支援多行文字與動態提示詞。 | STRING | 是 | - |

**注意：** 所有四個文字輸入（`clip_l`、`clip_g`、`t5xxl` 與 `llama`）皆為正常運作所必需，因為每個輸入都會透過排程編碼過程貢獻於最終的條件化輸出。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `CONDITIONING` | 來自所有已處理文字輸入的組合條件化輸出，使用排程編碼方法進行編碼 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c5e269c17bd2dd7d7171c02598a87983a988d953dd7df285978fc25a9c896e46`
