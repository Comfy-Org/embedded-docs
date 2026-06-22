# Recraft 去背

此節點使用 Recraft API 服務從圖像中移除背景。它會處理輸入批次中的每張圖像，並返回帶有透明背景的處理後圖像，以及指示已移除背景區域的對應 Alpha 遮罩。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖片` | 要進行背景移除處理的輸入圖像 | IMAGE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `圖片` | 帶有透明背景的處理後圖像 | IMAGE |
| `mask` | 指示已移除背景區域的 Alpha 通道遮罩 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9e3f1a0471da3afda6b8de26de3b7e78c1070c49ab49e4fc8b6b79bb10ff77de`
