# Bria 移除影片背景

此節點使用 Bria AI 服務移除影片的背景。它處理輸入影片，並將原始背景替換為您選擇的純色。此操作透過外部 API 執行，結果將作為新的影片檔案返回。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 輸入的影片檔案，將從中移除背景。 | VIDEO | 是 | N/A |
| `背景顏色` | 輸出影片的背景顏色。 | COMBO | 是 | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果都是非確定性的。（預設值：0） | INT | 是 | 0 到 2147483647 |

**注意：** 輸入影片的時長必須為 60 秒或以下。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 處理後的影片檔案，背景已移除並替換為所選顏色，編碼為使用 H.264 編解碼器的 MP4。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
