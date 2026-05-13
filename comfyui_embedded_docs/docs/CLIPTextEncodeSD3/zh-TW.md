> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/zh-TW.md)

## 概述

CLIPTextEncodeSD3 節點透過使用不同的 CLIP 模型編碼多個文字提示，來處理 Stable Diffusion 3 模型的文字輸入。它處理三個獨立的文字輸入（`clip_g`、`clip_l` 和 `t5xxl`），並提供管理空白文字填充的選項。該節點確保不同文字輸入之間的標記對齊，並返回適用於 SD3 生成管線的條件資料。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 用於文字編碼的 CLIP 模型 |
| `clip_l` | STRING | 是 | - | 本地 CLIP 模型的文字輸入。支援多行文字和動態提示。 |
| `clip_g` | STRING | 是 | - | 全域 CLIP 模型的文字輸入。支援多行文字和動態提示。 |
| `t5xxl` | STRING | 是 | - | T5-XXL 模型的文字輸入。支援多行文字和動態提示。 |
| `empty_padding` | COMBO | 是 | `"none"`<br>`"empty_prompt"` | 控制空白文字輸入的處理方式。設為 "none" 時，`clip_g`、`clip_l` 或 `t5xxl` 的空白文字輸入將產生空標記列表而非填充。這是一個進階參數（預設值："none"）。 |

**參數限制：**

- 當 `empty_padding` 設為 "none" 時，`clip_g`、`clip_l` 或 `t5xxl` 的空白文字輸入將產生空標記列表而非填充
- 當 `clip_l` 和 `clip_g` 輸入的標記長度不同時，節點會自動透過用空標記填充較短者來平衡兩者的標記長度
- 所有文字輸入均支援動態提示和多行文字輸入

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 已編碼的文字條件資料，準備好供 SD3 生成管線使用 |

---
**Source fingerprint (SHA-256):** `38f7538d05fe48e74f41f265550b83906b2f0c5d31f0783f6859f4df7b5cb9d3`
