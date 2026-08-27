# Bria 移除影片背景（透明）

此節點使用 Bria 的 AI 服務移除影片背景，並輸出去背後的幀以及一個 alpha 遮罩。將兩個輸出連接到合成節點，或將它們饋送到 Save WEBM 節點以寫入透明影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要處理的輸入影片。影片必須為 60 秒或更短。 | VIDEO | 是 | - |
| `種子` | Seed 控制節點是否應重新執行；無論 seed 為何，結果都是非確定性的（預設值：0） | INT | 是 | 0 至 2147483647 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `影像` | 已移除背景的影片幀，以 RGB 影像呈現，範圍介於 0.0 到 1.0 | IMAGE |
| `遮罩` | 影片幀的 alpha 遮罩，遵循 Load Image 慣例，其中 1 表示透明 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
