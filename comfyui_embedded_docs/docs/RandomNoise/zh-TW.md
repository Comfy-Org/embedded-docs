# 隨機雜訊

RandomNoise 節點根據種子值生成隨機雜訊模式。它建立可重現的雜訊，可用於各種影像處理和生成任務。相同的種子永遠會產生相同的雜訊模式，從而在多次運行中獲得一致的結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `noise_seed` | 用於生成隨機雜訊模式的種子值（預設：0）。相同的種子永遠會產生相同的雜訊輸出。啟用生成後控制，允許每次生成後將種子值隨機化、固定、遞增或遞減。 | INT | 是 | 0 到 18446744073709551615 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `noise` | 根據提供的種子值生成的隨機雜訊模式。 | NOISE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`
