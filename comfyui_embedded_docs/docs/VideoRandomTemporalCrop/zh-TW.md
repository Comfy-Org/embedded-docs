# 裁切影片（隨機時間區段）

從輸入影片中隨機裁剪一段連續的影格。保留的影格數由 `length` 參數設定，起始位置使用 `seed` 參數隨機選擇。該節點以惰性方式執行，意味著在輸出被下游使用之前不會處理整個影片。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|------|------|----------|------|------|
| `影片` | 輸入影片。 | VIDEO | 是 | – |
| `保留影格數` | 保留的影格數。如果 `length` 大於影片中的總影格數，則保留整個影片。（預設值：16） | INT | 是 | 最小值：1，最大值：99999 |
| `隨機種子` | 隨機種子。（預設值：0） | INT | 是 | min: 0, max: 0xFFFFFFFFFFFFFFFF |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|----------|------|----------|
| `影片` | 裁切後的影片（惰性）。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
