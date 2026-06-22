# OpenAI ChatGPT 輸入文件

## 概述

載入並格式化 OpenAI API 的輸入檔案。此節點負責準備文字檔（.txt）與 PDF 檔（.pdf），以作為 OpenAI 聊天節點的上下文輸入。當生成回應時，OpenAI 模型將會讀取這些檔案。您可以將多個 OpenAI 輸入檔案節點串聯在一起，以便在單一訊息中包含多個檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `file` | 作為模型上下文的輸入檔案。目前僅接受文字檔（.txt）與 PDF 檔（.pdf）。檔案大小必須小於 32MB。 | COMBO | 是 | 提供多個選項（輸入目錄中所有小於 32MB 的 .txt 與 .pdf 檔案） |
| `OPENAI_INPUT_FILES` | 可選的附加檔案，可與此節點載入的檔案批次處理。允許串聯輸入檔案，使單一訊息能夠包含多個輸入檔案。 | OPENAI_INPUT_FILES | 否 | 不適用 |

**檔案限制：**

- 僅支援 .txt 與 .pdf 檔案
- 最大檔案大小：32MB
- 檔案從 ComfyUI 輸入目錄載入

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `OPENAI_INPUT_FILES` | 已格式化的輸入檔案，準備好作為 OpenAI API 呼叫的上下文使用。 | OPENAI_INPUT_FILES |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e5e92f6628072da9af787867e38c89dde3db853b7289ef6c607a066cd04c1cc9`
