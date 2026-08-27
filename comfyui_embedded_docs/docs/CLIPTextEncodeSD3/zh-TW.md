# CLIPTextEncodeSD3

CLIPTextEncodeSD3 透過使用不同的 CLIP 模型對多個文字提示進行編碼，來處理 Stable Diffusion 3 模型的文字輸入。它處理三個獨立的文字輸入（`clip_g`、`clip_l` 和 `t5xxl`），並提供管理空文字填充的選項。此節點確保不同文字輸入之間的正確 token 對齊，並返回適用於 SD3 生成管線的 conditioning 數據。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於文字編碼的 CLIP 模型 | CLIP | 是 | - |
| `clip_l` | 供本地（local）CLIP 模型使用的文字輸入。支援多行文字和動態提示詞。 | STRING | 是 | - |
| `clip_g` | 供全域（global）CLIP 模型使用的文字輸入。支援多行文字和動態提示詞。 | STRING | 是 | - |
| `t5xxl` | 供 T5-XXL 模型使用的文字輸入。支援多行文字和動態提示詞。 | STRING | 是 | - |
| `空白填充` | 控制空文字輸入的處理方式。設定為「"none"」時，`clip_g`、`clip_l` 或 `t5xxl` 的空文字輸入會產生空 token 列表，而不是填充。設定為「"empty_prompt"」時，空輸入會作為空提示詞進行 token 化（標準填充行為）。這是一個進階參數（預設值："none"）。 | COMBO | 是 | `"none"`<br>`"empty_prompt"` |

**參數限制：**

- 當 `empty_padding` 設定為「"none"」時，`clip_g`、`clip_l` 或 `t5xxl` 的空文字輸入會產生空 token 列表，而不是填充。
- 當長度不同時，此節點會透過用空 token 填充較短的輸入，自動平衡 `clip_l` 和 `clip_g` 輸入之間的 token 長度。
- 所有文字輸入均支援動態提示詞和多行文字輸入。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 已編碼的文字 conditioning 數據，可直接用於 SD3 生成管線 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `874869bac024e6b5ac6b4bf4f79c31bb750e54f7096f6638647aac6b95bb202f`
