# 載入三重 CLIP

TripleCLIPLoader 節點同時載入三個文字編碼器模型，並將它們組合成單一 CLIP 模型。這對於需要多個文字編碼器的進階文字編碼情境非常有用，例如在需要 clip-l、clip-g 和 t5 模型共同運作的 SD3 工作流程中。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_name1` | 從可用的文字編碼器中載入的第一個文字編碼器模型 | COMBO | 是 | text_encoders 資料夾中的所有文字編碼器檔案 |
| `clip_name2` | 從可用的文字編碼器中載入的第二個文字編碼器模型 | COMBO | 是 | text_encoders 資料夾中的所有文字編碼器檔案 |
| `clip_name3` | 從可用的文字編碼器中載入的第三個文字編碼器模型 | COMBO | 是 | text_encoders 資料夾中的所有文字編碼器檔案 |

**注意：** 所有三個文字編碼器參數都必須從系統中可用的文字編碼器模型中選取。節點會以指定順序載入全部三個模型，並將它們組合成單一 CLIP 模型進行處理。對於 SD3 工作流程，請使用 clip-l、clip-g 和 t5 作為三個編碼器。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-----------|-------------|-----------|
| `CLIP` | 包含所有三個已載入文字編碼器的組合 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
