# Recraft 去背

此節點使用 Recraft API 服務從影像中移除背景。它會處理輸入批次中的每張影像，並返回具有透明背景的處理後影像，以及指示已移除背景區域的對應 Alpha 遮罩。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要用於移除背景的輸入影像 | IMAGE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 具有透明背景的處理後影像 | IMAGE |
| `mask` | 指示已移除背景區域的 Alpha 通道遮罩 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
