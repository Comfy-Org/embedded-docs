# Bria 移除影片背景（透明）

此節點使用 Bria 的 AI 服務移除影片背景，並回傳去除背景的幀以及 Alpha 遮罩。將兩個輸出連接到合成節點，或將它們饋送到 Save WEBM 節點以寫入透明影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要處理的輸入影片。最大時長為 60 秒。 | VIDEO | 是 | - |
| `seed` | Seed 控制節點是否應重新執行；無論 seed 為何，結果都是非確定性的（預設值：0） | INT | 是 | 0 to 2147483647 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 去除背景後的影片幀 | IMAGE |
| `mask` | 影片幀的 Alpha 遮罩，其中 1 表示透明 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
