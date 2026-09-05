# SenseNovaSamplingOptions

SenseNova Sampling Options 會在模型上設定 SenseNova 的流偏移（flow shift）。它會複製輸入模型，使用所選的流偏移值附加 SenseNova 模型取樣設定，並傳回修補後的模型以供取樣期間使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用 SenseNova 流偏移取樣設定的模型。 | MODEL | 是 | - |
| `shift` | 要在 SenseNova 模型取樣上設定的流偏移值（預設：3.0；UI 步進：0.01）。 | FLOAT | 是 | 未定義最小值或最大值 |

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 輸入模型的複製品，其取樣設定已套用 SenseNova 流偏移。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
