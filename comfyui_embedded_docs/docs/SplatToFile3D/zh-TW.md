# 建立 3D 檔案（由 Splat）

SplatToFile3D 將高斯潑濺（gaussian splat）轉換為 File3D 物件，可用於 Save 或 Preview 3D 節點。您可以選擇輸出檔案格式。此節點僅支援每批次一個項目；如果接收到多個項目，只會使用第一個並記錄警告。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `splat` | 要序列化到檔案的高斯潑濺資料。僅支援每批次一個項目。如果提供多個項目，只會使用第一個。 | SPLAT | 是 | - |
| `format` | 3D 檔案的輸出格式。ply：標準 3D Gaussian Splat，包含完整的球諧函數。ksplat：mkkellogg SplatBuffer（第 0 級，未壓縮），僅包含基礎顏色。spz：Niantic gzip 壓縮（約小 10 倍），僅包含基礎顏色（預設值："ply"） | COMBO | 是 | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 包含所選格式之序列化高斯潑濺資料的 File3D 物件，可用於儲存或預覽 | FILE3D |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
