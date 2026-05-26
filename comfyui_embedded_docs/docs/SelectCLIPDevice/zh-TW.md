> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/zh-TW.md)

## 概述

Select CLIP Device（選擇 CLIP 裝置）節點讓您能夠選擇 CLIP 文字編碼器運行的裝置（CPU 或特定 GPU）。預設情況下，裝置由模型載入器指定，但您可以覆蓋此設定，改為使用 CPU 或特定的 GPU。如果請求的裝置在您的機器上不存在，此節點會直接傳遞 CLIP 而不做任何更改，並記錄一則訊息，而不會引發錯誤。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | | 要指派給特定裝置的 CLIP 文字編碼器。 |
| `device` | COMBO | 是 | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` | 放置 CLIP 文字編碼器的裝置。`"default"` 會恢復由載入器指定的裝置。`"cpu"` 會將載入和卸載裝置都固定為 CPU。`"gpu:N"` 會將載入裝置固定為第 N 個可用的 GPU（預設值：`"default"`）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `clip` | CLIP | 指派給所選裝置的 CLIP 文字編碼器；如果請求的裝置不可用，則直接傳遞原始的 CLIP 而不做任何更改。 |

---
**Source fingerprint (SHA-256):** `92af94d9f5eea27095cc008debdf7339d26888a0e2cc8bd71ae9c9ba8718eb01`
