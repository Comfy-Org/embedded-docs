# SenseNova 取樣選項

SenseNova Sampling Options 會在模型上設定 SenseNova flow shift。它會複製輸入模型，使用所選的 flow shift 值附加 SenseNova 模型取樣設定，並傳回已套用修補的模型，供取樣時使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用 SenseNova flow shift 取樣設定的模型。 | MODEL | 是 | - |
| `shift` | 要在 SenseNova 模型取樣上設定的 flow shift 值（預設值：3.0；UI 步進：0.01）。 | FLOAT | 是 | 未定義最小值或最大值 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 輸入模型的複本，已將 SenseNova flow shift 套用至其取樣設定。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
