# SplatToFile3D 節點文檔

## ## 概述

SplatToFile3D 節點將高斯潑濺轉換為 File3D 物件，可與儲存或預覽 3D 節點搭配使用。此節點僅支援每批次一個項目，並允許您為匯出的 3D 資料選擇不同的輸出檔案格式。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `splat` | 要序列化為檔案的高斯潑濺資料 | SPLAT | 是 | - |
| `格式` | 3D 檔案的輸出格式。ply：標準 3D 高斯潑濺，包含完整球諧函數。ksplat：mkkellogg SplatBuffer（第 0 層，未壓縮），僅基礎顏色。spz：Niantic gzip 壓縮（約縮小 10 倍），僅基礎顏色（預設值："ply"） | COMBO | 是 | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 包含所選格式序列化高斯潑濺資料的 File3D 物件，可供儲存或預覽 | FILE3D |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c04fe04faa8ce81ad699e67c00d047550b0cadbfd037b687331f76944501a9f6`
