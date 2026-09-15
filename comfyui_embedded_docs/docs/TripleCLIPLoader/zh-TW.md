# 載入三重 CLIP

TripleCLIPLoader 會同時載入三個文字編碼器模型，並將它們組合成單一的 CLIP 模型。它適用於需要多個文字編碼器協同運作的工作流程，例如 SD3，其使用了 clip-l、clip-g 和 t5 模型。

SD3 的常見組合配方為：clip-l、clip-g、t5。

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip_name1` | 要從可用文字編碼器中載入的第一個文字編碼器模型 | COMBO | 是 | 有多個選項可用（text_encoders 資料夾中的所有檔案） |
| `clip_name2` | 要從可用文字編碼器中載入的第二個文字編碼器模型 | COMBO | 是 | 有多個選項可用（text_encoders 資料夾中的所有檔案） |
| `clip_name3` | 要從可用文字編碼器中載入的第三個文字編碼器模型 | COMBO | 是 | 有多個選項可用（text_encoders 資料夾中的所有檔案） |

**注意：** 三個參數皆為必填。可用的選項為您 text_encoders 資料夾中的文字編碼器檔案。若找不到所選的檔案，此節點會引發錯誤。此節點會載入全部三個所選模型，並將它們組合成單一的 CLIP 模型。

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `CLIP` | 包含全部三個已載入文字編碼器的組合 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
