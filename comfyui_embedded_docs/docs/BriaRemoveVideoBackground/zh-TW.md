# Bria 移除影片背景

此節點使用 Bria AI 服務移除影片背景。它會處理輸入影片，並將原始背景替換為您選擇的純色。此操作會透過外部 API 執行，並以新的影片檔案傳回結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要移除背景的輸入影片檔案。 | VIDEO | 是 | N/A |
| `背景顏色` | 輸出影片的背景顏色。 | COMBO | 是 | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `種子` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的。（預設值：0） | INT | 是 | 0 至 2147483647 |

**注意：** 輸入影片的長度必須為 60 秒或更短。即使 `seed` 值保持不變，結果仍是非確定性的。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 已移除背景並替換為所選顏色的處理後影片檔案，以 H.264 編解碼器編碼為 MP4。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
