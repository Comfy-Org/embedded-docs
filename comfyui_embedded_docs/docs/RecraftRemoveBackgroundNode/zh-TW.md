# Recraft 去背

此節點使用 Recraft API 服務移除影像背景。它會逐一處理輸入批次中的每張影像，並傳回具有透明背景的處理後影像，以及指示已移除背景區域的相應 Alpha 遮罩。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖片` | 要進行背景移除的輸入影像。批次中的每張影像都會個別處理。 | IMAGE | 是 | - |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 具有透明背景的處理後影像（RGBA 格式） | IMAGE |
| `mask` | 指出已移除背景區域的 Alpha 通道遮罩，格式為 B,H,W | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
