# 字典轉字串

此節點將字典（鍵值對的集合）轉換為文字字串，通常採用 JSON 格式。您可以控制縮排層級，使輸出更易於閱讀或更為精簡。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `字典` | 要轉換為字串的字典 | DICT | 是 | - |
| `縮排` | 每個縮排層級的空格數。設為 0 會產生緊湊的單行字串（預設值：2） | INT | 否 | 0 至 8 |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `STRING` | 轉換為 JSON 格式字串的字典 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertDictionaryToString/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ae4e9889d5347acfc69166bac66f2ba63f5cd37dafab25a9e0aff6bfe7381219`
