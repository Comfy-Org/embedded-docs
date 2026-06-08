CLIPTextEncodeHiDream 節點使用不同的語言模型（CLIP-L、CLIP-G、T5-XXL 和 LLaMA）處理四個獨立的文字輸入，並將它們組合成單一的條件輸出。它使用對應的模型對每個文字輸入進行標記化，並透過排程編碼方法將它們一起編碼，從而能夠同時利用多個語言模型實現更複雜的文字條件控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於標記化和編碼的 CLIP 模型 | CLIP | 是 | - |
| `clip_l` | 提供給 CLIP-L 模型處理的文字輸入。支援多行文字和動態提示。 | STRING | 是 | - |
| `clip_g` | 提供給 CLIP-G 模型處理的文字輸入。支援多行文字和動態提示。 | STRING | 是 | - |
| `t5xxl` | 提供給 T5-XXL 模型處理的文字輸入。支援多行文字和動態提示。 | STRING | 是 | - |
| `llama` | 提供給 LLaMA 模型處理的文字輸入。支援多行文字和動態提示。 | STRING | 是 | - |

**注意：** 所有四個文字輸入（`clip_l`、`clip_g`、`t5xxl` 和 `llama`）都是正常運作所必需的，因為每個輸入都會透過排程編碼過程對最終的條件輸出做出貢獻。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 來自所有已處理文字輸入的組合條件輸出，使用排程編碼方法進行編碼 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/zh-TW.md)

---
**Source fingerprint (SHA-256):** `51d117d82a9d833f095e874bf442d5cf8c46a12313fda6b98e628fa988797565`
