# MiniMax H3 Sigma Shift

設定 MiniMax H3 模型的影片與音訊流位移值。影片位移控制取樣器的 sigma 排程，兩個位移值都會傳遞給模型的內部 Transformer，Transformer 會使用它們從共享的基礎網格推導出音訊排程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用 sigma 位移修補的模型。節點會複製模型，因此原始模型保持不變。 | MODEL | 是 | - |
| `shift_video` | 影片流位移值。它驅動取樣器的 sigma 排程。預設值：12.0。 | FLOAT | 是 | 0.01 至 100.0 |
| `shift_audio` | 音訊流位移值。模型用它來推導音訊排程。預設值：3.0。 | FLOAT | 是 | 0.01 至 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已套用影片與音訊 sigma 位移設定的複製模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3SigmaShift/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0f731585cc1a9c87a3e54341757c4cf4e490d1d4718ecf458bd2b9f4378af63f`
