# Sonilo 文字轉音樂

Sonilo Text to Music 節點使用 Sonilo 的 AI 模型，根據文字描述生成音樂。您提供描述所需音樂的提示詞，節點會向 Sonilo 服務發送請求以建立音訊檔案。您可以為生成的片段設定目標時長。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成之音樂的文字提示詞。去除首尾空白後必須包含 1 到 1000 個字元。 | STRING | 是 | N/A |
| `duration` | 目標時長（秒）。上限：6 分鐘。預設：30。 | INT | 否 | 1 至 360 |
| `seed` | 用於重現的種子。目前被 Sonilo 服務忽略，但保留以維持工作流程圖的一致性。預設：0。 | INT | 否 | 0 至 18446744073709551615 |

**備註：**
- `seed` 輸入參數是為了工作流程一致性而提供，但目前不會影響 Sonilo 服務的輸出。
- 使用費用按所要求的 `duration` 每秒 $0.0025 計費。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 生成的音樂音訊檔案。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
