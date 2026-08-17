# Bria 影片更換背景

使用 Bria 將影片的背景替換為提供的圖像或影片。輸出會保留前景的解析度與影格率；如果背景的長寬比不同，會被拉伸以符合，因此請匹配背景以獲得無失真的結果。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 前景影片，其背景將被替換。 | VIDEO | 是 | - |
| `background_image` | 合成至前景後方的背景圖像。請提供背景圖像或背景影片，兩者擇一，不可同時提供。 | IMAGE | 否 | - |
| `background_video` | 合成至前景後方的背景影片。請提供背景圖像或背景影片，兩者擇一，不可同時提供。 | VIDEO | 否 | - |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果都是非確定性的。（預設值：0） | INT | 是 | 0 至 2147483647 |

**注意：** 您必須提供 `background_image` 或 `background_video` 其中之一——不能同時提供，也不能兩者都不提供。前景和背景影片都必須為 60 秒或更短。如果提供背景圖像，其上傳前會移除其 alpha（透明度）通道。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `video` | 背景被替換後的結果影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
