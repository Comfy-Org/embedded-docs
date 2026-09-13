# 種子

Seed 節點提供一個整數值，可用作 `seed` 來控制其他節點中隨機操作的可重現性。透過提供一致的起始值，它有助於在需要時讓生成的結果保持可重現。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `種子` | 要使用的 `seed` 值。control after generate 選項決定該值在每次生成後保持固定還是改變；在此節點中，它設定為 fixed。 | INT | 是 | 0 至 9223372036854775807 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `seed` | 生成的 `seed` 值。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`
