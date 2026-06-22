# Recraft 風格 - 無限風格庫

## 概述

此節點允許您使用既有的 UUID 從 Recraft 的無限風格庫中選取一種風格。它會根據提供的風格識別碼擷取風格資訊，並將其傳回以供其他 Recraft 節點使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `style_id` | 來自無限風格庫的風格 UUID。 | STRING | 是 | 任何有效的 UUID |

**注意：** `style_id` 輸入不能為空。如果提供了空字串，節點將會引發例外。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `recraft_style` | 從 Recraft 無限風格庫中選取的風格物件 | STYLEV3 |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/zh-TW.md)

---
**Source fingerprint (SHA-256):** `37d7d9eff1232cc17912c6fca908dc5b8c404c0b6cf0a36e8fecc837ff2a1eea`
