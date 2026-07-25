# 裁切影片（隨機時間區段）

隨機從輸入影片中裁切一段連續的幀範圍。裁切長度由 `length` 參數控制，起始位置則使用隨機種子選取。此節點以惰性方式運作，代表在輸出被下游使用之前，不會處理整個影片。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|------|------|----------|------|------|
| `影片` | 輸入影片。 | VIDEO | 是 | – |
| `保留長度` | 要保留的幀數。（預設值：16） | INT | 是 | min: 1, max: 99999 |
| `隨機種子` | 隨機種子。（預設值：0） | INT | 是 | min: 0, max: 0xFFFFFFFFFFFFFFFF |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|----------|------|----------|
| `影片` | 裁切後的影片（惰性）。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
