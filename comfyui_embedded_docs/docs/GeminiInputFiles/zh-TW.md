## 概述

載入並格式化輸入檔案，以供 Gemini API 使用。此節點允許使用者將文字（.txt）和 PDF（.pdf）檔案作為輸入上下文包含在 Gemini 模型中。檔案會被轉換為 API 所需的適當格式，並且可以串聯在一起，以便在單一請求中包含多個檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `檔案` | 要作為模型上下文包含的輸入檔案。目前僅接受文字（.txt）和 PDF（.pdf）檔案。檔案必須小於最大輸入檔案大小限制。 | COMBO | 是 | 多個選項可用 |
| `GEMINI_INPUT_FILES` | 一個可選的附加檔案，用於與從此節點載入的檔案批次處理。允許串聯輸入檔案，以便單一訊息可以包含多個輸入檔案。 | GEMINI_INPUT_FILES | 否 | 不適用 |

**注意：** `file` 參數僅顯示小於最大輸入檔案大小限制的文字（.txt）和 PDF（.pdf）檔案。檔案會自動按名稱進行篩選和排序。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `GEMINI_INPUT_FILES` | 已格式化的檔案資料，準備好與 Gemini LLM 節點一起使用，其中包含以適當 API 格式載入的檔案內容。 | GEMINI_INPUT_FILES |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/zh-TW.md)

---
**Source fingerprint (SHA-256):** `54da8696d144513efa9660fbc5ddbf5480da12eafe4d2791c8e81cd207ef8a52`
