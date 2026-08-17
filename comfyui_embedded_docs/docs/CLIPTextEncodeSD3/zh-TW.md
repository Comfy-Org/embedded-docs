# CLIPTextEncodeSD3

CLIPTextEncodeSD3 節點透過使用不同的 CLIP 模型編碼多個文字提示，來處理 Stable Diffusion 3 模型的文字輸入。它處理三個獨立的文字輸入（`clip_g`、`clip_l` 和 `t5xxl`），並提供管理空文字填充的選項。該節點確保不同文字輸入之間的 token 對齊正確，並回傳適用於 SD3 生成管線的 conditioning 資料。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於文字編碼的 CLIP 模型 | CLIP | 是 | - |
| `clip_l` | 本地 CLIP 模型的文字輸入。支援多行文字和動態提示。 | STRING | 是 | - |
| `clip_g` | 全局 CLIP 模型的文字輸入。支援多行文字和動態提示。 | STRING | 是 | - |
| `t5xxl` | T5-XXL 模型的文字輸入。支援多行文字和動態提示。 | STRING | 是 | - |
| `empty_padding` | 控制如何處理空文字輸入。設為 "none" 時，`clip_g`、`clip_l` 或 `t5xxl` 的空文字輸入將產生空的 token 列表而不是填充。這是進階參數（預設值："none"）。 | COMBO | 是 | `"none"`<br>`"empty_prompt"` |

**參數約束：**

- 當 `empty_padding` 設為 "none" 時，`clip_g`、`clip_l` 或 `t5xxl` 的空文字輸入將產生空的 token 列表而不是填充。
- 節點會自動平衡 `clip_l` 和 `clip_g` 輸入之間的 token 長度；當長度不同時，用空白 token 填充較短者。
- 所有文字輸入均支援動態提示和多行文字輸入。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 編碼後的文字 conditioning 資料，可直接用於 SD3 生成管線 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `874869bac024e6b5ac6b4bf4f79c31bb750e54f7096f6638647aac6b95bb202f`
