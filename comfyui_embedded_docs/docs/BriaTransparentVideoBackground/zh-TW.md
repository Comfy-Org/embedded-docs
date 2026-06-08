# Bria 移除影片背景（透明）

此節點使用 Bria 的 AI 服務移除影片背景，並輸出裁切後的影格以及 Alpha 遮罩。請將兩個輸出連接到合成節點，或將其饋送至 Save WEBM 節點以寫入透明影片。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要處理的輸入影片 | VIDEO | 是 | - |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果皆為非確定性（預設值：0） | INT | 是 | 0 至 2147483647 |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 已移除背景的影片影格 | IMAGE |
| `mask` | 影片影格的 Alpha 遮罩 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `45fb3fc185b5c6420d6ac2b87f2403566e1ef6dcdc57791fb833b6ccb2a64cd9`
