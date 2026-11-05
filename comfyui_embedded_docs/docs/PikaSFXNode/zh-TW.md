# Pika SFX

此節點使用 Pika 根據文字描述生成音效。描述聲音內容及其應持續的時間，節點會回傳一段音訊片段。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 音效應該是什麼。不得為空。預設值：""（空字串）。 | STRING | 是 | 1 至 4000 個字元 |
| `duration` | 音效的長度，以秒為單位。預設值：5.0。 | FLOAT | 是 | 1.0 至 20.0（步進值：0.1） |
| `seed` | 取樣用的種子。預設值：42。 | INT | 是 | 0 至 2147483647 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `AUDIO` | 生成的音效。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSFXNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a1dcd374d158009aceae2aecd87ed08f8105bff7db75160a99e8624be9459dfa`
