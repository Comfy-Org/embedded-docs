# Sonilo 文字轉音樂

Sonilo Text to Music 節點使用 Sonilo 的 AI 模型，根據文字描述生成音樂。您提供描述所需音樂的提示詞，節點便會向 Sonilo 服務發送請求，以建立音訊檔案。您也可以指定生成音樂的目標時長。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成音樂的文字提示。必須包含 1 到 1000 個字元。 | STRING | 是 | 1 to 1000 characters |
| `duration` | 目標時長（秒）。最長 6 分鐘。預設：30。 | INT | 否 | 1 to 360 |
| `seed` | 用於可重現性的種子。目前 Sonilo 服務會忽略此參數，但為了工作流圖一致性而保留。預設：0。 | INT | 否 | 0 to 18446744073709551615 |

**注意：** `seed` 輸入是為了工作流一致性而提供，目前不會影響 Sonilo 服務的輸出。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 生成的音樂音訊檔案。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
