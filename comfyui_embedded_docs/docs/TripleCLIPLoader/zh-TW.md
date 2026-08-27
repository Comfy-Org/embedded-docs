# 載入三重 CLIP

TripleCLIPLoader 同時載入三個文字編碼器模型，並將它們組合成單一 CLIP 模型。它用於需要多個文字編碼器協同工作的流程，例如 SD3，其使用 clip-l、clip-g 和 t5 模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_name1` | 要從可用文字編碼器中載入的第一個文字編碼器模型 | COMBO | 是 | 多個可用選項（text_encoders 資料夾中的所有檔案） |
| `clip_name2` | 要從可用文字編碼器中載入的第二個文字編碼器模型 | COMBO | 是 | 多個可用選項（text_encoders 資料夾中的所有檔案） |
| `clip_name3` | 要從可用文字編碼器中載入的第三個文字編碼器模型 | COMBO | 是 | 多個可用選項（text_encoders 資料夾中的所有檔案） |

**注意：** 三個參數皆為必填。可用選項為您的 text_encoders 資料夾中的文字編碼器檔案。若找不到選定的檔案，節點會產生錯誤。此節點會載入所有三個選定的模型，並將它們組合成單一 CLIP 模型。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CLIP` | 包含所有三個已載入文字編碼器的組合 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
