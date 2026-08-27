# 建立 3D 檔案（由 Splat）

SplatToFile3D 節點會將高斯潑濺資料轉換為 File3D 物件，可與 Save 或 Preview 3D 節點搭配使用。每個批次僅支援一個項目，並可讓您為匯出的 3D 資料選擇不同的輸出檔案格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `splat` | 要序列化為檔案的高斯潑濺資料 | SPLAT | 是 | - |
| `格式` | 3D 檔案的輸出格式。ply：標準 3D 高斯潑濺，包含完整球諧函數。ksplat：mkkellogg SplatBuffer（第 0 級，未壓縮），僅基礎顏色。spz：Niantic gzip 壓縮（約縮小 10 倍），僅基礎顏色（預設："ply"） | COMBO | 是 | "ply"<br>"ksplat"<br>"spz" |

注意：此節點每個批次僅支援一個項目。如果輸入的 `splat` 在批次中包含多個項目，節點會記錄警告並使用第一個項目。如果提供了不支援的格式，節點會拋出錯誤。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `3D 模型` | 包含所選格式之序列化高斯潑濺資料的 File3D 物件，可用於儲存或預覽 | FILE3D |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
